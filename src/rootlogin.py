#!/usr/bin/env python3

import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton
import subprocess

config_path = '/etc/ssh/sshd_config'

def add_permit_root_login():
    root_login_line = 'PermitRootLogin no'
    with open(config_path, 'r') as file:
        file_content = file.read()
        if 'PermitRootLogin yes' not in file_content and 'PermitRootLogin no' not in file_content:
            with open(config_path, 'a') as updated_file:
                updated_file.write('\n' + root_login_line)
            status_label.configure(text=f'Configuration added successfully', fg_color="#A3BE8C")
            reload_ssh()

def enable_root_login():
    with open(config_path, 'r') as file:
        content = file.read()

    if 'PermitRootLogin yes' in content:
        status_label.configure(text=f"Root Login is already enabled", fg_color="#A3BE8C")
    elif 'PermitRootLogin no' in content:
        updated_content = content.replace('PermitRootLogin no', 'PermitRootLogin yes')
        with open(config_path, 'w') as updated_file:
            updated_file.write(updated_content)
            status_label.configure(text=f'RootLogin Enabled', fg_color="#A3BE8C")
            reload_ssh()
    else:
        status_label.configure(text=f"PermitRootLogin configuration not found, click on add configuration!", fg_color="#ff4151")


def disable_root_login():
    with open(config_path, 'r') as file:
        content = file.read()

    if 'PermitRootLogin no' in content:
        status_label.configure(text=f"Root Login is already disabled", fg_color="#A3BE8C")
    elif 'PermitRootLogin yes' in content:
        updated_content = content.replace('PermitRootLogin yes', 'PermitRootLogin no')
        with open(config_path, 'w') as updated_file:
            updated_file.write(updated_content)
            status_label.configure(text=f'RootLogin Disabled', fg_color="#A3BE8C")
            reload_ssh()
    else:
        status_label.configure(text=f"PermitRootLogin configuration not found, click on add configuration!", fg_color="#ff4151")

def reload_ssh():
    try:
        subprocess.run(["systemctl", "reload", "sshd"], check=True)
    except subprocess.CalledProcessError:
        status_label.configure(text="Failed to reload SSH. Manually restart ssh service", fg_color="#ff4151")

# Theme
customtkinter.set_default_color_theme("material.json")

# Create main window

app = customtkinter.CTk()
app.title("Enable/Disable RootLogin")
app.geometry("400x300")

# Create buttons

enable_button = CTkButton(app, text="Enable RootLogin", command=enable_root_login)
enable_button.pack()

disable_button = CTkButton(app, text="Disable RootLogin", command=disable_root_login)
disable_button.pack()

add_button = CTkButton(app, text="Add Configuration", command=add_permit_root_login)
add_button.pack()

# Status Label
status_label = CTkLabel(app, text="", width=40)
status_label.pack()

app.mainloop()
