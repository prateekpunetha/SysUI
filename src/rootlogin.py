#!/usr/bin/env python3

import customtkinter
import os
import subprocess

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
            status_label.configure(text=f'Configuration added successfully')
            reload_ssh()

def enable_root_login():
    with open(config_path, 'r') as file:
        content = file.read()

    if 'PermitRootLogin yes' in content:
        status_label.configure(text=f"Root Login is already enabled")
    elif 'PermitRootLogin no' in content:
        updated_content = content.replace('PermitRootLogin no', 'PermitRootLogin yes')
        with open(config_path, 'w') as updated_file:
            updated_file.write(updated_content)
            status_label.configure(text=f'RootLogin Enabled')
            reload_ssh()
    else:
        status_label.configure(text=f"PermitRootLogin configuration not found, click on add configuration!")


def disable_root_login():
    with open(config_path, 'r') as file:
        content = file.read()

    if 'PermitRootLogin no' in content:
        status_label.configure(text=f"Root Login is already disabled")
    elif 'PermitRootLogin yes' in content:
        updated_content = content.replace('PermitRootLogin yes', 'PermitRootLogin no')
        with open(config_path, 'w') as updated_file:
            updated_file.write(updated_content)
            status_label.configure(text=f'RootLogin Disabled')
            reload_ssh()
    else:
        status_label.configure(text=f"PermitRootLogin configuration not found, click on add configuration!")

def reload_ssh():
    try:
        subprocess.run(["systemctl", "reload", "sshd"], check=True)
    except subprocess.CalledProcessError:
        status_label.configure(text="Failed to reload SSH. Manually restart ssh service")


# Usual stuff
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create main window

app = customtkinter.CTk()
app.title("Enable/Disable RootLogin")
app.geometry("400x300")

# Create buttons

enable_button = customtkinter.CTkButton(app, text="Enable RootLogin", command=enable_root_login)
enable_button.pack()

disable_button = customtkinter.CTkButton(app, text="Disable RootLogin", command=disable_root_login)
disable_button.pack()

add_button = customtkinter.CTkButton(app, text="Add Configuration", command=add_permit_root_login)
add_button.pack()

# Status Label
status_label = customtkinter.CTkLabel(app, text="", width=40)
status_label.pack()

app.mainloop()
