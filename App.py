
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer

from Com import Com
from VideoEditor import VideoEditor
from LabelEditor import LabelEditor

if __name__ == "__main__":

    com = Com()
    com.main = QtWidgets.QApplication(sys.argv)
    com.videoEditor = QtWidgets.QMainWindow()
    com.labelEditor = QtWidgets.QWidget()
    
    timer = QTimer()
    timer.setInterval(200)
    timer.timeout.connect(com.update)
    timer.start()

    ve = VideoEditor()
    le = LabelEditor()
    ve.setupUi(com)
    le.setupUi(com)

    com.videoEditor.show()

    sys.exit(com.main.exec_())
