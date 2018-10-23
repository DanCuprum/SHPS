# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\VideoEdit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VideoEdit(object):
    def setupUi(self, VideoEdit):
        VideoEdit.setObjectName("VideoEdit")
        VideoEdit.resize(856, 762)
        VideoEdit.setMinimumSize(QtCore.QSize(856, 762))
        VideoEdit.setMaximumSize(QtCore.QSize(856, 762))
        self.centralwidget = QtWidgets.QWidget(VideoEdit)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 680, 834, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboLabName = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboLabName.sizePolicy().hasHeightForWidth())
        self.comboLabName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboLabName.setFont(font)
        self.comboLabName.setObjectName("comboLabName")
        self.comboLabName.addItem("")
        self.comboLabName.addItem("")
        self.horizontalLayout.addWidget(self.comboLabName)
        self.timeLabTime = QtWidgets.QTimeEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.timeLabTime.setFont(font)
        self.timeLabTime.setObjectName("timeLabTime")
        self.horizontalLayout.addWidget(self.timeLabTime)
        self.buttonLabInsert = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonLabInsert.setFont(font)
        self.buttonLabInsert.setObjectName("buttonLabInsert")
        self.horizontalLayout.addWidget(self.buttonLabInsert)
        self.buttonLabDelete = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonLabDelete.setFont(font)
        self.buttonLabDelete.setObjectName("buttonLabDelete")
        self.horizontalLayout.addWidget(self.buttonLabDelete)
        self.buttonLabEdit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonLabEdit.setFont(font)
        self.buttonLabEdit.setObjectName("buttonLabEdit")
        self.horizontalLayout.addWidget(self.buttonLabEdit)
        self.LabelName = QtWidgets.QLabel(self.centralwidget)
        self.LabelName.setGeometry(QtCore.QRect(10, 650, 834, 19))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.LabelName.setFont(font)
        self.LabelName.setObjectName("LabelName")
        self.labPlotName = QtWidgets.QLabel(self.centralwidget)
        self.labPlotName.setGeometry(QtCore.QRect(10, 440, 834, 19))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.labPlotName.setFont(font)
        self.labPlotName.setObjectName("labPlotName")
        self.textPlot = QtWidgets.QTextEdit(self.centralwidget)
        self.textPlot.setGeometry(QtCore.QRect(10, 467, 834, 171))
        self.textPlot.setObjectName("textPlot")
        self.textVideo = QtWidgets.QTextEdit(self.centralwidget)
        self.textVideo.setGeometry(QtCore.QRect(10, 40, 471, 391))
        self.textVideo.setObjectName("textVideo")
        self.labVideoName = QtWidgets.QLabel(self.centralwidget)
        self.labVideoName.setGeometry(QtCore.QRect(10, 10, 834, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.labVideoName.setFont(font)
        self.labVideoName.setObjectName("labVideoName")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(490, 40, 351, 301))
        self.widget.setObjectName("widget")
        VideoEdit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VideoEdit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        VideoEdit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VideoEdit)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        VideoEdit.setStatusBar(self.statusbar)
        self.action_ffnen = QtWidgets.QAction(VideoEdit)
        self.action_ffnen.setObjectName("action_ffnen")
        self.actionSpeichern = QtWidgets.QAction(VideoEdit)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionSpeichern_unter = QtWidgets.QAction(VideoEdit)
        self.actionSpeichern_unter.setObjectName("actionSpeichern_unter")
        self.menuDatei.addAction(self.action_ffnen)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menuDatei.addAction(self.actionSpeichern_unter)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(VideoEdit)
        QtCore.QMetaObject.connectSlotsByName(VideoEdit)

    def retranslateUi(self, VideoEdit):
        _translate = QtCore.QCoreApplication.translate
        VideoEdit.setWindowTitle(_translate("VideoEdit", "Video Editor"))
        self.comboLabName.setItemText(0, _translate("VideoEdit", "Hindernis 1 Auffahrt"))
        self.comboLabName.setItemText(1, _translate("VideoEdit", "Hindernis 1 Abfahrt"))
        self.timeLabTime.setDisplayFormat(_translate("VideoEdit", "HH:mm:ss"))
        self.buttonLabInsert.setText(_translate("VideoEdit", "Hinzufügen"))
        self.buttonLabDelete.setText(_translate("VideoEdit", "Löschen"))
        self.buttonLabEdit.setText(_translate("VideoEdit", "Bearbeiten..."))
        self.LabelName.setText(_translate("VideoEdit", "Label <Dateiname>"))
        self.labPlotName.setText(_translate("VideoEdit", "Plot <Dateiname>"))
        self.textPlot.setHtml(_translate("VideoEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plot Graph</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textVideo.setHtml(_translate("VideoEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Video View</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labVideoName.setText(_translate("VideoEdit", "Video <Dateiname>"))
        self.menuDatei.setTitle(_translate("VideoEdit", "Datei"))
        self.action_ffnen.setText(_translate("VideoEdit", "Öffnen..."))
        self.actionSpeichern.setText(_translate("VideoEdit", "Speichern"))
        self.actionSpeichern_unter.setText(_translate("VideoEdit", "Speichern unter.."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VideoEdit = QtWidgets.QMainWindow()
    ui = Ui_VideoEdit()
    ui.setupUi(VideoEdit)
    VideoEdit.show()
    sys.exit(app.exec_())

