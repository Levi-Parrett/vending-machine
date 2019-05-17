from __init__ import ItemVend #vending item class
import tkinter as tk #GUI package

#creates an indexed dictionary for each product
products = []
for i in range(8):
	holder = ItemVend(1.00,24,'productName'+str(i))
	products.append(holder)

#possibly redundant credit class to handle current credit a vending machine has
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


#GUI creation
''' this holds previously working GUI elements prior to adding additional frame structure to application
win = tk.Tk()
win.geometry("600x150")

win.title("Vending Machine")

#Frame to display remaining change

title_frame = tk.Frame(win, bd = 2,  bg = '#225356')
title_frame.place(relx = 0, relwidth = 1, relheight = 0.25)

balanceLabel = tk.Label(title_frame,text = "Remaining Ballance: ", bg = '#225356', fg = 'white')
balanceLabel.place(relwidth = 0.2, relheight = 0.9, relx = 0.05, rely = 0.1)

balanceLabe2 = tk.Label(title_frame,text = '{:03.2f}'.format(credit.credit), bg = '#225356' , fg = 'white')
balanceLabe2.place(relwidth = 0.3, relheight = 0.9, relx = 0.47, rely = 0.1)

#selection frame

optionsFrame = tk.Frame(win, bd = 2, bg = '#3aa9bc')
optionsFrame.place(relx= 0, rely = 0.25, relwidth = 1, relheight = 0.75)

optionsLabel = tk.Label(optionsFrame, text="Choose an item:", bg ='#3aa9bc' )
optionsLabel.place(relx = 0.05 , rely= 0.1, relheight = 0.1)

#creation of choice buttons

choice1= tk.Button(optionsFrame, text = ''+products[0].productName, command = lambda: purchaseDrink(products[0]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice1.place(relx = 0.25, rely = 0.1, relwidth = 0.25, relheight = 0.2)

choice2= tk.Button(optionsFrame, text = ''+products[1].productName, command = lambda: purchaseDrink(products[1]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice2.place(relx = 0.25, rely = 0.325, relwidth = 0.25, relheight = 0.2)

choice3= tk.Button(optionsFrame, text = ''+products[2].productName, command = lambda: purchaseDrink(products[2]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice3.place(relx = 0.25, rely = 0.550, relwidth = 0.25, relheight = 0.2)

choice4= tk.Button(optionsFrame, text = ''+products[3].productName, command = lambda: purchaseDrink(products[3]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice4.place(relx = 0.25, rely = 0.775, relwidth = 0.25, relheight = 0.2)

choice5= tk.Button(optionsFrame, text = ''+products[4].productName, command = lambda: purchaseDrink(products[4]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice5.place(relx = 0.6, rely = 0.1, relwidth = 0.25, relheight = 0.2)

choice6= tk.Button(optionsFrame, text = ''+products[5].productName, command = lambda: purchaseDrink(products[5]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice6.place(relx = 0.6, rely = 0.325, relwidth = 0.25 , relheight = 0.2)

choice7= tk.Button(optionsFrame, text = ''+products[6].productName, command = lambda: purchaseDrink(products[6]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice7.place(relx = 0.6, rely = 0.550, relwidth = 0.25, relheight = 0.2)

choice8= tk.Button(optionsFrame, text = ''+products[7].productName, command = lambda: purchaseDrink(products[7]),bg ='#041e33', fg = 'White',relief = 'sunken')
choice8.place(relx = 0.6, rely = 0.775, relwidth = 0.25, relheight = 0.2)

settings = tk.Frame(win).place(relwidth = 1, relheight = 1)
restock_button = tk.Button(settings, text = 'Restock').pack()
settings.tkraise()

win.mainloop()'''
class vend(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Vending Machine')
        self.geometry('600x150')


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
    

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        title_frame = tk.Frame(self, bd = 2,  bg = '#225356')
        title_frame.place(relx = 0, relwidth = 1, relheight = 0.25)
        
        balanceLabel = tk.Label(title_frame,text = "Remaining Ballance: ", bg = '#225356', fg = 'white')
        balanceLabel.place(relwidth = 0.2, relheight = 0.9, relx = 0.05, rely = 0.1)
        
        self.balanceLabel2 = tk.Label(title_frame,text = '{:03.2f}'.format(credit.credit), bg = '#225356' , fg = 'white')
        self.balanceLabel2.place(relwidth = 0.3, relheight = 0.9, relx = 0.47, rely = 0.1)
        
        #selection frame
        
        optionsFrame = tk.Frame(self, bd = 2, bg = '#3aa9bc')
        optionsFrame.place(relx= 0, rely = 0.25, relwidth = 1, relheight = 0.75)
        
        optionsLabel = tk.Label(optionsFrame, text="Choose an item:", bg ='#3aa9bc')
        optionsLabel.place(relx = 0.05 , rely= 0.1, relheight = 0.1)
        
        #creation of choice buttons
        choice1= tk.Button(optionsFrame, text = ''+products[0].productName, command = lambda: self.purchaseDrink(products[0]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice1.place(relx = 0.25, rely = 0.1, relwidth = 0.25, relheight = 0.2)
        
        choice2= tk.Button(optionsFrame, text = ''+products[1].productName, command = lambda: self.purchaseDrink(products[1]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice2.place(relx = 0.25, rely = 0.325, relwidth = 0.25, relheight = 0.2)
        
        choice3= tk.Button(optionsFrame, text = ''+products[2].productName, command = lambda: self.purchaseDrink(products[2]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice3.place(relx = 0.25, rely = 0.550, relwidth = 0.25, relheight = 0.2)
        
        choice4= tk.Button(optionsFrame, text = ''+products[3].productName, command = lambda: self.purchaseDrink(products[3]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice4.place(relx = 0.25, rely = 0.775, relwidth = 0.25, relheight = 0.2)
        
        choice5= tk.Button(optionsFrame, text = ''+products[4].productName, command = lambda: self.purchaseDrink(products[4]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice5.place(relx = 0.6, rely = 0.1, relwidth = 0.25, relheight = 0.2)
        
        choice6= tk.Button(optionsFrame, text = ''+products[5].productName, command = lambda: self.purchaseDrink(products[5]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice6.place(relx = 0.6, rely = 0.325, relwidth = 0.25 , relheight = 0.2)
        
        choice7= tk.Button(optionsFrame, text = ''+products[6].productName, command = lambda: self.purchaseDrink(products[6]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice7.place(relx = 0.6, rely = 0.550, relwidth = 0.25, relheight = 0.2)
        
        choice8= tk.Button(optionsFrame, text = ''+products[7].productName, command = lambda: self.purchaseDrink(products[7]),bg ='#041e33', fg = 'White',relief = 'sunken')
        choice8.place(relx = 0.6, rely = 0.775, relwidth = 0.25, relheight = 0.2)

        button1 = tk.Button(optionsFrame, text="Manage Inventory",command=lambda: controller.show_frame("PageOne"),bg ='#041e33', fg = 'White',relief = 'sunken')
        button1.place(relx = 0.05, rely = 0.5, relwidth = 0.2)
        
    def purchaseDrink (self, item):
	    try:
		    credit.set_credit(float(item.buy(credit.get_credit())))
		    self.balanceLabel2.config(text ='{:03.2f}'.format(credit.get_credit()))
			#print(item.capacity)
			
	    except ValueError:
		    self.balanceLabel2.config(text=(item.buy(credit.get_credit())))
		    self.balanceLabel2.after(2000, lambda: self.balanceLabel2.config(text = '{:03.2f}'.format(credit.credit)))


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button_return = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button_return.place(relx = 0, rely = 0.85 )


if __name__ == "__main__":
    app = vend()
    app.mainloop()
