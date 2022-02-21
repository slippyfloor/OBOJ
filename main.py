print("PICK AN OPTION")
print("[1] Decrypt an OBOJ message")
print("[2] Encrypt an english message")

selection = input()

if selection == "1":
    print("Sending you to the Decryption software")
    exec(open("decrypt.py").read())

elif selection == "2":
    print("Sending you to the Encryption software")
    exec(open("encrypt.py").read())

else:
    print("404 PAGE NOT FOUND")