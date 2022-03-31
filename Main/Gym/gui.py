import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math as m

def action_get_info_dialog():
    m_text = "\
**************************\n\
 Autor: Tino Joseph, Flavio Correira Marta\n\
 Date: 31.03.2022\n\
 Version: 0.0001\n\
**************************"
    messagebox.showinfo(message=m_text, title="Infos")

def createNewWindow():

    def button_action():
        eingabefeld_str = eingabefeld.get()
        eingab = float(eingabefeld_str)

        eingabefeld_str2 = eingabefeld2.get()
        eingab2 = float(eingabefeld_str2)

        summe = (eingab + eingab2)
        ausgabe.configure(text=summe)



    fenster = Tk()
    fenster.title("test")

    info = Label(fenster, justify=LEFT, font=("Helvetica", 16))

    eingabefeld = Entry(fenster, bd=5, width=20)
    eingabefeld2 = Entry(fenster, bd=5, width=20)

    label = Label(fenster, justify=LEFT, font=("Helvetica", 16), text="Ausgabe: ")
    ausgabe = Label(fenster, justify=CENTER, font=("Helvetica", 16), text=" ")
    run_button = Button(fenster, text="Ausgabe", font=("Helvetica", 16), command=button_action)

    info.grid(row=0, column=0, columnspan=3, pady=20, padx=50)
    eingabefeld.grid(row=2, column=0, pady=20)
    eingabefeld2.grid(row=3, column=0, pady=20)
    run_button.grid(row=4, column=2, pady=20)
    label.grid(row=4, column=0, pady=20)
    ausgabe.grid(row=5, column=2, columnspan=2, pady=20)

    menuleiste = Menu(fenster)
    datei_menu = Menu(menuleiste, tearoff=0)
    help_menu = Menu(menuleiste, tearoff=0)
    help_menu.add_command(label="Info!", command=action_get_info_dialog)
    datei_menu.add_command(label="Exit", command=fenster.quit)

    menuleiste.add_cascade(label="Datei", menu=datei_menu)
    menuleiste.add_cascade(label="Help", menu=help_menu)

    fenster.config(menu=menuleiste)

    fenster.mainloop()


app = tk.Tk()
buttonExample = tk.Button(app,
                          text="test",
                          command=createNewWindow)
buttonExample.pack()


buttonExample.pack()

menuleiste = Menu(app)
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)
help_menu.add_command(label="Info!", command=action_get_info_dialog)
datei_menu.add_command(label="Exit", command=app.quit)

menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

app.config(menu=menuleiste)

app.mainloop()