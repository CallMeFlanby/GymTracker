import json
import os
from pathlib import Path
from main.address.addresses import Addresses
from main.address.address import Address
from main.gym.gym import Gym
from main.utils.contact import Contact
from main.utils.search import Search

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

addresses = Addresses.get()


def action_get_info_dialog(self):
    m_text = "\
******************************************\n\
 Autor: Tino Joseph, Flavio Marta\n\
 Date: 31.03.2022\n\
******************************************"
    messagebox.showinfo(message=m_text, title="Infos")

class fenster(tk.Tk):
    def __init__(self):


        super().__init__()

        path = Path(os.getcwd())
        icon = os.path.join(path.parent.absolute().parent.absolute(), 'documentation', 'GymTracker_logo.ico')
        self.iconbitmap(icon)
        self.geometry("600x200")
        self.title('GymTracker')
        self.resizable()

        # configure grid
        # self.columnconfigure(0)
        # self.columnconfigure(1)

        # self.info()
        self.create_widget()

    '''
    def info(self):
        m_text = "\
    ******************************************\n\
        Autor: Tino Joseph, Flavio Marta\n\
        Date: 31.03.2022\n\
    ******************************************"
        messagebox.showinfo(message=m_text, title="Infos")
    '''

    def create_widget(self):
        # Straße
        search_label = ttk.Label(self, text="Suche:")
        search_label.grid(column=0, row=0, columnspan=1, rowspan=1)

        search_field = ttk.Entry(self)
        search_field.grid(column=1, row=0, columnspan=1, rowspan=1)

        def search():
            frame = ttk.Frame(self)

            searched = search_field.get()
            found_addresses = Search.search_addresses(searched)

            x_row = 1
            for x in found_addresses:
                found_label = ttk.Label(frame, text=x)
                found_label.grid(column=0, row=x_row, sticky=tk.W, columnspan=1, rowspan=1)

                x_row = x_row + 1
                sep = ttk.Separator(frame, orient='horizontal')
                sep.grid(column=0, row=x_row, columnspan=1, rowspan=1)
                x_row = x_row+1
            frame.grid(column=0, row=1, columnspan=3, rowspan=1)

        #
        search_button = ttk.Button(self, text="Suchen", command=search)
        search_button.grid(column=2, row=0, columnspan=1, rowspan=1)


if __name__ == "__main__":
    app = fenster()
    app.mainloop()