#!/usr/bin/env python3

import customtkinter
import subprocess
import os

if os.geteuid() != 0:
    print("Please run this script as root (with sudo).")
    exit(1)


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

# Usual stuff
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create main window
app = customtkinter.CTk()
app.title("Delete User")

# Create labels and entry fields for username
username_label = customtkinter.CTkLabel(app, text="Username")
username_label.pack()
username_entry = customtkinter.CTkEntry(app)
username_entry.pack()

# Create label to display the result
result_label = customtkinter.CTkLabel(app, text="")
result_label.pack()

# Create button to trigger user deletion
delete_button = customtkinter.CTkButton(app, text="Delete User", command=delete_user)
delete_button.pack()

# Start GUI main loop
app.mainloop()