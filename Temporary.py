#def cryptomain(m, dt, alg, keysize, blocksize, kvalue, ivect, iptext):
from Crypto.Cipher import AES, Blowfish, DES3
from Crypto.Random import get_random_bytes
from utility import *
import Simple
import Advance 


def cryptomain(ipvalues):
	#main.py file content
	operation = ipvalues["opt"]			#
	encryption_mode = ipvalues["m"]			#
	type_of_data = ipvalues["dt"]			#

	algorithms = {"1": AES, "3": Blowfish, "2": DES3, "4": "Twofish"}
	choice = ipvalues["alg"]			#
	algorithm = algorithms[choice]
	
	key_size = int(ipvalues["keysize"])			#
	block_size = int(ipvalues["blocksize"])		#


	# Ensure key is always initialized
	key = None
	iv = None
	ciphertext= None
	ciphertext_hex= None


	#Validate python file content
	if encryption_mode == "1" and operation=="1":
		key,iv= get_random_bytes(key_size), get_random_bytes(block_size)
	elif (encryption_mode == "2" and operation=="1")or (encryption_mode == "2" and operation=="2"):
		key = bytes.fromhex(ipvalues["kvalue"].strip())	#
		iv = bytes.fromhex(ipvalues["ivect"].strip())		#

		if len(key) != key_size or len(iv) != block_size:
			return 401		#raise ValueError("Error: Incorrect key or IV length.")
				



	elif encryption_mode == "1" and operation=="2":
		key = bytes.fromhex(ipvalues["kvalue"].strip())	#
		iv = 0
		if len(key) != key_size :
			return 402		#raise ValueError("Error: Incorrect key length.")
			

	if key is None:
        	return 403  # Return error if key was never assigned



#result={"encryptedMessage": str(ciphertext), "encryptedHex":str(ciphertext.hex()), "keyValue": str(key.hex()), "ivValue": str(iv.hex())



	result = {}
	#Simple mode
	if encryption_mode=="1":
		if type_of_data == "1":
		
			if operation == "1":
				result.update({"keyValue": str(key.hex())})	#On 24/03/2025 at 12:00am, we removed the ivValue return from this code
				plaintext = ipvalues["iptext"]		#
				ciphertext =Simple.encrypt_text(algorithm, key, block_size, plaintext, iv)
				#print(f"Encrypted text (hex): {ciphertext.hex()}")
				#print(f"Key (hex): {key.hex()}")
				result.update({"encryptedMessage": str(ciphertext.hex()),"keyValue": str(key.hex()) })
				
			else:
				ciphertext_hex = ipvalues["iptext"]		#
				ciphertext = bytes.fromhex(ciphertext_hex)
				iv = ciphertext[:block_size]
				
				decrypted_text = decrypt_twofish(ciphertext[block_size:], key, iv).decode() if algorithm == "Twofish" else Simple.decrypt_text(algorithm, key, block_size, ciphertext,iv)
				#print(f"Decrypted text: {decrypted_text}")
				result.update({"decryptedMessage": str(decrypted_text)})
		else:
			if operation == "1":
				input_file = ipvalues["fname"]		#
				hex_file = "hex_" + input_file + ".txt" # Store hex file
				encrypted_file = "encrypted_crpty_" + input_file    # Encrypted file in given format
				last=input_file.rfind('.')
				encrypted_hex_file = "encrypted_hex_" + input_file[:last]+ ".txt" # Encrypted file in hex

				convert_to_text(input_file, hex_file)

				Simple.encrypt_file(algorithm, key,iv, block_size, hex_file, encrypted_file, encrypted_hex_file)
				#print(f"Encrypted file stored in: {encrypted_file}")
				#print(f"Encrypted hex stored in: {encrypted_hex_file}")
				#print(f"Key (hex): {key.hex()}")
				result.update({"encryptedFile": encrypted_file,"encryptedHexFile": encrypted_hex_file, "keyValue": str(key.hex())})
			else:
				input_file = ipvalues["fname"]		#
				decrypted_file = Simple.decrypt_simple(algorithm, key, block_size, input_file)
				result.update({"decryptedFile": decrypted_file})
	
	#Advanced Mode
	elif encryption_mode=="2":
		if type_of_data == "1":
        
			if operation == "1":
				plaintext = ipvalues["iptext"]		#
				ciphertext = encrypt_twofish(plaintext.encode(), key, iv) if algorithm == "Twofish" else Advance.encrypt_text(algorithm, key, block_size, plaintext, iv)
				#print(f"Encrypted text (hex): {ciphertext.hex()}")
				#print(f"Key (hex): {key.hex()}")
				#print(f"IV (hex): {iv.hex()}")
				result.update({"encryptedMessage": str(ciphertext.hex()),"keyValue": str(key.hex()), "ivValue": str(iv.hex())})
			else:
				ciphertext_hex = ipvalues["iptext"]		#
				ciphertext = bytes.fromhex(ciphertext_hex)
				decrypted_text = decrypt_twofish(ciphertext, key, iv).decode() if algorithm == "Twofish" else Advance.decrypt_text(algorithm, key, block_size, ciphertext,iv)
				#print(f"Decrypted text: {decrypted_text}")
				result.update({"decryptedMessage": str(decrypted_text)})
		else:
			if operation == "1":
				input_file = ipvalues["fname"]		#
				hex_file = "hex_" + input_file + ".txt" # Store hex file
				encrypted_file = "encrypted_crpty_" + input_file    # Encrypted file in given format
				last=input_file.rfind('.')
				encrypted_hex_file = "encrypted_hex_" + input_file[:last]+ ".txt" # Encrypted file in hex
				convert_to_text(input_file, hex_file)

				Advance.encrypt_file(algorithm, key,iv, block_size, hex_file, encrypted_file, encrypted_hex_file)
				#print(f"Encrypted file stored in: {encrypted_file}")
				#print(f"Encrypted hex stored in: {encrypted_hex_file}")
				#print(f"Key (hex): {key.hex()}")
				#print(f"IV (hex): {iv.hex()}")
				result.update({"encryptedFile": encrypted_file,"encryptedHexFile": encrypted_hex_file, "keyValue": str(key.hex()), "ivValue": str(iv.hex()) })
				
			else:
				input_file = ipvalues["fname"]		#
				decrypted_file = Advance.decrypt_advanced(algorithm, key, iv, block_size, input_file)
				result.update({"decryptedFile": decrypted_file})
	#else:
		#return

	#result={"encryptedMessage": str(ciphertext), "encryptedHex":str(ciphertext.hex()), "keyValue": str(key.hex()), "ivValue": str(iv.hex())}

	return result






















