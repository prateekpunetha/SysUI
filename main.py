#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_password():
    try:
        password = subprocess.check_output(['zenity', '--password'], text=True).strip()
        return password
    except subprocess.CalledProcessError as e:
        print(f"Error getting password: {e}")
        return None

def execute_python_script(script_path):
    try:
        password = get_password()
        if password is not None:
            subprocess.run(['sudo', '-S', 'python', script_path], input=password, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")

def execute_without_root(script_path):
    try:
            subprocess.run(['python', script_path])
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")

def create_user():
    script_path = 'src/createuser.py'
    execute_python_script(script_path)

def rm_user():
    script_path = 'src/rmuser.py'
    execute_python_script(script_path)

def manage_ssh():
    script_path = 'src/rootlogin.py'
    execute_python_script(script_path)

def manage_firewall():
    script_path = 'src/firewall.py'
    execute_python_script(script_path)

def toggle_usb():
    script_path = 'src/usbtoggle.py'
    execute_python_script(script_path)

def encrypt_file():
    script_path = 'src/encfile.py'
    execute_without_root(script_path)

def open_htop():
    script_path = 'src/htop.py'
    execute_without_root(script_path)

def bind_label_click(label, func):
    label.bind("<Button-1>", lambda event: func())
    label.bind("<Enter>", lambda event: label.config(cursor="hand2"))
    label.bind("<Leave>", lambda event: label.config(cursor=""))

def create_label(frame, image_path, text, command, row, column):
    img = Image.open(image_path)
    img = img.resize(icon_size)
    img = ImageTk.PhotoImage(img)
    label = Label(frame, image=img, background='white')
    label.image = img
    label.grid(row=row, column=column, padx=(20, 20), pady=(20, 0), sticky='n')
    bind_label_click(label, command)

    text_label = Label(frame, text=text, background='white')
    text_label.grid(row=row + 1, column=column, padx=(20, 20), pady=(0, 20), sticky='s')

    return {'label': label, 'text_label': text_label, 'visible': True}

win = Tk()
win.title("SysUI")
win.geometry('800x800')

icon_size = (60, 60)
num_columns = 3  # adjust number of columns

frame1 = Frame(win, background='white')
frame1.pack(expand=True, fill='both')

frame2 = Frame(frame1, background='white')
frame2.pack(expand=True, fill='both', side='top')

labels_info = [
    {'image': resource_path('img/hundred.png'), 'text': 'Create User', 'command': create_user},
    {'image': resource_path('img/remove.png'), 'text': 'Remove User', 'command': rm_user},
    {'image': resource_path('img/shield.png'), 'text': 'Manage Firewall', 'command': manage_firewall},
    {'image': resource_path('img/ssh.png'), 'text': 'SSH Settings', 'command': manage_ssh},
    {'image': resource_path('img/usb.png'), 'text': 'Toggle USB', 'command': toggle_usb},
    {'image': resource_path('img/enc.png'), 'text': 'Secure File', 'command': encrypt_file},
    {'image': resource_path('img/monitor.png'), 'text': 'Process Viewer', 'command': open_htop},
]

labels = []

total_icons = len(labels_info)
num_rows = (total_icons + num_columns - 1) // num_columns  # calculate the number of rows needed

for i, label_info in enumerate(labels_info):
    row = i // num_columns * 2  # each label and text label occupy two rows
    column = i % num_columns
    label_data = create_label(frame2, label_info['image'], label_info['text'], label_info['command'], row, column)
    labels.append(label_data)

# configure column weights to distribute available space evenly
for i in range(num_columns):
    frame2.columnconfigure(i, weight=1)

def toggle_visibility():
    for label_info in labels:
        label_info['label'].config(state='normal' if label_info['visible'] else 'hidden')
        label_info['text_label'].config(state='normal' if label_info['visible'] else 'hidden')

def on_resize(event):
    toggle_visibility()

win.bind("<Configure>", on_resize)

toggle_visibility()  # Initialize visibility

win.mainloop()
