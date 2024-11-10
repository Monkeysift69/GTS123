# This file for anyone who wants to create a folder contain 10 python files for lab and folder name is addressable in GUI

import os
import tkinter as tk
from tkinter import messagebox

def create_files():

    folder_name = folder_entry.get()

    if not folder_name:
        messagebox.showerror("Error", "Please enter a folder name")
        return

    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for i in range(1, 11):
        filename = f"{i}.py"
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w') as file:
            file.write("")
    
    messagebox.showinfo("Success", f"Folder '{folder_name}' and files created successfully!")

root = tk.Tk()
root.title("Folder and File Creator")


label = tk.Label(root, text="Enter folder name:")
label.pack(pady=10)

folder_entry = tk.Entry(root, width=30)
folder_entry.pack(pady=5)

create_button = tk.Button(root, text="Create Files", command=create_files)
create_button.pack(pady=20)

root.mainloop()
