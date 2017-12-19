from tkinter import *
from tkinter.ttk import *
import pandas as pd
import numpy as np


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

##	TEXT WIDGET PRACTICE ##
		#self.FrameR3C5 = Frame(self)
		#self.FrameR3C5.grid(row=3, column=5, columnspan=1, rowspan=6, sticky=W)
		#self.R3C5 = Text(self.FrameR3C5, height=6, width=45)
		#self.R3C5.pack(side='left', fill='both', expand=True)
		#scrollbar = Scrollbar(self.FrameR3C5)
		#scrollbar.pack(side='right', fill='both', expand=True) #grid(row=3, column=5, rowspan=6, sticky=N+S+E)
		#self.R3C5.insert(END, "Just a text Widget that has an overflow of text we will see what happens\nin multiple lines\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15")
		#self.R3C5.config(state=DISABLED, yscrollcommand=scrollbar.set)
		#scrollbar.config(command=self.R3C5.yview)

		
		#self.R4C4 = Text(self, width=10, height=2) # Text allows users to enter multiple lines of text
		#self.R4C4.grid(row=4, column=4)
### /TEXT ###

## FRAME WITH SCROLLBAR PRACTICE
		df = pd.DataFrame(np.random.randint(0,10000,size=(15, 4)), columns=list('ABCD'))
		print(df)
		print(df.iloc[0,2])
		dfstring = ""
		
		self.FrameR3C6 = Frame(self, height=5)
		self.FrameR3C6.grid(row=3, column=6, columnspan=1, rowspan=6, sticky=NW)
		for i in range(0,15):
			for j in range(0,4):
				#if j==0: b = Label(self.FrameR3C6, text=str(df.iloc[i,j])[0:2])
				#else: b = Label(self.FrameR3C6, text=str(df.iloc[i,j]))
				#b.grid(row=i, column=j)
				if j in (0,1,2): endchar = " | "
				else: endchar = "\n"
				if j==3 and i==14: endchar=""
				if j == 0: prefwidth = 11
				else: prefwidth = 4
				dfstring = dfstring+str(df.iloc[i,j]).ljust(prefwidth)+endchar
				#if j==3: dfstring = dfstring+"\n"
				
		print(dfstring)

		self.textR3C6 = Text(self.FrameR3C6, height=6, width=45)
		self.textR3C6.pack(side='left', fill='both', expand=True)
		self.scrollR3C6 = Scrollbar(self.FrameR3C6)
		self.scrollR3C6.pack(side='right', fill='both', expand=True)
		self.textR3C6.insert(END, dfstring)
		self.textR3C6.config(state=DISABLED, yscrollcommand=self.scrollR3C6.set)
		self.scrollR3C6.config(command=self.textR3C6.yview)




		#self.FrameR3C5 = Frame(self)
		#self.FrameR3C5.grid(row=3, column=5, columnspan=1, rowspan=6, sticky=W)
		#self.R3C5 = Text(self.FrameR3C5, height=6, width=45)
		#self.R3C5.pack(side='left', fill='both', expand=True)
		#scrollbar = Scrollbar(self.FrameR3C5)
		#scrollbar.pack(side='right', fill='both', expand=True) #grid(row=3, column=5, rowspan=6, sticky=N+S+E)
		#self.R3C5.insert(END, "Just a text Widget that has an overflow of text we will see what happens\nin multiple lines\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15")
		#self.R3C5.config(state=DISABLED, yscrollcommand=scrollbar.set)
		#scrollbar.config(command=self.R3C5.yview)



## /FRAME WITH SCROLLBAR




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
		print("R1C1 Fetched")


root = Tk()
root.geometry("1000x750")
app = Application(root)
root.mainloop()






