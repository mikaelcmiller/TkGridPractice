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
		self.bind_all('n',self.fetchR1C1)

	def create_widgets(self):
		print("creating widgets")
		r = range(0,25)
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
		self.R4C4 = Text(self, width=10, height=2) # Text allows users to enter multiple lines of text
		self.R4C4.grid(row=4, column=4)
		self.R5C4 = Entry(self).grid(row=5, column=4) # Use entry for single-line values
		# self.RC = Label(self, text="RC").grid(row=1, column=0) # widgets stack on top of each other when put in the same grid
		
	
	def onefunction(self,*event):
		print("onefunctioncalled")
		self.R1C1.delete(0, END)
		self.R1C1.insert(0, "R0C0")

	def fetchR1C1(self,*event):
		got = self.R1C1.get()
		print(got)
		self.R1C1.delete(0, END)
		self.R1C1.insert(0, got)


root = Tk()
root.geometry("1000x750")
app = Application(root)
root.mainloop()






