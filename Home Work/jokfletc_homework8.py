#John Fletcher
#Homework 8

#Problem 9.20
from tkinter import *
from random import randint
import sys
import os

class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.number = 0
        self.rand_number()
    def create_widgets(self):
        self.lbl = Label(self, text="Enter your guess:")
        self.lbl.grid()
        self.ent1 = Entry(self)
        self.ent1.grid()
        
        self.bttn = Button(self, text = "Enter", command = self.guess)
        self.bttn.grid()
        self.ent1.bind('<Return>',self.guess)
        
        
    def rand_number(self):
        self.number = self.number = randint(0,9)
    
    def guess(self,event):
        user_guess = self.ent1.get()
        
        if int(user_guess) == self.number:
            message = "Your guess was correct! \n Let's do this again..."
            toplevel = Toplevel()
            label1 = Label(toplevel, text=message, height=5, width=20)
            label1.pack()
            self.rand_number()
        
        
        self.ent1.delete(0,END)
        
        
    

# main

root = Tk()
root.title("tk")
root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()




