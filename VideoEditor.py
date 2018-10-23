
import json
from ui import VideoEdit as VE


class VideoEditor(VE.Ui_VideoEdit):
    
    com = None
           
    def setupUi(self, com):
        
        VE.Ui_VideoEdit.setupUi(self, com.videoEditor)
        
        self.com = com
        self.buttonLabInsert.clicked.connect(self.button_insert_click)
        self.buttonLabDelete.clicked.connect(self.button_delete_click)
        self.buttonLabEdit.clicked.connect(self.buttonEditClick)
        self.loadComboBox()

    @staticmethod
    def button_insert_click():
        print('Clicked button "Insert"')

    @staticmethod
    def button_delete_click():
        print('Clicked button "Delete"')

    def buttonEditClick(self):
        print('Clicked button "Edit"')
        self.com.labelEditor.show()

    def loadComboBox(self):
        self.comboLabName.clear()
        file = open(self.com.labelFile1)
        data = json.load(file)
        for d in data:
            self.comboLabName.addItem(d['LabelName'])
