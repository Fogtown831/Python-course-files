#Question 1 (Part 1 and 2)
import tkinter as tk
from tkinter.ttk import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageTk

root = tk.Tk()
root.title("CSUMB App")
root.geometry("800x600")
root.resizable(0,0)
root.configure(bg="light blue")
img = Image.open('logo.png')
img1 = img.convert('RGBA')
img2 = img1.getdata()

newData = []
for item in img2:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img1.putdata(newData)
img1.save('logo2.png')
picture = Image.open("logo2.png")
resizedpic = picture.resize((100, 100), Image.ANTIALIAS)
resizedpic1 = ImageTk.PhotoImage(resizedpic)
label = Label(root, image=resizedpic1)
label.place(x=350, y=10)

def Calendar1():
   data = pd.read_csv("exam1.csv")
   df = pd.DataFrame(data, columns=['CalendarDate'])
   lb.config(text=df)
b1 = tk.Button(text="Calendar", font=("Arial", 15), bg="light green",
              command=Calendar1)
b1.place(x=425, y=170)
lb = tk.Label( font=("Arial", 7), text=" ", justify="left")
lb.place(x=125, y=130)

def Buildings1():
   data1 = pd.read_csv("exam1.csv")
   col = pd.DataFrame(data1, columns=['Buildings'])
   lb.config(text=col)
b2 = tk.Button(text="Buildings", font=("Arial", 15), bg="light green",
              command= Buildings1)
b2.place(x=525, y=170)
lb = tk.Label( font=("Arial", 10), text=" ", justify="left")
lb.place(x=30, y=130)

def Faculty1():
   data1 = pd.read_csv("exam1.csv")
   col = pd.DataFrame(data1, columns=['FacultyName'])
   lb.config(text=col)
b2 = tk.Button(text="Faculty", font=("Arial", 15), bg="light green",
              command= Faculty1)
b2.place(x=623, y=170)
lb = tk.Label( font=("Arial", 10), text=" ", justify="left")
lb.place(x=30, y=130)


tk.mainloop()


#Question 2

import tkinter as tk
from tkinter.ttk import *
import pandas as pd
import random
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageTk

root = tk.Tk()
root.title("CSUMB App")
root.geometry("800x600")
root.resizable(0,0)
img = Image.open('logo.png')
img1 = img.convert('RGBA')
img2 = img1.getdata()

newData = []
for item in img2:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img1.putdata(newData)
img1.save('logo2.png')
picture = Image.open("logo2.png")
resizedpic = picture.resize((100, 100), Image.ANTIALIAS)
resizedpic1 = ImageTk.PhotoImage(resizedpic)
label = Label(root, image=resizedpic1)
label.place(x=350, y=10)

def Calendar1():
   data = pd.read_csv("exam1.csv")
   df = pd.DataFrame(data, columns=['CalendarDate'])
   lb.config(text=df)
b1 = tk.Button(text="Calendar", font=("Arial", 15), bg="light green",
              command=Calendar1)
b1.place(x=425, y=170)
lb = tk.Label( font=("Arial", 7), text=" ", justify="left")
lb.place(x=125, y=130)

def Buildings1():
   data1 = pd.read_csv("exam1.csv")
   col = pd.DataFrame(data1, columns=['Buildings'])
   lb.config(text=col)
b2 = tk.Button(text="Buildings", font=("Arial", 15), bg="light green",
              command= Buildings1)
b2.place(x=525, y=170)
lb = tk.Label( font=("Arial", 10), text=" ", justify="left")
lb.place(x=30, y=130)

def Faculty1():
   data1 = pd.read_csv("exam1.csv")
   col = pd.DataFrame(data1, columns=['FacultyName'])
   lb.config(text=col)
b3 = tk.Button(text="Faculty", font=("Arial", 15), bg="light green",
              command= Faculty1)
b3.place(x=623, y=170)
lb = tk.Label( font=("Arial", 10), text=" ", justify="left")
lb.place(x=30, y=130)

def LuckyFaculty1():
    names = []
    # Open csv file
    with open('exam1.csv', 'r') as fp:
        # Read csv file
        reader = csv.reader(fp, delimiter=' ', skipinitialspace=False)
        # Skip header
        next(reader)
        # Iterate through rows and create names and seats array
        for cloumn in reader:
            names.append(cloumn[2])
    name = random.choice(names)
    print(name)
    computer_action = random.choice(name)
    print(computer_action)
    lb5.config(text=computer_action)
b4 = tk.Button(text="Lucky Faculty", font=("Arial", 15), bg="light green",
              command= LuckyFaculty1)
b4.place(x=525, y=370)
lb5 = tk.Label( font=("Arial", 10), text=" ", justify="left")
lb5.place(x=30, y=130)

tk.mainloop()


#Question 3 Part 1
from tkinter import *


def main():
    root = Tk()
    root.geometry("450x230")
    label1 = Label(text="Enter Weight in LBS", font=("Arial", 13)).place(x=25, y=30)
    textbox1 = Entry(root, width=12)
    textbox1.place(x=200, y=35)
    label2 = Label(root, text=" ")
    label2.place(x=180, y=100)

    def Weight1():
        pounds = round(float(textbox1.get()) / 2.20462, 2)
        label2.configure(text=str(pounds) + '  Pounds')

b1 = Button(root, text="Submit", command=Weight1, font=("Arial", 13)).place(x=95, y=75)

root.mainloop()


main()

#Question 3 Part 2
from PyPDF2 import PdfFileReader, PdfFileWriter
import webbrowser
pdf_file = 'Paper.pdf'
pdf = PdfFileReader(pdf_file)

pdfwriter = PdfFileWriter()

for page_num in range(1,10):
    pdfwriter.addPage(pdf.getPage(page_num))

with open('NewPDF.pdf', 'wb') as out:
    pdfwriter.write(out)

webbrowser.open_new('NewPDF.pdf')

