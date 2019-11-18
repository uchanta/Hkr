# Ethical Hacking using Python | Password Cracker Using Python | Edureka
# https://www.youtube.com/watch?v=CV_mMAYzTxw
#
# OBJECTIVE: Used of de HASHLIB-md5, convert word an lokingford in a file.
#

import hashlib

flag = 0

pass_hash = input("Enter md5 hash (default = 0d7270270aae2c0a0b46cfe7b81980d0 = phosphate): ")
if pass_hash == "":
	pass_hash = "0d7270270aae2c0a0b46cfe7b81980d0"

wordlist = input("File name (defaut = c:\Hkr\ypcup\wordlist.txt): ")
if wordlist == "":
	wordlist = "c:\Hkr\ypcup\wordlist.txt"

# TRY se utiliza para el manejo de errores, si la condicion no se cumple (no es manejada por el codigo)
# se ejecuta la excepcion.
try:
	pass_file = open (wordlist, "r")
except:
	print(" No file found")
	quit()

for word in pass_file:

	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	if digest == pass_hash:
		print('\n' + "Password found: " + '\n')
		print("Password is: "+ word)
		flag = 1
		break

if flag == 0:
	print("Password is not in the list: ")