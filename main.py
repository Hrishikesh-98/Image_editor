from tkinter import *
from PIL import Image, ImageTk
from classes.Edit import *
from classes.Load import *

class Run:
    def __init__(self, window):
        self.image_path = "none"
        self.main_image = "none"
        main_menu = Menu(window)
        window.config(menu=main_menu, bg="black")
        window.title("Image Editor")
        file_menu = Menu(main_menu)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New..")
        file_menu.add_command(label="Open..", command=self.openimage)
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save As..")
        file_menu.add_command(label="Exit")

        edit_menu = Menu(main_menu)
        main_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Resize", command=self.resizeImage)
        edit_menu.add_command(label="Rotate")
        edit_menu.add_command(label="Crop")
        edit_menu.add_command(label="Flip")
        edit_menu.add_command(label="Combine")

        filter_menu = Menu(edit_menu)
        edit_menu.add_cascade(label="Filter", menu=filter_menu)
        filter_menu.add_command(label="Black and White")
        filter_menu.add_command(label="Blur")
        filter_menu.add_command(label="Sharpen")
        filter_menu.add_command(label="Edges")
        window.mainloop()

    def openimage(self):
        self.main_image = openFileDialog(window)

    def resizeImage(self):
        imageResize(self.main_image, window)

window = Tk()
run = Run(window)

