from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.ui_btn import Ui_MainWindow
from db.Users import insert_User,select_all_Users,delete_User
import os

class ListUserWindow(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.AddUser_btn.clicked.connect(self.Add_User)
        self.table_config()
        # self.populate_table(select_all_Users())
        # self.populate_combobox()
        
        
    def add_new_user_row(self,data):
        qty_rows=self.listUsersTable.rowCount()
        index_row=qty_rows
        qty_rows+=1
        self.listUsersTable.setRowCount(qty_rows)
        for (index_cell,cell) in enumerate(data):
            self.listUsersTable.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))
        self.records_qty()
    def Add_User(self):
        from controllers.AddUser import NewUserWindow
        window = NewUserWindow(self)
        window.show()
        
    def table_config(self):
        column_headers = ("First name", "Last name", "Email", "Address")
        self.listUsersTable.setColumnCount(len(column_headers))
        self.listUsersTable.setHorizontalHeaderLabels(column_headers)

        self.listUsersTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    def records_qty(self):
        qty_rows = str(self.listUsersTable.rowCount())
        self.booksQtyLabel.setText(qty_rows)
        
    def add_new_user_row(self, data):
        qty_rows=self.listUsersTable.rowCount()
        index_row=qty_rows
        qty_rows+=1
        self.listUsersTable.setRowCount(qty_rows)
        for (index_cell,cell) in enumerate(data):
            self.listUsersTable.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))
        self.records_qty()