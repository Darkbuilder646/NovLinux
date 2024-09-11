from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtGui import QIcon
from HomePage import HomePage
from InfoPage import InfoPage
from RecapPage import RecapPage
from LoadingPage import LoadingPage
from SuccessPage import SuccessPage
import os


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("FullStart")
        self.resize(800, 600)

        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file_path)
        images_directory = os.path.join(current_directory, 'images')
        image_path = os.path.join(images_directory, "SmallLogo.png")
        print(image_path)

        self.setWindowIcon(QIcon(image_path))
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_page = HomePage(self)
        self.project_info_page = InfoPage(self)
        self.recap_page = RecapPage(self)
        self.loading_page = LoadingPage()
        self.success_page = SuccessPage(self)

# Create the pages
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.project_info_page)
        self.stacked_widget.addWidget(self.recap_page)
        self.stacked_widget.addWidget(self.loading_page)
        self.stacked_widget.addWidget(self.success_page)

# Navigation between pages
        self.home_page.language_selected.connect(self.go_to_project_info_page)
        self.project_info_page.go_to_recap_page.connect(self.go_to_recap_page)
        self.recap_page.back_clicked.connect(self.go_to_project_info_page_from_recap)
        self.recap_page.go_to_success_page.connect(self.go_to_success_page)
        self.project_info_page.back_clicked.connect(self.go_to_home_page)
        

# Method for navigation 
    def go_to_project_info_page(self, language):
        self.selected_language = language
        self.project_info_page.set_language(language)
        self.project_info_page.MainTitle.setText(f"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">{language} Project</span></p></body></html>")
        self.stacked_widget.setCurrentIndex(1)

    def go_to_recap_page(self, project_name, framework, project_dir, docker_enabled, git_enabled):
        self.recap_page.set_recap_data(
            project_name, project_dir, self.selected_language, framework, git_enabled, docker_enabled
        )
        self.stacked_widget.setCurrentIndex(2)

    def go_to_project_info_page_from_recap(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_home_page(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def go_to_success_page(self, project_name, framework, project_dir, result):
        self.success_page.set_message(project_name, framework, project_dir, result)
        self.stacked_widget.setCurrentIndex(4)


