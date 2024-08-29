from typing import Optional

from PySide6.QtCore import QThread, Signal
from pytube import YouTube
import re

class downloadThread(QThread):
    finished = Signal(str)
    error=Signal(str)

    def __init__(self, streamSelected, ytStream, location):
        super().__init__()
        self.streamSelected = streamSelected
        self.yt: Optional[YouTube]=ytStream
        self.location= location

    def run(self):
        try:
            itag_macth = re.search(r"itag:\s*(\d+)", self.streamSelected)
            itag = int(itag_macth.group(1))

            stream = self.yt.streams.get_by_itag(itag)
            stream.download(output_path=self.location)
            self.finished.emit(f"Video descargado en {self.location}")
        except Exception as e:
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
                for stream in yt.streams:
                    print(f"itag: {stream.itag}, Tipo: {stream.mime_type}, Resolución: {stream.resolution}, Codec: {stream.codecs}")
                    showDataStream.append(
                        f"itag: {stream.itag}, Tipo: {stream.mime_type}, Resolución: {stream.resolution}, Codec: {stream.codecs}")
                self.streams_ready.emit(showDataStream,yt)

            else:
                self.error.emit("No hay URL disponibles")

        except Exception as e:
            self.error.emit(str(e))
