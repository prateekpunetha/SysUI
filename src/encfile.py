#!/usr/bin/env python3

import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton, filedialog
import subprocess

def enc_file():
    filename = filedialog.askopenfilename(initialdir="/home", title="Select File")
    if filename:
        encrypt_file(filename)

def dec_file():
    filename = filedialog.askopenfilename(initialdir="/home", title="Select File")
    if filename:
        decrypt_file(filename)

def encrypt_file(filename):
    cmd = ["gpg", "-c", filename]

    try:
        subprocess.run(cmd,check=True)
        print("File encrypted!")
    except subprocess.CalledProcessError as e:
        print("Error",e)

def decrypt_file(filename):
    cmd = ["gpg", "-d", filename]

    try:
        subprocess.run(cmd,check=True)
        print("File Decrypted!")
    except subprocess.CalledProcessError as e:
        print("Error",e)

# Theme
customtkinter.set_default_color_theme("material.json")

# Create main window
app = customtkinter.CTk()
app.title("Encrypt")
app.geometry("400x300")

file = CTkButton(app, text="encrypt file", command=enc_file)
file.pack(pady=10)

file = CTkButton(app, text="Decrypt file", command=dec_file)
file.pack(pady=10)


# Start the GUI main loop
app.mainloop()
