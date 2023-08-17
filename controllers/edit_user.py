from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.ui_EDIT import Ui_EDIT_USER_DETAILS_2
from db.Users import select_User_by_id, update_User
import re
import os
import shutil
class EditUserWindow(QWidget, Ui_EDIT_USER_DETAILS_2):
    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.populate_inputs()
        # self.selectFileButton.clicked.connect(self.select_file)
        self.EDIT_BTN.clicked.connect(self.edit_User)
        
    
    def populate_inputs(self):
        data = select_User_by_id(self._id)
        
        
        self.firstName=self.firstName.setText(data[1])
        self.lastName = self.lastName.setText(data[2])
        self.Email = self.Email.setText(data[3])
        self.Address = self.Address.setText(data[4])
        
    def check_inputs(self):
        firstName = self.firstName.text()
        lastName = self.lastName.text()
        Email = self.Email.text()
        Address = self.Address.text()

        errors_count = 0
        
        if firstName == "":
            print("El campo titulo es obligatorio")
            errors_count += 1
        if lastName == "":
            print("El campo cateogria es obligatorio")
            errors_count +=1
        if Email == "":
            print("Debe seleccionar un libro")
            errors_count +=1
        
        if errors_count == 0:
            return True
        
        
    def edit_User(self):
        firstName = self.firstName.text()
        lastName = self.lastName.text()
        Email = self.Email.text()
        Address = self.Address.text()
        
        data = [firstName,lastName,Email,Address]
        if self.check_inputs():
            
            if update_User(self._id, data):
                
                self.close()