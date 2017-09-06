from tkinter import *
from tkinter.ttk import *


class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		print("initialized")
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		print("creating widgets")
		self.firstentry = Label(self, text="Mikael")
		self.firstentry.grid(row=2, column=1, sticky=W)
		#self.firstentry.pack()


root = Tk()
root.geometry("400x300")
app = Application(root)
root.mainloop()






