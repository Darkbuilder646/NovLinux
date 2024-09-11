from PyQt6 import QtCore, QtWidgets, QtGui

class LoadingPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LoadingPage, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.progress_bar = QtWidgets.QProgressBar(parent=Form)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_bar.setMaximum(100)
        self.verticalLayout.addWidget(self.progress_bar)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Loading"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Your project is being set up, please wait a moment</p></body></html>"))

    def show_loading_page(self):
        self.progress_bar.setValue(0)
        self.show()

    def hide_loading_page(self):
        self.hide()

    def update_progress(self, progress_value):
        self.progress_bar.setValue(progress_value)
