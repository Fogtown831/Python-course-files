from tkinter import*
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title('Clock')
root.resizable(0,0)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('Calibri', 90), background = 'black', foreground = 'red')

lbl.pack (anchor = 'center')
time()


mainloop()
