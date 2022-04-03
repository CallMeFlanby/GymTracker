import logging
import os
from pathlib import Path
from tkinter.ttk import Notebook

from main.gui import splash_screen
from main.gui.gym_tab import GymTab
from main.gym.gym import Gym
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


def update_gym_notebook(frame, nearby_gyms):
    notebook = Notebook(frame)

    try:
        iterator = iter(nearby_gyms)
        for gym in nearby_gyms:
            if gym == Gym.no_gym_found():
                Label(notebook, text="Kein Fitness Studio gefunden, das tut uns leid. :(").grid(row=0, column=0)
                break
            current_tab = GymTab.create_gym_tab(gym, notebook)
            notebook.add(current_tab, text=gym.name)
    except TypeError:
        logging.info("No address was selected.")
        Label(notebook, text="Bitte eine Adresse eingeben.").grid(row=0, column=0)

    notebook.grid(column=0, row=0, sticky=tk.NSEW)


def create_frames(root):
    # Creating search frame and contents.
    search_frame = ttk.Frame(root)
    search_frame.columnconfigure(0, weight=1)
    search_frame.columnconfigure(1, weight=0)
    search_frame.grid(column=0, row=0, padx=5, pady=5, sticky=tk.EW)

    search_label = ttk.Label(search_frame, text='Adresse')
    search_label.grid(column=0, row=0, columnspan=2, sticky=tk.N)
    search_field = ttk.Entry(search_frame)
    search_field.grid(column=0, row=1, sticky=tk.EW)

    # Creating address listbox frame.
    address_listbox_frame = ttk.Frame(root)
    address_listbox_frame.grid(column=0, row=1, padx=5, pady=5, sticky=tk.NSEW)

    address_listbox_frame.columnconfigure(0, weight=3)
    address_listbox_frame.columnconfigure(1, weight=0)
    address_listbox_frame.grid_rowconfigure(0, weight=1)

    # Creating gym listbox frame.
    gym_listbox_frame = ttk.Frame(root)
    gym_listbox_frame.grid(column=1, row=0, rowspan=3, padx=5, pady=5, sticky=tk.NSEW)
    update_gym_notebook(gym_listbox_frame, "")
    gym_listbox_frame.grid_rowconfigure(0, weight=1)
    gym_listbox_frame.grid_columnconfigure(0, weight=1)

    search_button = ttk.Button(search_frame, text="Suchen")
    search_button.grid(column=1, row=1, sticky= tk.E)

    def search():
        searched = search_field.get()

        found_addresses = Search.search_addresses(searched)

        listbox = Listbox(address_listbox_frame)
        listbox.grid(column=0, row=0, sticky=tk.NSEW)

        scrollbar = Scrollbar(address_listbox_frame)
        scrollbar.grid(column=1, row=0, sticky=tk.NSEW)

        # Cleans the listbox before populating it again.
        listbox.delete(0, END)

        # Insert elements into the listbox.
        for addr in found_addresses:
            listbox.insert(END, addr)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Responsible for the select listener from the list.
        def onselect(event):
            w = event.widget
            idx = int(w.curselection()[0])
            value = w.get(idx)
            nearby_gyms = Search.get_near_gyms(found_addresses[value])
            update_gym_notebook(gym_listbox_frame, nearby_gyms)

        listbox.bind('<<ListboxSelect>>', onselect)

    search_button.config(command=search)

    # Key listener addition.
    def on_press(key):
        if key is keyboard.Key.enter:
            search()

    def on_release(key):
        return

    search()
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


class Window(tk.Tk):
    def __init__(self):
        logging.info("Starting splash screen.")
        # TODO  Shows splash screen? Not sure :(
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
        self.columnconfigure(0, weight=2, minsize=200)
        self.columnconfigure(1, weight=3, minsize=300)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=4)

        create_frames(self)


if __name__ == "__main__":
    app = Window()
    app.mainloop()
