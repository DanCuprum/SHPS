
import json
from ui import LabelEdit as LE

from PyQt5.QtWidgets import QMessageBox

class LabelEditor(LE.Ui_LabelEdit):

    com = None
    labs1 = []
    labs2 = []
    added = 0

    def setupUi(self, com):

        LE.Ui_LabelEdit.setupUi(self, com.labelEditor)
        
        self.com = com
        self.btnOk.clicked.connect(self.buttonOkClick)
        self.btnLabImport.clicked.connect(self.buttonLabImportClick)
        # self.buttonLabInsert.clicked.connect(self.onButtonInsertClick)
        self.labs1 = self.loadLabels(self.com.labelFile1)

        self.updateLabels(self.labs1)

    def buttonLabImportClick(self):

        print('Clicked button "Import"')
        self.labs2 = self.loadLabels(self.com.labelFile2)

        self.addNewLabels()          
        self.updateLabels(self.labs1)
        self.showDialogOk("Information", str(self.added) + " neue Labels wurden hinzugefuegt")
        
    def buttonOkClick(self):

        print('Clicked button "Ok"')
        self.com.labelEditor.hide()
        
    def showDialogOk(self, title, text):
        
       msg = QMessageBox()    
       msg.setIcon(QMessageBox.Information)
       msg.setWindowTitle(title)    
       msg.setText(text)
       msg.setStandardButtons(QMessageBox.Ok)
       msg.exec_()
 
    def updateLabels(self, labs):
        
        self.listLabNames.clear()
        for l in labs:
            self.listLabNames.addItem(l['LabelName'])

    def loadLabels(self, fileName):
        
        file = open(fileName)
        labs = json.load(file);
        return labs

    def addNewLabels(self):
        
        self.added = 0
        for l in self.labs2:
            if not self.labelExists(l['LabelName'], self.labs1):
                self.added += 1
                self.labs1.append(l)

    def labelExists(self, name, labs):
        
        for l in labs:
            if name == l['LabelName']: return True
        return False
