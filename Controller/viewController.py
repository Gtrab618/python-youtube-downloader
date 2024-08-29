from typing import Optional

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QFileDialog
from pytube import YouTube
import re


from Controller.threadController.manageThread import searchThread, downloadThread


class viewController(QObject):
    directory=""
    youtube: Optional[YouTube] = None
    def __init__(self, view):
        super().__init__()
        self.search_thread = None
        self.view = view
        self.connect_signals()
        self.manageThread=None


    def connect_signals(self):
        self.view.btnBuscar.clicked.connect(self.on_search_clicked)
        self.view.btnRuta.clicked.connect(self.on_choose_path_clicked)
        self.view.btnDescargar.clicked.connect(self.on_download_clicked)


    #search part
    def on_search_clicked(self):
        self.youtube=None
        self.view.cmbFormats.clear()
        url= self.view.inputUrl.text()
        if url:
            self.search_thread=searchThread(url)
            self.search_thread.streams_ready.connect(self.on_streams_ready)
            self.search_thread.error.connect(self.on_general_error)
            self.search_thread.start()

    def on_streams_ready(self, showDataStream,yt):
        self.view.cmbFormats.addItems(showDataStream)
        self.youtube=yt
        print("Streams disponibles cargados y yt disponible para descargar")



    def on_general_error(self, error_message):
        print(f"Error: {error_message}")


    #download part
    def on_download_clicked(self):
        itemStream=self.view.cmbFormats.currentText()
        if itemStream:
            if self.directory:
                self.download_thread=downloadThread(itemStream,self.youtube,self.directory)
                self.download_thread.finished.connect(self.on_download_ready)
                self.download_thread.error.connect(self.on_general_error)
                self.download_thread.start()
            else:
                print("seleccione una ubicacion")

        else:
            print("selecciona un formato para descargar")

    def on_download_ready(self,confirm_message):
        print(confirm_message)




    #directory
    def on_choose_path_clicked(self):
        self.directory=QFileDialog.getExistingDirectory(self.view,"Selecciona una carpeta")
        if self.directory:
            self.view.labelTargetSelected.setText(self.directory)

