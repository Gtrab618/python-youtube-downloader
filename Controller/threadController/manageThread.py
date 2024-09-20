import os
from typing import Optional
from PySide6.QtCore import QThread, Signal
from pytube import YouTube
import re
from moviepy.editor import VideoFileClip

from controller.threadController.soundThread import start_playing_saved, start_playing_error, start_playing_search


class downloadThread(QThread):
    finished = Signal(str)
    error=Signal(str)

    def __init__(self, streamSelected, ytStream, location,view):
        super().__init__()
        self.streamSelected = streamSelected
        self.yt: Optional[YouTube]=ytStream
        self.location= location
        self.view=view

    def run(self):
        try:
            if self.streamSelected!="audio-mp3":
                itag_macth = re.search(r"itag:\s*(\d+)", self.streamSelected)
                itag = int(itag_macth.group(1))

                stream = self.yt.streams.get_by_itag(itag)
                stream.download(output_path=self.location)

                #sound
                start_playing_saved()

                self.finished.emit(f"Video descargado: {stream.title}")
            else:
                stream = self.yt.streams.get_by_itag(18)
                video_path = stream.download(output_path=self.location)
                # Paso 2: Convertir el video a MP3
                audio_path = video_path.replace('.mp4', '.mp3')

                with VideoFileClip(video_path) as video_clip:
                    self.view.gif_labelDown.setVisible(False)
                    self.view.gif_labelConv.setVisible(True)
                    video_clip.audio.write_audiofile(audio_path)

                # Opcional: Elimina el archivo de video original
                video_clip.close()
                os.remove(video_path)

                start_playing_saved()

                self.finished.emit(f"Musica descargada {stream.title}")

        except Exception as e:
            start_playing_error()
            self.error.emit(str(e))




class searchThread(QThread):
    streams_ready=Signal(list,YouTube)
    error = Signal(str)

    def __init__(self,url):
        super().__init__()
        self.url=url

    def run(self):
        try:
            yt=YouTube(self.url)
            showDataStream = []
            if yt.streams:
                showDataStream.append("audio-mp3")
                for stream in yt.streams:

                    showDataStream.append(
                        f"itag: {stream.itag}, Tipo: {stream.mime_type}, Resolución: {stream.resolution}, Codec: {stream.codecs}")


                start_playing_search()
                self.streams_ready.emit(showDataStream,yt)

            else:
                start_playing_error()
                self.error.emit("No hay URL disponibles")

        except Exception as e:
            self.error.emit(str(e))
