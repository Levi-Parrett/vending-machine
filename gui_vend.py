from __init__ import ItemVend #vending item class
import tkinter as tk #GUI package

#creates an indexed dictionary for each product
products = []
for i in range(8):
	holder = ItemVend(1.00,24,'productName'+str(i))
	products.append(holder)

class credits:
	def __init__(self, amount):
		self.credit = amount
	def load(self,money):
		self.credit+= money
	def get_credit(self):
		return self.credit
	def set_credit(self,value):
		self.credit = value
credit = credits(26.00)

def purchaseDrink (item):
	try:
		credit.set_credit(float(item.buy(credit.get_credit())))
		balanceLabe2.config(text ='{:03.2f}'.format(credit.get_credit()))
	except ValueError:
		balanceLabe2.config(text=(item.buy(credit.get_credit())))
		balanceLabe2.after(2000, lambda: balanceLabe2.config(text = '{:03.2f}'.format(credit.credit)))

win = tk.Tk()
win.geometry("600x300")

win.title("Vending Machine")

balanceLabel = tk.Label(win,text = "Remaining Ballance: ")
balanceLabel.pack()
balanceLabe2 = tk.Label(win,text = '{:03.2f}'.format(credit.credit))
balanceLabe2.pack()

optionsFrame = tk.Frame(win)
optionsFrame.pack()

optionsLabel = tk.Label(optionsFrame, text="Choose an item")
optionsLabel.pack()
for i in range(8):
	tk.Button(optionsFrame, text = ''+products[i].productName, command = lambda: purchaseDrink(products[i])).pack()

win.mainloop()
'''from tkinter import messagebox
root = tk.Tk()
frame = tk.Frame(root, height = 200 , width = 400)

def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")
   
holder = ItemVend(1.00,24,'fizzydrink')
   
item1_button= tk.Button(frame, text = "hello", command =holder.buy(credit.get_credit()))
item1_button.place( x= 50, y=50)


creditLabel = tk.Label( root, text = "Your current credit ballence is "+str(credit.get_credit))

creditLabel.pack()


frame.pack()
root.title('Vending Machine')
root.mainloop()'''

