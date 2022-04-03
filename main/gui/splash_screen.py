import os
import tkinter as tk
from pathlib import Path

panel = tk.Tk()

# Shows no frame.
panel.overrideredirect(True)

# Centers splash screen.
width = panel.winfo_screenwidth()
height = panel.winfo_screenheight()
panel.geometry('%dx%d+%d+%d' % (width * 0.8, height * 0.8, width * 0.1, height * 0.1))

# Loads the logo.
path = Path(os.getcwd())
image_file = os.path.join(path.parent.absolute(), 'documentation', 'GymTracker_logo.png')

# Centers the image.
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(panel, height=height * 0.8, width=width * 0.8)
canvas.create_image(width * 0.8 / 2, height * 0.8 / 2, image=image)
canvas.pack()

label = tk.Label(text="Copyright: Flávio Marta & Tino Joseph")
label.pack()

# Show for 2 seconds.
panel.after(2000, panel.destroy)
