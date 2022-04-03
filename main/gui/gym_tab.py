import tkinter
from tkinter import Frame
from tkinter.ttk import Label, Separator


class GymTab():

    @staticmethod
    def create_gym_tab(gym, notebook):
        current_tab = Frame(notebook)

        index = 0
        Label(current_tab, text="Name:").grid(row=index, column=0, sticky=tkinter.E)
        Label(current_tab, text=gym.name).grid(row=index, column=1, sticky=tkinter.W)

        index = index+1
        Separator(current_tab, orient='horizontal').grid(row=index, column=0, columnspan=2, sticky=tkinter.EW)

        index = index+1
        Label(current_tab, text="Öffnungszeiten:").grid(row=index, column=0, sticky=tkinter.E)
        Label(current_tab, text=gym.opening_hours).grid(row=index, column=1, sticky=tkinter.W)

        index = index+1
        Separator(current_tab, orient= 'horizontal').grid(row=index, column=0, columnspan=2, sticky=tkinter.EW)

        index = index+1
        Label(current_tab, text="Anschrift:").grid(row=index, column=0, sticky=tkinter.NE)
        Label(current_tab, text=gym.address.get_address()).grid(row=index, column=1, sticky=tkinter.W)

        index = index+1
        Separator(current_tab, orient= 'horizontal').grid(row=index, column=0, columnspan=2, sticky=tkinter.EW)

        index = index+1
        Label(current_tab, text="Kontaktdaten").grid(row=index, column=0, sticky=tkinter.E)
        index = index+1
        Label(current_tab, text="Telefon:").grid(row=index, column=0, sticky=tkinter.E)
        Label(current_tab, text=gym.contact.telephone).grid(row=index, column=1, sticky=tkinter.W)
        index = index+1
        Label(current_tab, text="Handy:").grid(row=index, column=0, sticky=tkinter.E)
        Label(current_tab, text=gym.contact.mobile).grid(row=index, column=1, sticky=tkinter.W)
        index = index+1
        Label(current_tab, text="E-Mail:").grid(row=index, column=0, sticky=tkinter.E)
        Label(current_tab, text=gym.contact.mail).grid(row=index, column=1, sticky=tkinter.W)
        index = index+1
        Label(current_tab, text="Website:").grid(row=index, column=0, sticky=tkinter.E)
        Label(current_tab, text=gym.contact.website).grid(row=index, column=1, sticky=tkinter.W)
        index = index+1
        Separator(current_tab, orient='horizontal').grid(row=index, column=0, columnspan=2, sticky=tkinter.EW)
        index = index+1

        Label(current_tab, text="Koordinaten:").grid(row=index, column=0, sticky=tkinter.E)
        Label(current_tab, text=gym.coordinates).grid(row=index, column=1, sticky=tkinter.W)

        current_tab.grid_columnconfigure(0, weight=1)
        current_tab.grid_columnconfigure(1, weight=1)

        return current_tab
