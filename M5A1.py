#this is a code to that helps generate a random password
#Source https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9
from tkinter import *
import random         #I added these three lines to set up the tkinter which is the package used for the GUI
import string

def genie():
    password = []  #these lines of code is defining the data in the generator
    for i in range(3):
        lower=random.choice(string.ascii_lowercase) #defining the data set using string and making it randomly selected
        upper=random.choice(string.ascii_uppercase)#defining the data set using string and making it randomly selected
        num=random.choice(string.digits) #defining the data set using string digits
        password.append(lower) #storing the data lower case
        password.append(upper) #storing the data uppercase
        password.append(num) #storing the data numbers
        passw=" ".join(str(x)for x in password) # passing combined data with length and joining them
        label.config(text=passw) #configuration

root = Tk()  #this line of code and the following are setting up the graphical interface
label = Label(root, font = ('arial', 40, 'bold')) #this line is the font and its size for the label
label.pack() #this is setting up the GUI's print out
button1 = Button(root,text="Generate", fg='white', bg='black', font = ('arial', 40, 'bold'), command = genie) #this line is for labeling and font of the button on the gui
button1.place(x=200,y=300) #this line is for placement of the button
root.geometry("700x700") #size of the gui
root.title("Password Generator") #this is what is printed when button is clicked
root.resizable(0, 0) #does not allow user to adjust GUI
root.mainloop() #this loops the function to allow the user multiple clicks