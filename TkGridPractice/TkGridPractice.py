from tkinter import *
from tkinter.ttk import *


class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		print("initialized")
		self.grid()
		self.create_widgets()
		self.bind_all('<Return>',self.resetfunction)
		self.bind_all('n',self.fetchR1C1)
		self.bind_all('c',self.clearall)

	def create_widgets(self):
		self.entrylist = []
		print("creating widgets")
		r = range(1,30)
		for i in r:
			self.x = Label(self,text='R'+str(i))
			self.x.grid(row=i, column=0)
			self.x = Label(self,text='C'+str(i))
			self.x.grid(row=0, column=i)
		self.R1C1 = Entry(self)
		self.entrylist.append(self.R1C1)
		self.R1C1.grid(row=1, column=1, sticky=W)
		self.R2C1 = Label(self, text="R2C1")
		self.R2C1.grid(row=2, column=1)
		self.R2C2 = Label(self, text="R2C2")
		self.R2C2.grid(row=2, column=2)
		self.R3C3 = Label(self, text="R3C3")
		self.R3C3.grid(row=3, column=3)
		#self.R4C4 = Text(self, width=10, height=2) # Text allows users to enter multiple lines of text
		#self.R4C4.grid(row=4, column=4)
		self.R5C4 = Entry(self)
		self.R5C4.grid(row=5, column=4) # Use entry for single-line values
		# self.RC = Label(self, text="RC").grid(row=1, column=0) # widgets stack on top of each other when put in the same grid
		self.entrylist.append(self.R5C4)
		self.R6C4 = Entry(self)
		self.R6C4.grid(row=6, column=4)
		self.entrylist.append(self.R6C4)
		self.R20C20 = Entry(self)
		self.R20C20.grid(row=20, column=20)
		self.entrylist.append(self.R20C20)
		self.R21C20 = Label(self, text="Label R21C20").grid(row=21, column=20)

	def clearall(self, *event):
		for entry in self.entrylist:
			entry.delete(0, END)
		print("Clear Activated")

	def resetfunction(self,*event):
		print("Default R1C1 Activated")
		self.R1C1.delete(0, END)
		self.R1C1.insert(0, "[R1C1 Default value]")

	def fetchR1C1(self,*event):
		got = self.R1C1.get()
		print(got)
		self.R1C1.delete(0, END)
		self.R1C1.insert(0, got)


root = Tk()
root.geometry("1000x750")
app = Application(root)
root.mainloop()






