from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import requests
import os

class InfoPage(QtWidgets.QWidget):
    back_clicked = QtCore.pyqtSignal()
    go_to_recap_page = QtCore.pyqtSignal(str, str, str, bool, bool)

    def __init__(self, parent=None):
        super(InfoPage, self).__init__(parent)
        self.language = None
        self.docker_enabled = False
        self.git_enabled = False
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.VL_Main = QtWidgets.QVBoxLayout()
        self.VL_Main.setObjectName("VL_Main")
        self.MainTitle = QtWidgets.QLabel(self)
        self.MainTitle.setObjectName("MainTitle")
        self.VL_Main.addWidget(self.MainTitle)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.VL_Main.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
# Name selection
        self.Name = QtWidgets.QLabel(self)
        self.Name.setObjectName("Name")
        self.horizontalLayout_3.addWidget(self.Name)
        self.LineName = QtWidgets.QLineEdit(self)
        self.LineName.setObjectName("LineName")
        self.horizontalLayout_3.addWidget(self.LineName)
        self.VL_Main.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
# Path selection 
        self.Path = QtWidgets.QLabel(self)
        self.Path.setObjectName("Path")
        self.horizontalLayout_2.addWidget(self.Path)
        self.LinePath = QtWidgets.QLineEdit(self)
        self.LinePath.setObjectName("LinePath")
        self.horizontalLayout_2.addWidget(self.LinePath)
# Browse button 
        self.browseButton = QtWidgets.QPushButton(self)
        self.browseButton.setText("")
        icon = QtGui.QIcon.fromTheme("folder-open")
        self.browseButton.setIcon(icon)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.VL_Main.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.VL_Main)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
# Frameworks selection 
        self.VL_Framework = QtWidgets.QVBoxLayout()
        self.VL_Framework.setObjectName("VL_Framework")
        self.Framework = QtWidgets.QLabel(self)
        self.Framework.setObjectName("Framework")
        self.VL_Framework.addWidget(self.Framework)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.VL_Framework.addWidget(self.comboBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.VL_Framework.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.VL_Framework)
# Options 
        self.VL_Options = QtWidgets.QVBoxLayout()
        self.VL_Options.setObjectName("VL_Options")
        self.Options = QtWidgets.QLabel(self)
        self.Options.setObjectName("Options")
        self.VL_Options.addWidget(self.Options)
        self.HL_Git = QtWidgets.QHBoxLayout()
        self.HL_Git.setObjectName("HL_Git")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.HL_Git.addItem(spacerItem5)
        self.checkBox_Git = QtWidgets.QCheckBox("Git", self)
        self.checkBox_Git.setObjectName("checkBox_Git")
        self.HL_Git.addWidget(self.checkBox_Git)
        self.VL_Options.addLayout(self.HL_Git)
        self.HL_DOcker = QtWidgets.QHBoxLayout()
        self.HL_DOcker.setObjectName("HL_DOcker")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.HL_DOcker.addItem(spacerItem6)
        self.checkBox_Docker = QtWidgets.QCheckBox("Docker", self)
        self.checkBox_Docker.setObjectName("checkBox_Docker")
        self.HL_DOcker.addWidget(self.checkBox_Docker)
        self.VL_Options.addLayout(self.HL_DOcker)
        self.verticalLayout.addLayout(self.VL_Options)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
# Buttons 
        self.VL_Button = QtWidgets.QVBoxLayout()
        self.VL_Button.setObjectName("VL_Button")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back = QtWidgets.QPushButton(self)
        self.Back.setObjectName("Back")
        self.horizontalLayout.addWidget(self.Back)
        self.Next = QtWidgets.QPushButton(self)
        self.Next.setObjectName("Next")
        self.horizontalLayout.addWidget(self.Next)
        self.VL_Button.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.VL_Button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

# Connect the buttons to the methods
        self.browseButton.clicked.connect(self.browseFolder)
        self.Back.clicked.connect(self.on_back_clicked)
        self.Next.clicked.connect(self.on_next_clicked)

        self.checkBox_Docker.stateChanged.connect(self.update_docker_status)
        self.checkBox_Git.stateChanged.connect(self.update_git_status)

    def browseFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.LinePath.setText(folder_path)

    def on_back_clicked(self):
        self.LineName.clear()
        self.LinePath.clear()
        self.LineName.setStyleSheet("")
        self.LinePath.setStyleSheet("")
        self.LineName.setPlaceholderText("")
        self.LinePath.setPlaceholderText("")
        self.back_clicked.emit()

    def update_docker_status(self, state):
        self.docker_enabled = (state == QtCore.Qt.CheckState.Checked.value)
    def update_git_status(self, state):
        self.git_enabled = (state == QtCore.Qt.CheckState.Checked.value)

    def on_next_clicked(self):
        project_name = self.LineName.text().strip()
        project_dir = self.LinePath.text().strip()

# ElseIf for managing errors
        if not project_name:
            self.LineName.setPlaceholderText("You have to complete the field")
            self.LineName.setStyleSheet("border: 2px solid red; border-radius: 5px; height: 30px;")
        else:
            self.LineName.setStyleSheet("")

        if not project_dir:
            self.LinePath.setPlaceholderText("You have to complete the field")
            self.LinePath.setStyleSheet("border: 2px solid red; border-radius: 5px; height: 30px;")
        else:
            self.LinePath.setStyleSheet("")

        if project_name and project_dir:
            if os.path.isdir(project_dir):
                framework = self.comboBox.currentText()
                self.go_to_recap_page.emit(project_name, framework, project_dir, self.docker_enabled, self.git_enabled)
            else:
                QtWidgets.QMessageBox.warning(self, "Invalid Path", "The specified path does not exist. Please enter a valid path.")
                self.LinePath.setFocus()
                self.LinePath.selectAll()
                self.LinePath.setStyleSheet("border: 2px solid red; border-radius: 5px; height: 30px;")

# Method to fetch frameworks
    def set_language(self, language):
        self.language = language
        self.framework_url = f"http://127.0.0.1:5000/frameworks/{language}"  
        self.framework = self.fetch_framework() 
        self.update_frameworks_combobox(self.framework)
    
    def update_frameworks_combobox(self, frameworks):
        self.comboBox.clear()  
        for framework in frameworks:
            self.comboBox.addItem(framework)  

    def fetch_framework(self):
        try:
            response = requests.get(self.framework_url)
            response.raise_for_status()
            framework = response.json()
            return framework
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Name.setText(_translate("Form", "Name:"))
        self.Path.setText(_translate("Form", "Path:"))
        self.Framework.setText(_translate("Form", "Framework"))
        self.Options.setText(_translate("Form", "Other Options:"))
        self.Back.setText(_translate("Form", "Back"))
        self.Next.setText(_translate("Form", "Next"))
