from random import randint
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QHeaderView
)

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

from pandas_model import *


class Vault(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self, master):
        super().__init__()
        self.setWindowTitle("Krypt - Password Vault")
        self.setGeometry(200, 100, 600, 150)
        self.setWindowIcon(QIcon('icon.png'))
        
        layout = QVBoxLayout()
        top_gfx = QLabel()
        pixmap = QPixmap('top_bar_gfx.png')
        top_gfx.setPixmap(pixmap)
        self.table_view = QtWidgets.QTableView(self)
        df = pd.read_csv('data/secrets.csv')
        model = PandasModel(df)
        self.table_view.setModel(model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.search_field = QLineEdit()
        self.search_field.setReadOnly(False)
        self.search_field.setPlaceholderText("Search")
        self.search_button_site = QPushButton("Search By Site")
        self.search_button_site.clicked.connect(self.lookup_site)
        
        self.search_button_user = QPushButton("Search By Username")
        self.search_button_user.clicked.connect(self.lookup_user)
        
        self.clear_button = QPushButton("Clear Filter")
        self.clear_button.clicked.connect(self.update_data)
        
        layout.addWidget(self.search_field)
        layout.addWidget(self.search_button_site)
        layout.addWidget(self.search_button_user)
        layout.addWidget(self.clear_button)
        layout.addWidget(top_gfx)
        layout.addWidget(self.table_view)
        self.setLayout(layout)
        
        self.master = master
        
    def update_data(self):
    	df = pd.read_csv('data/secrets.csv')
    	model = PandasModel(df)
    	self.table_view.setModel(model)
    	
    def lookup_site(self):
    	df = pd.read_csv('data/secrets.csv')
    	filtered_df = df[df['Website'] == self.search_field.displayText()]
    	model = PandasModel(filtered_df)
    	self.table_view.setModel(model)
    	
    def lookup_user(self):
    	df = pd.read_csv('data/secrets.csv')
    	filtered_df = df[df['Username'] == self.search_field.displayText()]
    	model = PandasModel(filtered_df)
    	self.table_view.setModel(model)
    	
    def delete_entry(self):
    	pass
