import sys
import string
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QSpinBox, QMainWindow
)
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QIcon

from generate import PlaintextGenerator
from encrypt import CryptoEngine
from vault import Vault

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Krypt")
        self.setGeometry(100, 100, 400, 150)
        self.setWindowIcon(QIcon('icon.png'))
        self.crypto_engine = CryptoEngine(self)
        
        try:
        	self.key = self.crypto_engine.load_key()
        except:
        	self.key = self.crypto_engine.generate_key()
        	
        self.vault_window = Vault(self)

        # Label and spinbox for password length
        length_label = QLabel("Password Length:")
        self.length_spin = QSpinBox()
        self.length_spin.setRange(4, 64)  # Min 4, max 64 characters
        self.length_spin.setValue(12)

        length_layout = QHBoxLayout()
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_spin)

        # Display for generated password
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setPlaceholderText("Your generated password will appear here")
        self.plain_generator = PlaintextGenerator(self)

        # Generate button
        generate_btn = QPushButton("Generate Password")
        generate_btn.clicked.connect(self.plain_generator.generate_password)
        
        # Site and username fields
        self.site_field = QLineEdit()
        self.site_field.setReadOnly(False)
        self.site_field.setPlaceholderText("Website")
        self.username_field = QLineEdit()
        self.username_field.setReadOnly(False)
        self.username_field.setPlaceholderText("Username")
        
        # Save encrypted button
        save_button = QPushButton("Save Encrypted")
        save_button.clicked.connect(self.crypto_engine.encrypt_and_save)
        
        # Vault button
        vault_button = QPushButton("Password Vault")
        vault_button.clicked.connect(self.toggle_vault)

        # Layout setup
        main_layout = QVBoxLayout()
        main_layout.addLayout(length_layout)
        main_layout.addWidget(generate_btn)
        main_layout.addWidget(self.password_display)
        main_layout.addWidget(self.site_field)
        main_layout.addWidget(self.username_field)
        main_layout.addWidget(save_button)
        main_layout.addWidget(vault_button)
        

        self.setLayout(main_layout)
    
    def toggle_vault(self, checked):
        if self.vault_window.isVisible():
            self.vault_window.hide()
            self.vault_window.update_data()
            self.crypto_engine.encrypt_secrets()

        else:
        	try:
        		self.vault_window.show()
        		self.crypto_engine.decrypt_secrets()
        		self.vault_window.update_data()
        	except:
        		pass

    	
