from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from threading import Thread
from LoadingPage import LoadingPage

class RecapPage(QtWidgets.QWidget):
    back_clicked = QtCore.pyqtSignal()
    update_ui_signal = QtCore.pyqtSignal(str)
    go_to_success_page = QtCore.pyqtSignal(str, str, str, str)

    def __init__(self, parent=None):
        super(RecapPage, self).__init__(parent)
        self.setupUi()
        self.loading_page = LoadingPage()
        self.update_ui_signal.connect(self.update_ui)
        self.response_received = False
        self.timer_finished = False
        self.status = ""
        self.message = ""

# timer and progress
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_loading_progress)
        self.timer.setInterval(100)
        self.progress_value = 0

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.Label_Info = QtWidgets.QLabel(self)
        self.Label_Info.setObjectName("Label_Info")
        self.verticalLayout.addWidget(self.Label_Info)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        self.VL_Info = QtWidgets.QVBoxLayout()
        self.VL_Info.setObjectName("VL_Info")

# Name
        self.HL_Name = QtWidgets.QHBoxLayout()
        self.HL_Name.setObjectName("HL_Name")
        self.Label_Name = QtWidgets.QLabel(self)
        self.Label_Name.setObjectName("Label_Name")
        self.HL_Name.addWidget(self.Label_Name)
        self.Answer_Name = QtWidgets.QLabel(self)
        self.Answer_Name.setObjectName("Answer_Name")
        self.HL_Name.addWidget(self.Answer_Name)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.HL_Name.addItem(spacerItem1)
        self.VL_Info.addLayout(self.HL_Name)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.VL_Info.addItem(spacerItem2)

# Path
        self.HL_Path = QtWidgets.QHBoxLayout()
        self.HL_Path.setObjectName("HL_Path")
        self.Label_Path = QtWidgets.QLabel(self)
        self.Label_Path.setObjectName("Label_Path")
        self.HL_Path.addWidget(self.Label_Path)
        self.Answer_Path = QtWidgets.QLabel(self)
        self.Answer_Path.setObjectName("Answer_Path")
        self.HL_Path.addWidget(self.Answer_Path)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.HL_Path.addItem(spacerItem3)
        self.VL_Info.addLayout(self.HL_Path)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.VL_Info.addItem(spacerItem4)

# Language
        self.HL_Language = QtWidgets.QHBoxLayout()
        self.HL_Language.setObjectName("HL_Language")
        self.Label_Language = QtWidgets.QLabel(self)
        self.Label_Language.setObjectName("Label_Language")
        self.HL_Language.addWidget(self.Label_Language)
        self.Answer_Language = QtWidgets.QLabel(self)
        self.Answer_Language.setObjectName("Answer_Language")
        self.HL_Language.addWidget(self.Answer_Language)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.HL_Language.addItem(spacerItem5)
        self.VL_Info.addLayout(self.HL_Language)

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.VL_Info.addItem(spacerItem6)

# Framework
        self.HL_Framework = QtWidgets.QHBoxLayout()
        self.HL_Framework.setObjectName("HL_Framework")
        self.Label_Framework = QtWidgets.QLabel(self)
        self.Label_Framework.setObjectName("Label_Framework")
        self.HL_Framework.addWidget(self.Label_Framework)
        self.Answer_Framework = QtWidgets.QLabel(self)
        self.Answer_Framework.setObjectName("Answer_Framework")
        self.HL_Framework.addWidget(self.Answer_Framework)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.HL_Framework.addItem(spacerItem7)
        self.VL_Info.addLayout(self.HL_Framework)

        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.VL_Info.addItem(spacerItem8)

# Git
        self.HL_Git = QtWidgets.QHBoxLayout()
        self.HL_Git.setObjectName("HL_Git")
        self.Label_Git = QtWidgets.QLabel(self)
        self.Label_Git.setObjectName("Label_Git")
        self.HL_Git.addWidget(self.Label_Git)
        self.Answer_Git = QtWidgets.QLabel(self)
        self.Answer_Git.setObjectName("Answer_Git")
        self.HL_Git.addWidget(self.Answer_Git)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.HL_Git.addItem(spacerItem9)
        self.VL_Info.addLayout(self.HL_Git)

        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.VL_Info.addItem(spacerItem10)

