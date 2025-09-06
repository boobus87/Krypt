from cryptography.fernet import Fernet
import pandas as pd

class CryptoEngine:
	def __init__(self, gui):
		self.gui = gui
		

	# Generate and save a key (do this once; reuse the key for encryption/decryption)
	def generate_key(self):
		key = Fernet.generate_key()
		with open("data/secret.key", "wb") as key_file:
			key_file.write(key)
			print("Encryption key saved")
			return key

	# Load the key from the file
	def load_key(self):
		with open("data/secret.key", "rb") as saved_key:
			skey = saved_key.read()
			print("Encryption key loaded")
			return skey

	# Encrypt and save data to secrets.csv
	def encrypt_and_save(self):
		
		key = self.gui.key
		fernet = Fernet(key)
		
		with open("data/secrets.csv", "rb") as f:
			secrets = f.read()
			
		try:
			self.decrypt_secrets()
		except:
			pass
			
		secret_data = pd.read_csv("data/secrets.csv")
		
		data = {
    	'Website': [self.gui.site_field.displayText()],
    	'Username': [self.gui.username_field.displayText()],
    	'Password': [self.gui.password_display.text()]
		}
		
		df = pd.DataFrame(data)
		# vault_df = pd.DataFrame(secrets)
		secret_data = pd.concat([secret_data, df], ignore_index=False)
		
		secret_data.to_csv('data/secrets.csv', index=False)
		
		with open('data/secrets.csv', 'rb') as out:
			original = out.read()
		self.gui.vault_window.update_data()
		# Encrypt the file content
		encrypted = fernet.encrypt(original)

		# Overwrite the original file with the encrypted data
		with open('data/secrets.csv', 'wb') as f:
			f.write(encrypted)
			
	def decrypt_secrets(self):
    	
		key = self.gui.key
		fernet = Fernet(key)
		
		# Read the encrypted data from the file
		with open('data/secrets.csv', 'rb') as f:
			encrypted = f.read()

		# Decrypt the encrypted data
		decrypted = fernet.decrypt(encrypted)

		# Write the decrypted data back to the file
		with open('data/secrets.csv', 'wb') as f:
			f.write(decrypted)
			
			
	def encrypt_secrets(self):
    	
		key = self.gui.key
		fernet = Fernet(key)
		
		# Read the encrypted data from the file
		with open('data/secrets.csv', 'rb') as f:
			decrypted = f.read()

		# Decrypt the encrypted data
		encrypted = fernet.encrypt(decrypted)

		# Write the decrypted data back to the file
		with open('data/secrets.csv', 'wb') as f:
			f.write(encrypted) 
				

