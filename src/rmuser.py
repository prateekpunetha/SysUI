#!/usr/bin/env python3

import customtkinter
from customtkinter import CTkEntry, CTkLabel, CTkButton
import subprocess

def delete_user():
    username = username_entry.get()

    try:
        cmd = f'sudo userdel -r {username}'
        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()

        if process.returncode == 0:
            result_label.configure(text=f"User {username} deleted successfully")
        else:
            result_label.configure(text=f"Error: {stderr}")
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}")

# Theme
customtkinter.set_default_color_theme("material.json")

# Create main window
app = customtkinter.CTk()
app.title("Delete User")
app.geometry("400x300")

# Create labels and entry fields for username
username_label = CTkLabel(app, text="Username")
username_label.pack(pady=(20,10))

username_entry = CTkEntry(app)
username_entry.pack(pady=(0,10))

# Create label to display the result
result_label = CTkLabel(app, text="")
result_label.pack()

# Create button to trigger user deletion
delete_button = CTkButton(app, text="Delete User", command=delete_user)
delete_button.pack(pady=(2,20))

# Start GUI main loop
app.mainloop()
