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
		r = range(0,10)
		for i in r:
			self.x = Label(self,text='R'+str(i)+'C0')
			self.x.grid(row=i, column=0)
		for i in r:
			self.x = Label(self,text='R0C'+str(i))
			self.x.grid(row=0, column=i)
		self.R1C1 = Entry(self)
		self.R1C1.grid(row=1, column=1, sticky=W)
		self.R2C1 = Label(self, text="R2C1")
		self.R2C1.grid(row=2, column=1)
		self.R2C2 = Label(self, text="R2C2")
		self.R2C2.grid(row=2, column=2)
		self.R3C3 = Label(self, text="R3C3")
		self.R3C3.grid(row=3, column=3)
		self.R4C4 = Label(self, text="R4C4")
		self.R4C4.grid(row=3, column=3)
		# self.RC = Label(self, text="RC").grid(row=1, column=0) # widgets stack on top of each other when put in the same grid
		
	
	def onefunction(self,*event):
		print("onefunctioncalled")
		self.R0C0.delete(0, END)
		self.R0C0.insert(0, "R0C0")


root = Tk()
root.geometry("1000x750")
app = Application(root)
root.mainloop()






