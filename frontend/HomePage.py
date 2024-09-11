from PyQt6 import QtCore, QtGui, QtWidgets
import requests
import os

class HomePage(QtWidgets.QWidget):
    language_selected = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self)  
        self.mainLayout.setObjectName("mainLayout")
        
        self.titleLayout = QtWidgets.QVBoxLayout()
        self.titleLayout.setObjectName("titleLayout")
        
        self.MainTitle = QtWidgets.QLabel(self)
        self.MainTitle.setObjectName("MainTitle")
        self.MainTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLayout.addWidget(self.MainTitle)
        
        self.SecondTitle = QtWidgets.QLabel(self)
        self.SecondTitle.setObjectName("SecondTitle")
        self.SecondTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLayout.addWidget(self.SecondTitle)

        self.mainLayout.addLayout(self.titleLayout)

        self.languagesLayout = QtWidgets.QVBoxLayout()
        self.languagesLayout.setObjectName("languagesLayout")

        self.languages_url = "http://127.0.0.1:5000/languages"
        self.languages = self.fetch_languages()

# Create the rows of language buttons
        row_layout = None
        for index, language in enumerate(self.languages):
            if index % 5 == 0:
                row_layout = QtWidgets.QHBoxLayout()
                self.languagesLayout.addLayout(row_layout)

                spacer_left = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                spacer_right = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                row_layout.addItem(spacer_left)
                row_layout.addItem(spacer_right)

                row_layout.setSpacing(30)  
            
            self.createLanguageFrame(language, row_layout)
            
        self.mainLayout.addLayout(self.languagesLayout)

        self.mainLayout.setStretch(0, 1)  
        self.mainLayout.setStretch(1, 2)  

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

# Create the language buttons
    def createLanguageFrame(self, language, layout):
        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        verticalLayout = QtWidgets.QVBoxLayout(frame)

        # Dynamically construct the path to the image
        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file_path)
        images_directory = os.path.join(current_directory, 'images')
        image_path = os.path.join(images_directory, f"{language}.png")
        print(image_path)

        button = QtWidgets.QToolButton(frame)
        button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        pixmap = QtGui.QPixmap(image_path)
        button.setIcon(QtGui.QIcon(pixmap))
        button.setIconSize(QtCore.QSize(64, 64))
        button.setText(language)
        button.setFixedSize(100, 100)
        button.setStyleSheet("QToolButton { font-weight: bold; font-size: 14px}")
        button.setAutoRaise(True) 
        button.clicked.connect(lambda: self.language_selected.emit(language))
        verticalLayout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)

        layout.insertWidget(layout.count() - 1, frame)

    def fetch_languages(self):
        try:
            response = requests.get(self.languages_url)
            response.raise_for_status()
            languages = response.json()
            return languages
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Welcome to </span><span style=\" font-size:14pt; font-weight:700;\">FullStart</span><span style=\" font-size:14pt;\"> !</span></p></body></html>"))
        self.SecondTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Select a language to create a new project </span></p></body></html>"))
