#!/usr/bin/env python3

import tkinter as tk
import os

if os.getuid() != 0:
    print("Please run this script as root (with sudo).")
    exit(1)

config_path = '/etc/ssh/sshd_config'

def add_permit_root_login():
    root_login_line = 'PermitRootLogin no'
    with open(config_path, 'r') as file:
        file_content = file.read()
        if 'PermitRootLogin yes' not in file_content and 'PermitRootLogin no' not in file_content:
            with open(config_path, 'a') as updated_file:
                updated_file.write('\n' + root_login_line)

def enable_root_login():
    with open(config_path, 'r') as file:
        content = file.read()

    if 'PermitRootLogin yes' in content:
        status_label.config(text=f"Root Login is already enabled")
    elif 'PermitRootLogin no' in content:
        updated_content = content.replace('PermitRootLogin no', 'PermitRootLogin yes')
        with open(config_path, 'w') as updated_file:
            updated_file.write(updated_content)
            status_label.config(text=f'RootLogin Enabled')
    else:
        status_label.config(text=f"PermitRootLogin configuration not found, click on add configuration!")


def disable_root_login():
    with open(config_path, 'r') as file:
        content = file.read()

    if 'PermitRootLogin no' in content:
        status_label.config(text=f"Root Login is already disabled")
    elif 'PermitRootLogin yes' in content:
        updated_content = content.replace('PermitRootLogin yes', 'PermitRootLogin no')
        with open(config_path, 'w') as updated_file:
            updated_file.write(updated_content)
            status_label.config(text=f'RootLogin disabled')
    else:
        status_label.config(text=f"PermitRootLogin configuration not found, click on add configuration!")


# Create the main window

root = tk.Tk()
root.title("Enable/Disable RootLogin")

#Create buttons

enable_button = tk.Button(root, text="Enable RootLogin", command=enable_root_login)
enable_button.pack()

disable_button = tk.Button(root, text="Disable RootLogin", command=disable_root_login)
disable_button.pack()

add_button = tk.Button(root, text="Add Configuration", command=add_permit_root_login)
add_button.pack()

# Status Label
status_label = tk.Label(root, text="", width=40)
status_label.pack()

root.mainloop()
