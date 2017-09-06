from tkinter import *
from tkinter.ttk import *


class Application(Frame):
	def __init__(self, master):
		print("initialized")

root = Tk()
root.geometry("400x300")
app = Application(root)
root.mainloop()






