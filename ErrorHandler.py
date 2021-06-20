"""
Ayman Wahbani   209138155
Sapir Ezra      313546194
Moriel Turjeman 308354968
"""
from tkinter import messagebox

def display_error(msg: str):
    '''Inform the user what is wrong with a pop-up message box.'''
    messagebox.showerror(title="Error", message=msg)

def display_info(msg: str):
    messagebox.showinfo(title="Error", message=msg)