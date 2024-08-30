import os
import subprocess
from fileinput import filename
from typing import Optional

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QFileDialog, QMessageBox
from pytube import YouTube


from controller.threadController.manageThread import searchThread, downloadThread


class viewController(QObject):
    directory=""
    youtube: Optional[YouTube] = None
    def __init__(self, view):
        super().__init__()
        self.search_thread = None
        self.view = view
        self.connect_signals()
        self.manageThread=None
        self.search_directory()




    def connect_signals(self):
        self.view.btnBuscar.clicked.connect(self.on_search_clicked)
        self.view.btnRuta.clicked.connect(self.on_choose_path_clicked)
        self.view.btnDescargar.clicked.connect(self.on_download_clicked)
        self.view.btnWindonws.clicked.connect(self.open_windows)

    #search part
    def on_search_clicked(self):
        self.youtube=None
        self.view.cmbFormats.clear()
        url= self.view.inputUrl.text()
        if url:
            self.view.gif_labelSearch.setVisible(True)
            self.view.btnBuscar.setEnabled(False)
            self.search_thread=searchThread(url)
            self.search_thread.streams_ready.connect(self.on_streams_ready)
            self.search_thread.error.connect(self.on_search_error)
            self.search_thread.start()

    def on_streams_ready(self, showDataStream,yt):
        self.view.cmbFormats.addItems(showDataStream)
        self.youtube=yt
        self.view.gif_labelSearch.setVisible(False)
        self.view.btnBuscar.setEnabled(True)



    def on_search_error(self, error_message):

        self.view.btnBuscar.setEnabled(True)
        self.view.gif_labelSearch.setVisible(False)
        #normalmente error bad response 400

        match error_message:
          case r"regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*":

            self.show_alert("Revice la url", "La url puede estar mal")

          case "HTTP Error 400: Bad Request":
              self.show_alert("Error conexion", "Reinicie la app o el wifi")

          case "<urlopen error [Errno 11001] getaddrinfo failed>":
              self.show_alert("Error Internet", "Sin conexión a internet")
          case _:
              if "is unavailable" in error_message:
                  self.show_alert("Url incorrect", "La url no pertence a youtube")



    def on_download_error(self, error_message):
        self.view.btnDescargar.setEnabled(True)
        # normalmente error bad response 400
        print(f"Error: {error_message}")

    #download part
    def on_download_clicked(self):
        itemStream=self.view.cmbFormats.currentText()
        if itemStream:
            if self.directory:
                self.view.gif_labelDown.setVisible(True)
                self.view.btnDescargar.setEnabled(False)
                self.download_thread=downloadThread(itemStream,self.youtube,self.directory,self.view)
                self.download_thread.finished.connect(self.on_download_ready)
                self.download_thread.error.connect(self.on_download_error)
                self.download_thread.start()

            else:

                self.show_alert("Selecione una ubicación","No ha seleccionado una ubicación")

        else:
            self.show_alert("selecciona un formato para descargar", "Seleccione itag 18 o Mp3")


    def open_windows(self):
        if self.directory:
            path = f'"{self.directory}"'
            os.startfile(path)



    def on_download_ready(self,confirm_message):
        self.view.btnDescargar.setEnabled(True)
        self.view.gif_labelDown.setVisible(False)
        self.view.gif_labelConv.setVisible(False)



    #directory
    def on_choose_path_clicked(self):
        self.directory=QFileDialog.getExistingDirectory(self.view,"Selecciona una carpeta")
        if self.directory:
            self.view.labelTargetSelected.setText(self.directory)
            with open("paths.txt", "w") as file:
                file.write(self.directory)


    def search_directory(self):
        try:
            with open("paths.txt","r") as file:
                path= file.readline()
                self.directory=path
                self.view.labelTargetSelected.setText(self.directory)
                return path
        except FileNotFoundError:

            return ""

    def show_alert(self,title,text):
        alert = QMessageBox()
        alert.setWindowTitle(title)
        alert.setText(text)
        alert.setIcon(QMessageBox.Information)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()