from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.ui_Adduser import Ui_Form
from db.Users import delete_User,select_all_Users,insert_User
import shutil
import os
class NewUserWindow(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.Done_btn.clicked.connect(self.add_User)
    def check_inputs(self):
        firstName=self.firstName.text()
        lastName = self.lastName.text()
        Email = self.Email.value()
        Address = self.Address.text()
        errors_count = 0
        
        if firstName == "":
            print("Invalid first name")
            errors_count += 1
        if lastName == "":
            print("Invalid last name")
            errors_count +=1
        if Email == 0:
            print("Invalid eamil name")
            errors_count +=1
        if Address == "":
            print("Invalid Address name")
            errors_count +=1
        
        return (errors_count == 0)
    
    def add_User(self):
        firstName=self.firstName.text()
        lastName = self.lastName.text()
        Email = self.Email.value()
        Address = self.Address.text()

        if self.check_inputs():
            # new_path = shutil.copy(path, "book_files")
            data = (firstName, lastName, Email, Address)
            if insert_User(data):
                self.clean_inputs()
                # self.parent.refresh_table_from_child_window()
            else:
                # self.filePathLineEdit.setText(new_path)
                self.undo()

    def clean_inputs(self):
        
        self.firstName.clear()
        self.lastName.clear()
        self.Email.clear()
        self.Address.clear()
        