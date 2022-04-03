import logging
import os
import tkinter
from pathlib import Path
from tkinter.ttk import Style

from main.gui import splash_screen
from main.utils.search import Search

from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

from pynput import keyboard


def action_get_info_dialog(self):
    m_text = "\
******************************************\n\
 Autor: Tino Joseph, Flavio Marta\n\
 Date: 31.03.2022\n\
******************************************"
    messagebox.showinfo(message=m_text, title="Infos")


def create_frames(root):

    # Creating search frame and contents.
    search_frame = ttk.Frame(root)
    search_label = ttk.Label(search_frame, text='Addresse')
    search_label.grid(column=0, row=0)
    search_field = ttk.Entry(search_frame)
    search_field.grid(column=1, row=0, ipadx=5, sticky=tk.EW)

    search_frame.columnconfigure(0, weight=0)
    search_frame.columnconfigure(1, weight=3)
    search_frame.columnconfigure(2, weight=0)
    search_frame.grid(column=0, row=0, sticky=tk.EW)

    # Creating listbox frame.
    listbox_frame = ttk.Frame(root)
    listbox_frame.grid(column=0, row=1, padx=5, pady=5, sticky=tk.NSEW)

    search_button = ttk.Button(search_frame, text="Suchen", command=search(listbox_frame, search_field))
    search_button.grid(column=2, row=0)
    listbox_frame.columnconfigure(0, weight=3)
    listbox_frame.columnconfigure(1, weight=0)
    listbox_frame.grid_rowconfigure(0, weight=1)

    # Key listener addition.
    def on_press(key):
        if key is keyboard.Key.enter:
            search(listbox_frame, search_field)

    def on_release(key):
        return

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


def search(frame, search_field):
    # Cleans the frame before population it again.
    for widget in frame.winfo_children():
        widget.destroy()

    searched = search_field.get()
    found_addresses = Search.search_addresses(searched)

    listbox = Listbox(frame)
    listbox.grid(column=0, row=0, sticky=tk.NSEW)

    scrollbar = Scrollbar(frame)
    scrollbar.grid(column=1, row=0, sticky=tk.NSEW)

    # Insert elements into the listbox.
    for values in found_addresses:
        listbox.insert(END, values)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

class Window(tk.Tk):
    def __init__(self):
        # Shows splash screen? Not sure :(
        logging.info("Starting splash screen.")
        splash_screen
        super().__init__()

        path = Path(os.getcwd())
        icon = os.path.join(path.parent.absolute().parent.absolute(), 'documentation', 'GymTracker_logo.ico')
        self.iconbitmap(icon)
        self.title('GymTracker')
        self.resizable()

        # Responsible for centering the window.
        window_height = 500
        window_width = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)

        create_frames(self)


if __name__ == "__main__":
    app = Window()
    app.mainloop()
