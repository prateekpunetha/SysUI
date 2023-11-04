#!/usr/bin/env python3

import tkinter as tk
import os
import platform
import shutil

kernel_version = platform.release()
usb_module_path = f"/lib/modules/{kernel_version}/kernel/drivers/usb/storage/usb-storage.ko"
backup_path = '.sysui/backup/'

def create_backup_path():
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
        status_label.config(text=f"backup directory created ==> {backup_path}")

def disable_usb():
    create_backup_path()
    try:
        if os.path.exists(usb_module_path):
            shutil.move(usb_module_path, backup_path)
            status_label.config(text="USB Disabled!")
        else:
            status_label.config(text="USB is already disabled!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

def enable_usb():
    try:
        if os.path.exists(backup_path):
            shutil.move(backup_path, usb_module_path)
            status_label.config(text="USB enabled!")
        else:
            status_label.config(text="USB is already enabled")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("USB Disable/Enable")

# Create buttons
enable_button = tk.Button(root, text="Enable USB", command=enable_usb)
enable_button.pack()

disable_button = tk.Button(root, text="Disable USB", command=disable_usb)
disable_button.pack()

# Status Label
status_label = tk.Label(root, text="", width=40)
status_label.pack()

root.mainloop()
