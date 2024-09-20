import os.path
import sys

from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel, \
    QLineEdit, QComboBox, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView


class viewDonwloader(QMainWindow):
    def __init__(self):
        super().__init__()


        # Configura la ventana principal
        self.setWindowTitle("GtDownloader")
        self.setGeometry(100, 100, 1000, 500)

        # style
        btnStyle = """ 
        QPushButton {
             background-color: gray;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            color:white;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        }
        QPushButton:pressed {
            background-color: rgba(0, 150, 255, 0.5);
            transform: scale(1.05);
        }
        """

        labelStyle="""
        QLabel {

            border: 2px solid gray;
            padding: 5px;
            font: bold 14px;
            border-radius: 3px;
            opacity: 200;
            width: 13px;
        }
        """

        inputStyle="""
        QLineEdit {
            border: 2px solid gray;
            padding: 3px 5px;
            selection-background-color: gray;
        }
        """

        cmbStyle="""
        QComboBox {
            border: 1px solid gray;
            border-radius: 3px;
            padding: 3px 5px;
            min-width: 6em;
        }
        """
        # Configura los botones
        self.btnBuscar = QPushButton("Buscar")
        self.btnBuscar.setStyleSheet(btnStyle)

        self.btnDescargar = QPushButton("Descargar")
        self.btnDescargar.setStyleSheet(btnStyle)

        self.btnRuta = QPushButton("Elegir ruta")
        self.btnRuta.setStyleSheet(btnStyle)

        # ingresar url y salida
        labelUrl= QLabel("Url del video")
        self.inputUrl=QLineEdit()

        labelFormat = QLabel("Formato de salida")
        self.cmbFormats= QComboBox()

        labelTarget = QLabel("Guardar en:")
        self.labelTargetSelected = QLabel("Ruta no seleccionada")

        # laber title download
        self.labelTitleDownload = QLabel("")
        self.labelTitleDownload.setStyleSheet("color: green;")
        #cmbFormats.addItems(["option1", "option2", "option3"])
        #style
        labelUrl.setStyleSheet(labelStyle)
        self.inputUrl.setStyleSheet(inputStyle)


        #btn abrir explorador################
        self.btnWindonws = QPushButton("Abrir ruta descargas")
        self.btnWindonws.setStyleSheet(btnStyle)

        #area de testeo

        gif_relativeLoad = os.path.join("..", "assets", "loading.gif")
        gif_relativeDown = os.path.join("..", "assets", "download.gif")
        gif_relativeConv = os.path.join("..", "assets", "disc.gif")
        # creacion de gifs
        self.gif_labelSearch = QLabel()
        self.gif_labelSearch.setFixedSize(25,25)
        self.gif_movie = QMovie(gif_relativeLoad)
        self.gif_movie.setScaledSize(QSize(25,25))
        self.gif_labelSearch.setMovie(self.gif_movie)
        self.gif_labelSearch.setVisible(False)
        self.gif_movie.start()

        self.gif_labelDown = QLabel()
        self.gif_labelDown.setFixedSize(25, 25)
        self.gif_movie2 = QMovie(gif_relativeDown)
        self.gif_movie2.setScaledSize(QSize(25, 25))
        self.gif_labelDown.setMovie(self.gif_movie2)
        self.gif_labelDown.setVisible(False)
        self.gif_movie2.start()

        self.gif_labelConv = QLabel()
        self.gif_labelConv.setFixedSize(25, 25)
        self.gif_movie3 = QMovie(gif_relativeConv)
        self.gif_movie3.setScaledSize(QSize(25, 25))
        self.gif_labelConv.setMovie(self.gif_movie3)
        self.gif_labelConv.setVisible(False)
        self.gif_movie3.start()

        #layou1
        layoutUrl= QHBoxLayout()
        layoutUrl.addWidget(labelUrl,1)
        layoutUrl.addWidget(self.inputUrl,8)
        layoutUrl.addWidget(self.btnBuscar,1)
        layoutUrl.addWidget(self.gif_labelSearch)
        #layout2
        layoutFormat = QHBoxLayout()
        layoutFormat.addWidget(labelFormat,1)
        layoutFormat.addWidget(self.cmbFormats,8)
        layoutFormat.addWidget(self.btnDescargar,1)
        layoutFormat.addWidget(self.gif_labelDown)
        layoutFormat.addWidget(self.gif_labelConv)
        #layout3
        layoutTarget = QHBoxLayout()
        layoutTarget.addWidget(labelTarget,1)
        layoutTarget.addWidget(self.labelTargetSelected,7)
        layoutTarget.addWidget(self.labelTitleDownload, 1)
        layoutTarget.addWidget(self.btnRuta, 1)

        #layout 4################3
        ##########################
        layoutOptions = QHBoxLayout()
        layoutOptions.addWidget(self.btnWindonws)

        #style
        labelFormat.setStyleSheet(labelStyle)
        self.cmbFormats.setStyleSheet(cmbStyle)
        # Configura la vista web
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://www.youtube.com/"))

        # Configura el diseño principal
        layoutMain = QVBoxLayout()

        #insersion de los componentes
        layoutMain.addLayout(layoutUrl)# añadir la barra para ingresar la url
        layoutMain.addLayout(layoutFormat)# añadir formatos
        layoutMain.addLayout(layoutTarget)
        layoutMain.addLayout(layoutOptions)
        layoutMain.addWidget(self.web_view)  # Añade la vista web al diseño

        # Configura el widget central y el diseño
        central_widget = QWidget()
        central_widget.setLayout(layoutMain)
        self.setCentralWidget(central_widget)

