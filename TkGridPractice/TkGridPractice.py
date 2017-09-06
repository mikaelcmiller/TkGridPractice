from tkinter import *
from tkinter.ttk import *


class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		print("initialized")
		self.grid()
		self.create_widgets()
		self.bind_all('<Return>',self.onefunction)

	def create_widgets(self):
		print("creating widgets")
		self.firstentry = Entry(self)
		self.firstentry.grid(row=2, column=1, sticky=W)
	
	def onefunction(self,*event):
		print("onefunctioncalled")
		self.firstentry.delete(0, END)
		self.firstentry.insert(0, "Mikael")


root = Tk()
root.geometry("400x300")
app = Application(root)
root.mainloop()






