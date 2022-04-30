from yahoo_fin import stock_info #program for Yahoo Finance in order to get stock price
from tkinter import * #TkInter program for creating a GUI


def stockprice(): #Defining the code, I gave the name stockprice
    price = stock_info.get_live_price(entry1.get()) #borrowed, code the connects the entry to the program yahoofinance
    Current_stock.set(price) #borrowed, code the gets the current stock price using program


root = Tk() #can use root or anything, gui set up
Current_stock = StringVar() #borrowed, current stock interchanges sting and varriables

Label(root, text="Ticker Symbol: ").grid(row=0) #code for a label master is a refenrece to TK, text is the text it diplays, .grid is it placement in the GUi
Label(root, text="Stock Price:").grid(row=3)  #text is the text it diplays, .grid is it placement in the GUi

result = Label(root, text="", textvariable=Current_stock).grid(row=3, column=1) #borrowed and added some code such as a grid function


entry1 = Entry(root) #entry box
entry1.grid(row=0, column=1) #placement for entry box

button1 = Button(root, text="Show", command=stockprice) #I custom made this button to allow a subimision to the gui
button1.grid(row=0, column=2)#placement in gui for button

mainloop()#closing the program