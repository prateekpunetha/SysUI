#!/usr/bin/env python3

import tkinter as tk
import subprocess
import os

root = tk.Tk()
root.title("Add User")

if os.geteuid() != 0:
    print("Please run this script as root (with sudo).")
    exit(1)

# Create label and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

def add_user():
    username = username_entry.get()
    password = password_entry.get()

    try:
        # Use the '-S' option to read the password from stdin
        cmd = f'sudo adduser {username}'
        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=password)

        if process.returncode == 0:
            result_label.config(text="User added successfully")
        else:
            result_label.config(text=f"Error: {stderr}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create button to trigger user addition
add_button = tk.Button(root, text="Add User", command=add_user)
add_button.pack()

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
