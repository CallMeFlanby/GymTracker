import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def action_get_info_dialog(self):
    m_text = "\
******************************************\n\
 Autor: Tino Joseph, Flavio Marta\n\
 Date: 31.03.2022\n\
******************************************"
    messagebox.showinfo(message=m_text, title="Infos")

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("450x450")
        self.title('GymTracker')
        self.resizable()

        #configure grid
        #self.columnconfigure(0)
        #self.columnconfigure(1)

        #self.info()
        self.create_widgets()

    '''
    def info(self):
        m_text = "\
    ******************************************\n\
        Autor: Tino Joseph, Flavio Marta\n\
        Date: 31.03.2022\n\
    ******************************************"
        messagebox.showinfo(message=m_text, title="Infos")
    '''
    def create_widgets(self):
        # Straße
        strasse_label = ttk.Label(self, text="Straße:")
        strasse_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        strasse_entry = ttk.Entry(self)
        strasse_entry.grid(column=1, row=0, sticky=tk.E, pady=5, padx=5)
        # hausnummer
        house_no_label = ttk.Label(self, text="Hausnr.:")
        house_no_label.grid(column=3, row=0, sticky=tk.W, padx=5, pady=5)

        house_no_entry = ttk.Entry(self)
        house_no_entry.grid(column=4, row=0, sticky=tk.E, padx=5, pady=5)

        #postleitzahl
        postcode_label = ttk.Label(self, text="Postleitzahl:")
        postcode_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        postcode_entry = ttk.Entry(self)
        postcode_entry.grid(column=1, row=2, sticky=tk.E, pady=5, padx=5)

        # submit bzw suche
        search_button = ttk.Button(self, text="Suche")
        search_button.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)



if __name__ == "__main__":
    app = App()
    app.mainloop()





"""""
app = Tk()
app.title("test")

info = Label(app, justify=LEFT, font=("Helvetica", 16))

strasse = Entry(app, bd=5, width=20)
hausnummer = Entry(app, bd=5, width=20)


label = Label(app, justify=LEFT, font=("Helvetica", 16), text="Straße: ")

run_button = Button(app, text="Submit", font=("Helvetica", 16), command="")

info.grid(row=0, column=0, columnspan=3, pady=20, padx=50)
strasse.grid(row=2, column=1, pady=20)
hausnummer.grid(row=2, column=4, padx=10)

run_button.grid(row=4, column=2, pady=20)
label.grid(row=2, column=0, pady=20)


menuleiste = Menu(app)
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)
help_menu.add_command(label="Info!", command=action_get_info_dialog)
datei_menu.add_command(label="Exit", command=app.quit)

menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Info", menu=help_menu)

app.config(menu=menuleiste)

app.mainloop()
"""