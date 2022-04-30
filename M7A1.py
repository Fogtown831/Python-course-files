

###


from tkinter import *
from openpyxl import *


root = Tk()
root.title("CSUMB Student App")
root.geometry("300x200")
root.resizable(0,0)
bg = PhotoImage(file="csumbtransparent.png")
label = Label(root, image=bg)
label.place(x=0, y=0)

wb = load_workbook('M7A1.xlsx')
ws = wb.active
column_a = ws['A']

def submit():
    list = ''
    for cell in column_a:
        list = f'{list +str(cell.value)}\n'
        label1.config(text=list)

button1 = Button(root, text="Student's Name", command=submit)
button1.place(x=100, y=75)

label1 = Label(root, text = "  ")
label1.place(x=135, y=100)

root.mainloop()