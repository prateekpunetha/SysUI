#!/usr/bin/env python3

import customtkinter
import os
import platform
import shutil

kernel_version = platform.release()
usb_module_path = f"/lib/modules/{kernel_version}/kernel/drivers/usb/storage/usb-storage.ko"
backup_path = '.sysui/backup/'


if os.geteuid() != 0:
    print("Please run this script as root (with sudo).")
    exit(1)

def create_backup_path():
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
        status_label.configure(text=f"backup directory created ==> {backup_path}")

def disable_usb():
    create_backup_path()
    try:
        if os.path.exists(usb_module_path):
            shutil.move(usb_module_path, backup_path)
            status_label.configure(text="USB Disabled!")
        else:
            status_label.configure(text="USB is already disabled!")
    except Exception as e:
        status_label.configure(text=f"Error: {e}")

def enable_usb():
    try:
        if os.path.exists(backup_path):
            shutil.move(backup_path, usb_module_path)
            status_label.configure(text="USB enabled!")
        else:
            status_label.configure(text="USB is already enabled")
    except Exception as e:
        status_label.configure(text=f"Error: {e}")

# usual stuff
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create the main window
app = customtkinter.CTk()
app.title("USB Disable/Enable")

# Create buttons
enable_button = customtkinter.CTkButton(app, text="Enable USB", command=enable_usb)
enable_button.pack()

disable_button = customtkinter.CTkButton(app, text="Disable USB", command=disable_usb)
disable_button.pack()

# Status Label
status_label = customtkinter.CTkLabel(app, text="", width=40)
status_label.pack()

app.mainloop()