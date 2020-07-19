import hashlib

flag = 0

#get an md5 hash
md5_hash = input("Enter md5 hash: ")

#get a filename
wordlist = input("Enter file name: ")

#try to open the given filename
try:
	dictionary = open(wordlist, "r")
except:
	print("No file found")
	quit()

#for each word in the dictionary, we encode it and hash it
for word in dictionary:

	enc_word = word.encode('utf-8')
	digest = hashlib.md5(enc_word.strip()).hexdigest()

	#if the hash of the word is the same as the given hash, then the word is the password
	if digest == md5_hash:
		print("Password found !")
		print("Password is " + word)
		flag = 1
		break

if flag == 0:
	print("Password/passphrase is not in the list")
