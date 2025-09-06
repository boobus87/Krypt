import string
import random


class PlaintextGenerator:
	def __init__(self, gui):
		self.gui = gui
		self.length = 12
		
	def generate_password(self):
		self.length = self.gui.length_spin.value()		
		characters = string.ascii_letters + string.digits + string.punctuation
		password = ''.join(random.choice(characters) for _ in range(self.length))
		self.gui.password_display.setText(password)

        