# Buttons
        self.HL_Button = QtWidgets.QHBoxLayout()
        self.HL_Button.setObjectName("HL_Button")
        self.Back_Button = QtWidgets.QPushButton(self)
        self.Back_Button.setObjectName("Back_Button")
        self.Back_Button.clicked.connect(self.back_clicked)
        self.HL_Button.addWidget(self.Back_Button)
        self.Confirm_Button = QtWidgets.QPushButton(self)
        self.Confirm_Button.setObjectName("Confirm_Button")
        self.HL_Button.addWidget(self.Confirm_Button)
        self.VL_Info.addLayout(self.HL_Button)
        
        self.verticalLayout.addLayout(self.VL_Info)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Recap Page"))
        self.Label_Info.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Recap Information</span></p></body></html>"))
        self.Label_Name.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Name : </span></p></body></html>"))
        self.Answer_Name.setText(_translate("Form", ""))
        self.Label_Path.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Path :</span></p></body></html>"))
        self.Answer_Path.setText(_translate("Form", ""))
        self.Label_Language.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Language :</span></p></body></html>"))
        self.Answer_Language.setText(_translate("Form", ""))
        self.Label_Framework.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Framework :</span></p></body></html>"))
        self.Answer_Framework.setText(_translate("Form", ""))
        self.Label_Git.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Git :</span></p></body></html>"))
        self.Answer_Git.setText(_translate("Form", ""))
        self.Back_Button.setText(_translate("Form", "Back"))
        self.Confirm_Button.setText(_translate("Form", "Confirm"))
        self.Confirm_Button.clicked.connect(self.send_data)

# Methods for processing data
    def set_recap_data(self, name, path, language, framework, git_enabled, docker_enabled):
        self.Answer_Name.setText(f"{name}")
        self.Answer_Path.setText(f"{path}")
        self.Answer_Language.setText(f"{language}")
        self.Answer_Framework.setText(f"{framework}")
        self.Answer_Git.setText("Oui" if git_enabled else "Non")

    def send_data(self):
        self.progress_value = 0
        self.loading_page.show_loading_page()
        self.timer.start()
        Thread(target=self._install_dependencies).start()

    def _install_dependencies(self):
        language = self.Answer_Language.text()
        framework = self.Answer_Framework.text()
        url = f"http://localhost:5000/install/{language}/{framework}"
        try:
            response = requests.post(url)
            response.raise_for_status()
            result = response.json()
            if result.get('error'):
                self.update_ui_signal.emit(f"Installation Error: {result.get('error')}")
            else:
                print(f"Installation Output: {result.get('output')}")
                self._send_data()
        except requests.RequestException as e:
            self.update_ui_signal.emit(f"Installation Error: {str(e)}")

    def _send_data(self):
        data = {
            "language": self.Answer_Language.text(),
            "framework": self.Answer_Framework.text(),
            "project_name": self.Answer_Name.text(),
            "project_path": self.Answer_Path.text()
        }
        url = "http://localhost:5000/run_with_details"
        try:
            response = requests.post(url, json=data, headers={"Content-Type": "application/json"})
            response.raise_for_status()
            result = response.json()
            output_message = result.get('output', '')
            self.result_data = output_message  
            print(f"{self.result_data}")           
            self.response_received = True
            self.update_ui_signal.emit(str(result))
        except requests.RequestException as e:
            self.update_ui_signal.emit(str(e))

    def update_loading_progress(self):
        if not self.response_received:  # Only update progress while waiting for the response
            if self.progress_value < 90:
                self.progress_value += 100 / 60  # Adjust the increment value as needed
                self.loading_page.update_progress(int(self.progress_value))
            else:
                self.progress_value = 90  # Ensure it stays at 90%
                self.loading_page.update_progress(90)  # Update the loading page to show 90%
        else:  # If response received, complete the progress
            if self.progress_value < 100:  # Only increase to 100% if it hasn't already
                self.progress_value = 100
                self.loading_page.update_progress(100)
                self.timer.stop()  # Stop the timer

        self.check_transition()

    def check_transition(self):
        if self.response_received and self.progress_value == 100:
            self.loading_page.hide_loading_page()  # Hide loading page
            self.go_to_success_page.emit(self.Answer_Name.text(), 
                                         self.Answer_Framework.text(), 
                                         self.Answer_Path.text(), 
                                         self.result_data)

    def update_ui(self, message):
        self.response_received = True
        self.message = message  
        self.check_transition()

