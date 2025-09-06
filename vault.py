from random import randint
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from PyQt5.QtGui import QIcon

from pandas_model import *


class Vault(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self, master):
        super().__init__()
        self.setWindowTitle("Krypt - Password Vault")
        self.setGeometry(200, 100, 400, 150)
        self.setWindowIcon(QIcon('icon.png'))
        
        layout = QVBoxLayout()
        self.table_view = QtWidgets.QTableView(self)
        df = pd.read_csv('data/secrets.csv')  # Replace with your CSV file
        model = PandasModel(df)
        self.table_view.setModel(model)
        
        layout.addWidget(self.table_view)
        self.setLayout(layout)
        
        self.master = master
        
    def update_data(self):
    	df = pd.read_csv('data/secrets.csv')
    	model = PandasModel(df)
    	self.table_view.setModel(model)

