#!/usr/bin/env python3

import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton
import subprocess

def run_command(cmd):
    try:
        process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True)
        stdout, stderr = process.communicate()
        result = stdout + stderr
        result_label.configure(text=result)
        process.wait()
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}")

def ufw_enable():
    run_command('sudo ufw enable')

def ufw_disable():
        run_command('sudo ufw disable')

def ufw_deny():
    port_number = port_number_entry.get()
    run_command(f'sudo ufw deny {port_number}')

def ufw_allow():
    port_number = port_number_entry.get()
    run_command(f'sudo ufw allow {port_number}')

def ufw_reload():
    run_command(f'sudo ufw reload')

def ufw_reset():
    run_command(f'sudo ufw --force reset')

# Theme
customtkinter.set_default_color_theme("material.json")

# create main window
app = customtkinter.CTk()
app.title("Manage Firewall")
app.geometry("400x300")

port_number_label = CTkLabel(app, text="Allow Port Number")
port_number_label.pack()
port_number_entry = CTkEntry(app)
port_number_entry.pack()

# label to display result
result_label = CTkLabel(app, text="")

result_label.pack()

# allow button
enable_button = CTkButton(app, text="Allow", command=ufw_allow)
enable_button.pack()

# deny button
enable_button = CTkButton(app, text="Deny", command=ufw_deny)
enable_button.pack()

# enable button
enable_button = CTkButton(app, text="Enable Firewall", command=ufw_enable)
enable_button.pack()

# disable button
disable_button = CTkButton(app, text="Disable Firewall", command=ufw_disable)
disable_button.pack()

# reload button
reload_button = CTkButton(app, text="Reload Firewall", command=ufw_reload)
reload_button.pack()

# reset button
reset_button = CTkButton(app, text="Reset", command=ufw_reset)
reset_button.pack()

app.mainloop()
