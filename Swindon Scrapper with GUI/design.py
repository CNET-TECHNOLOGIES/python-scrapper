from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from configparser import ConfigParser
from documents import Documents
from summary import Summary
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from searchresults import SearchResults


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.check_path()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftside = QtWidgets.QWidget(self.centralwidget)
        self.leftside.setStyleSheet("QWidget{\n"
                                    "background-color:rgb(83, 83, 83);\n"
                                    "}\n"
                                    "\n"
                                    "QLabel{\n"
                                    "width:auto;\n"
                                    "color:#ffffff;\n"
                                    "text-align:center;\n"
                                    "font-size:25px;\n"
                                    "height:auto;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.leftside.setObjectName("leftside")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftside)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.leftside)
        self.widget_6.setStyleSheet("QWidget{\n"
                                    "text-align:center;\n"
                                    "}\n"
                                    "")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_6)
        self.label.setStyleSheet("text-align:center;\n")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_4 = QtWidgets.QWidget(self.leftside)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.leftside)
        self.rightside = QtWidgets.QWidget(self.centralwidget)
        self.rightside.setStyleSheet("QCheckBox\n"
                                     "{\n"
                                     "width:auto;\n"
                                     "height: auto;\n"
                                     "font-size:15px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton\n"
                                     "{\n"
                                     "width:20px;\n"
                                     "height:20px;\n"
                                     "font-size:15px;\n"
                                     "}")
        self.rightside.setObjectName("rightside")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightside)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.rightside)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.searchresult_checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.searchresult_checkBox.setObjectName("searchresult_checkBox")
        self.verticalLayout_4.addWidget(self.searchresult_checkBox)

        self.summary_checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.summary_checkBox.setObjectName("summary_checkBox")
        self.verticalLayout_4.addWidget(self.summary_checkBox)

        self.documents_checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.documents_checkBox.setObjectName("documents_checkBox")
        self.verticalLayout_4.addWidget(self.documents_checkBox)

        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.rightside)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.rightside)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSelect_Dump_Folder = QtWidgets.QAction(MainWindow)
        self.actionSelect_Dump_Folder.setObjectName("actionSelect_Dump_Folder")
        self.menuMenu.addAction(self.actionSelect_Dump_Folder)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # title
        self.label.setText(_translate("MainWindow", "Swindon"))
        self.label_3.setText(_translate("MainWindow", "Demo"))

        # checkbox
        self.searchresult_checkBox.setText(_translate("MainWindow", "SearchResults"))
        self.summary_checkBox.setText(_translate("MainWindow", "Summary"))
        self.documents_checkBox.setText(_translate("MainWindow", "Documents"))
        # self.checkBox_4.setText(_translate("MainWindow", "All"))

        # submit button
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton.clicked.connect(self.main)

        # Menu bar
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSelect_Dump_Folder.setText(_translate("MainWindow", "Select Dump Folder"))
        self.actionSelect_Dump_Folder.triggered.connect(self.openFileNameDialog)

    def openFileNameDialog(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder To Store Data')
        self.config.set("INFO", "path", self.path)
        with open("config.ini", "w") as conf:
            self.config.write(conf)

    def check_path(self):
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.path = self.config.get("INFO", "path")
        if not self.path:
            self.openFileNameDialog()

    def store_months(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.headless = True
        args = ["hide_console", ]
        self.driver = webdriver.Chrome(options=options, service_args=args)
        self.driver.get("https://pa1.swindon.gov.uk/publicaccess/search.do?action=monthlyList")

        # Main page Month selection
        select = Select(self.driver.find_element(By.ID, "month"))
        self.temp_month = [i.text for i in select.options]
        print(self.temp_month)
        self.config.set("INFO", "months", ",".join(self.temp_month))
        with open("config.ini", "w") as conf:
            self.config.write(conf)
        self.driver.quit()

    def main(self):

        self.store_months()
        try:
            if self.searchresult_checkBox.isChecked():
                try:
                    self.temp_month = self.config.get("INFO", "months").split(",")
                    SearchResults.fetch_results_validated(self.temp_month, self.path)
                    print("Validated SearchResults Completed")
                    SearchResults.fetch_results_decided(self.temp_month, self.path)
                    print("Decided SearchResults Completed")

                except Exception as e:
                    print(e)
        except:
            pass
        try:
            if self.summary_checkBox.isChecked():
                try:
                    self.temp_month = self.config.get("INFO", "months").split(",")
                    Summary.scrape_summary_validated(self.temp_month, self.path)
                    print("Validated Summary Completed")
                    Summary.scrape_summary_decided(self.temp_month, self.path)
                    print("Decided Summary Completed")
                except Exception as e:
                    print(e)
        except:
            pass
        try:
            if self.documents_checkBox.isChecked():
                try:
                    self.temp_month = self.config.get("INFO", "months").split(",")
                    Documents.scrape_documents_validated(self.temp_month, self.path)
                    print("Validated Documents completed")
                    Documents.scrape_documents_decided(self.temp_month, self.path)
                    print("Decided Documents Completed")

                except Exception as e:
                    print(e)
        except:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
