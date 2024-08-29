
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel, \
    QLineEdit, QComboBox
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
             background-color: rgba(0, 0, 0, 1);
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
            selection-background-color: white;
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

        #cmbFormats.addItems(["option1", "option2", "option3"])
        #style
        labelUrl.setStyleSheet(labelStyle)
        self.inputUrl.setStyleSheet(inputStyle)

        #layou1
        layoutUrl= QHBoxLayout()
        layoutUrl.addWidget(labelUrl,1)
        layoutUrl.addWidget(self.inputUrl,8)
        layoutUrl.addWidget(self.btnBuscar,1)

        #layout2
        layoutFormat = QHBoxLayout()
        layoutFormat.addWidget(labelFormat,1)
        layoutFormat.addWidget(self.cmbFormats,8)
        layoutFormat.addWidget(self.btnDescargar,1)

        #layout3
        layoutTarget = QHBoxLayout()
        layoutTarget.addWidget(labelTarget,1)
        layoutTarget.addWidget(self.labelTargetSelected,8)
        layoutTarget.addWidget(self.btnRuta, 1)
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
        layoutMain.addWidget(self.web_view)  # Añade la vista web al diseño

        # Configura el widget central y el diseño
        central_widget = QWidget()
        central_widget.setLayout(layoutMain)
        self.setCentralWidget(central_widget)
        #

