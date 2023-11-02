#!/usr/bin/env python3

import tkinter as tk
import subprocess
import os

root = tk.Tk()
root.title("Delete User")

if os.geteuid() != 0:
    print("Please run this script as root (with sudo).")
    exit(1)

# Create labels and entry fields for username
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

def delete_user():
    username = username_entry.get()

    try:
        cmd = f'sudo userdel -r {username}'
        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()

        if process.returncode == 0:
            result_label.config(text=f"User {username} deleted successfully")
        else:
            result_label.config(text=f"Error: {process.stderr.read()}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create button to trigger user deletion
delete_button = tk.Button(root, text="Delete User", command=delete_user)
delete_button.pack()

# Create label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start GUI main loop
root.mainloop()
