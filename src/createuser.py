#!/usr/bin/env python3

import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton
import subprocess

def add_user():
    username = username_entry.get()
    password = password_entry.get()

    try:
        # Use the '-S' option to read the password from stdin
        cmd = f'sudo adduser {username}'
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=password)

        if process.returncode == 0:
            result_label.configure(text="User added successfully", fg_color="#A3BE8C")
        else:
            result_label.configure(text=f"Error: {stderr}", fg_color="#FF4151")
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}", fg_color="#FF4151")

# Theme
customtkinter.set_default_color_theme("material.json")

# Create main window
app = customtkinter.CTk()
app.title("Add User")
app.geometry("400x300")

# Create label and entry fields for username and password
username_label = CTkLabel(app, text="Username")
username_label.pack(pady=(20, 0))  # Add padding at the top

username_entry = CTkEntry(app)
username_entry.pack(pady=(0, 10))  # Add padding at the bottom

password_label = CTkLabel(app, text="Password")
password_label.pack()

password_entry = CTkEntry(app, show="*")
password_entry.pack(pady=(0, 20))  # Add padding at the bottom

# Create button to trigger user addition
add_button = CTkButton(app, text="Add User", command=add_user)
add_button.pack(pady=(0, 20))  # Add padding at the bottom

# Create label to display result
result_label = CTkLabel(app, text="")
result_label.pack()

# Start the GUI main loop
app.mainloop()
