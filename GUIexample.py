#---------
#Import stuff here
#---------
import tkinter as tk

#keydown Function
def click():
	entered_text = textentry.get()
	output.delete(0.0,'end')
	#delete from before the first line and column to end
	try:
		definition = my_compdictionary[entered_text]
	except:
		definition = 'Sorry there is not word like that please try again'
	output.insert('end',definition)
	
def close_window():
	win.destroy()
	exit()

#Create Instance
win = tk.Tk()

#Add title to GUI
win.title("MY Computer Glossary")
#add a background
win.configure(background= 'Black')

#adding photo
photo = tk.PhotoImage(file = "c:\\Users\\Levi Parrett\\Pictures\\NoRespect.PNG")
tk.Label (win, image = photo, bg = 'black').grid(row = 0, column = 0, sticky = 'W')

#create Label
tk.Label(win, text="Enter the word you would like a definition for:", bg="black", fg="white", font="none 8 bold").grid(row=1, column=0, sticky = 'W')

#create text entry box
textentry = tk.Entry(win, width=20, bg="white")
textentry.grid(row=2, column=0, sticky = 'W')

tk.Button(win,text = "Submit", width = 6, command = click).grid(row=3, column = 0, sticky ='W')

#add another Label
tk.Label(win, text = "\nDefinition:", bg = 'black', fg='white', font = 'none 8 bold').grid(row =4 , column = 0 , sticky = 'W')

#create a text outputBox
output = tk.Text(win, width = 75, height = 6, wrap = 'word', background = 'white')
output.grid(row = 5, column=0, columnspan = 2, sticky = 'W')

#add a dictionary
my_compdictionary = {'algorithm': 'Step by step instructions to complete a task', 'bug':'piece of code that causes a proram to fail'
	}

#add a exit label
tk.Label(win, text = 'Click to exit', bg= 'black', fg = 'white', font = 'none 12 bold').grid(row = 11, column = 0, sticky = 'W')

#add exit button
tk.Button(win, text = 'Exit', width = 14, command = close_window).grid(row=12, column = 0, sticky = 'W')	

#Start GUI Loop
win.mainloop()
