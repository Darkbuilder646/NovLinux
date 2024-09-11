import os
import subprocess
import sys
from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore

class SuccessPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SuccessPage, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.icon_label = QtWidgets.QLabel(self)
        self.icon_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        icon_path = "/home/alexis/Desktop/T-YEP-600-LIL_13/frontend/images/success.png"  
        pixmap = QtGui.QPixmap(icon_path)
        self.icon_label.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio))

        self.layout.addWidget(self.icon_label)

        self.success_label = QtWidgets.QLabel(self)
        self.success_label.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#4CAF50;\">Success!</span></p></body></html>"
        )
        self.layout.addWidget(self.success_label)

        self.message_label = QtWidgets.QLabel(self)
        self.message_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.message_label.setWordWrap(True)
        self.layout.addWidget(self.message_label)

        self.open_folder_button = QtWidgets.QPushButton("Open\nProject\nFolder", self)
        self.open_folder_button.setStyleSheet(
            "padding: 0px; font-size: 12px; width: 100px; height: 100px; text-align: center;"
        )
        self.layout.addWidget(self.open_folder_button, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.open_folder_button.clicked.connect(self.open_project_folder)

        self.project_dir = ""

    def set_message(self, project_name, framework, project_dir, result):
        self.project_dir = os.path.join(project_dir, project_name)

        message_text = (
            f"<html><head/><body>"
            f"<p align=\"center\">Your {framework} project <b>{project_name}</b> has been successfully created!</p>"
            f"<p align=\"center\">{result}</p>"
            f"<p align=\"center\">You can find your project at:</p>"
            f"<p align=\"center\"><i>{self.project_dir}</i></p>"
            f"<p align=\"center\">Or simply click on the button below</p>"
            f"</body></html>"
        )
        self.message_label.setText(message_text)

    def open_project_folder(self):
        if os.path.isdir(self.project_dir):
            if os.name == 'nt':  # Windows
                os.startfile(self.project_dir)
            elif os.name == 'posix':  # macOS or Linux
                subprocess.Popen(['open', self.project_dir] if sys.platform == 'darwin' else ['xdg-open', self.project_dir])
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "The directory does not exist.")

