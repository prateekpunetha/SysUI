#!/usr/bin/env python3

import customtkinter
import subprocess
import os

if os.geteuid() != 0:
    print("Please run this script as root (with sudo).")
    exit(1)

def add_user():
    username = username_entry.get()
    password = password_entry.get()

    try:
        # Use the '-S' option to read the password from stdin
        cmd = f'sudo adduser {username}'
        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=password)

        if process.returncode == 0:
            result_label.configure(text="User added successfully")
        else:
            result_label.configure(text=f"Error: {stderr}")
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}")

# Usual stuff
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create main window
app = customtkinter.CTk()
app.title("Add User")

# Create label and entry fields for username and password
username_label = customtkinter.CTkLabel(app, text="Username")
username_label.pack()
username_entry = customtkinter.CTkEntry(app)
username_entry.pack()

password_label = customtkinter.CTkLabel(app, text="Password")
password_label.pack()
password_entry =customtkinter.CTkEntry(app, show="*")
password_entry.pack()

# Create button to trigger user addition
add_button = customtkinter.CTkButton(app, text="Add User", command=add_user)
add_button.pack()

# Create label to display result
result_label = customtkinter.CTkLabel(app, text="")
result_label.pack()

# Start the GUI main loop
app.mainloop()
