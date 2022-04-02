import os
from pathlib import Path

from main.gui import splash_screen
from main.utils.search import Search

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from pynput import keyboard


def action_get_info_dialog(self):
    m_text = "\
******************************************\n\
 Autor: Tino Joseph, Flavio Marta\n\
 Date: 31.03.2022\n\
******************************************"
    messagebox.showinfo(message=m_text, title="Infos")


class Window(tk.Tk):
    def __init__(self):

        # Shows splash screen? Not sure :(
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

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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

        frame = ttk.Frame(self)

        def search():

            # Cleans the frame before population it again.
            for widget in frame.winfo_children():
                widget.destroy()

            searched = search_field.get()
            found_addresses = Search.search_addresses(searched)

            listbox = Listbox(frame)
            listbox.grid(column=0, row=0, columnspan=3, rowspan=1)

            scrollbar = Scrollbar(frame)
            scrollbar.grid(column=4, row=0, columnspan=1, rowspan=1)

            # Insert elements into the listbox.
            for values in found_addresses:
                listbox.insert(END, values)

            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)

            """""
            x_row = 1
            for x in found_addresses:
                found_label = ttk.Label(frame, text=x)
                found_label.grid(column=0, row=x_row, sticky=tk.W, columnspan=1, rowspan=1)

                x_row = x_row + 1
                sep = ttk.Separator(frame, orient='horizontal')
                sep.grid(column=0, row=x_row, columnspan=1, rowspan=1)
                x_row = x_row + 1
            """
            frame.grid(column=0, row=1, columnspan=3, rowspan=1)

        search()
        search_button = ttk.Button(self, text="Suchen", command=search)
        search_button.grid(column=2, row=0, columnspan=1, rowspan=1)

        # Key listener addition.
        def on_press(key):
            if key is keyboard.Key.enter:
                search()

        def on_release(key):
            return

        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()


if __name__ == "__main__":
    app = Window()
    app.mainloop()
