# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autofalloff/assets/basic_layout.ui'
#
# Created: Wed Apr 13 09:11:23 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 597)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 371, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.frame_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidgetReference = QtGui.QStackedWidget(self.frame_2)
        self.stackedWidgetReference.setGeometry(QtCore.QRect(10, 20, 321, 321))
        self.stackedWidgetReference.setObjectName("stackedWidgetReference")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.labelReferenceImage = QtGui.QLabel(self.page)
        self.labelReferenceImage.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.labelReferenceImage.setObjectName("labelReferenceImage")
        self.stackedWidgetReference.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidgetReference.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 190, 351, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.frame_3 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stackedWidgetSource = QtGui.QStackedWidget(self.frame_3)
        self.stackedWidgetSource.setGeometry(QtCore.QRect(10, 20, 321, 321))
        self.stackedWidgetSource.setObjectName("stackedWidgetSource")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.labelReferenceImage_2 = QtGui.QLabel(self.page_3)
        self.labelReferenceImage_2.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.labelReferenceImage_2.setObjectName("labelReferenceImage_2")
        self.stackedWidgetSource.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidgetSource.addWidget(self.page_4)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(760, 190, 351, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.frame_4 = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.stackedWidgetCombined = QtGui.QStackedWidget(self.frame_4)
        self.stackedWidgetCombined.setGeometry(QtCore.QRect(10, 20, 321, 321))
        self.stackedWidgetCombined.setObjectName("stackedWidgetCombined")
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.labelReferenceImage_3 = QtGui.QLabel(self.page_5)
        self.labelReferenceImage_3.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.labelReferenceImage_3.setObjectName("labelReferenceImage_3")
        self.stackedWidgetCombined.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidgetCombined.addWidget(self.page_6)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.buttonStart = QtGui.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(30, 70, 90, 27))
        self.buttonStart.setObjectName("buttonStart")
        self.buttonStop = QtGui.QPushButton(self.centralwidget)
        self.buttonStop.setGeometry(QtCore.QRect(30, 110, 90, 27))
        self.buttonStop.setObjectName("buttonStop")
        self.buttonInitialize = QtGui.QPushButton(self.centralwidget)
        self.buttonInitialize.setGeometry(QtCore.QRect(30, 30, 90, 27))
        self.buttonInitialize.setObjectName("buttonInitialize")
        self.labelStatus = QtGui.QLabel(self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(200, 10, 251, 16))
        self.labelStatus.setObjectName("labelStatus")
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(140, 10, 59, 15))
        self.label_12.setObjectName("label_12")
        self.textLog = QtGui.QTextEdit(self.centralwidget)
        self.textLog.setGeometry(QtCore.QRect(380, 30, 731, 141))
        self.textLog.setObjectName("textLog")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 30, 216, 59))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.labelPaddleController = QtGui.QLabel(self.layoutWidget)
        self.labelPaddleController.setObjectName("labelPaddleController")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelPaddleController)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.labelStageController = QtGui.QLabel(self.layoutWidget)
        self.labelStageController.setObjectName("labelStageController")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelStageController)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.labelCameraController = QtGui.QLabel(self.layoutWidget)
        self.labelCameraController.setObjectName("labelCameraController")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.labelCameraController)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 100, 166, 59))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelSourcePaddle = QtGui.QLabel(self.layoutWidget1)
        self.labelSourcePaddle.setObjectName("labelSourcePaddle")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelSourcePaddle)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.labelReferencePaddle = QtGui.QLabel(self.layoutWidget1)
        self.labelReferencePaddle.setObjectName("labelReferencePaddle")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelReferencePaddle)
        self.label_14 = QtGui.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_14)
        self.labelStagePosition = QtGui.QLabel(self.layoutWidget1)
        self.labelStagePosition.setObjectName("labelStagePosition")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.labelStagePosition)
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidgetReference.setCurrentIndex(0)
        self.stackedWidgetSource.setCurrentIndex(0)
        self.stackedWidgetCombined.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReferenceImage.setText(QtGui.QApplication.translate("MainWindow", "Reference Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReferenceImage_2.setText(QtGui.QApplication.translate("MainWindow", "Source Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Combined", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReferenceImage_3.setText(QtGui.QApplication.translate("MainWindow", "Combined Image", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonInitialize.setText(QtGui.QApplication.translate("MainWindow", "Initialize", None, QtGui.QApplication.UnicodeUTF8))
        self.labelStatus.setText(QtGui.QApplication.translate("MainWindow", "Pre-initialization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Paddle Controller Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPaddleController.setText(QtGui.QApplication.translate("MainWindow", "Pre-init", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Stage controller status:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelStageController.setText(QtGui.QApplication.translate("MainWindow", "Pre-init", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Camera controlelr status:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCameraController.setText(QtGui.QApplication.translate("MainWindow", "Pre-init", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSourcePaddle.setText(QtGui.QApplication.translate("MainWindow", "Pre-init", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Reference Paddle:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReferencePaddle.setText(QtGui.QApplication.translate("MainWindow", "Pre-init", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Stage Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelStagePosition.setText(QtGui.QApplication.translate("MainWindow", "Pre-init", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Source Paddle:", None, QtGui.QApplication.UnicodeUTF8))

