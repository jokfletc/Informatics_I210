from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="This is a label!")
        self.lbl.grid()

        self.lb2 = Label(self, text="What would you like to be delivered?").grid(row = 0, column = 0)

        self.ent1 = Entry(self,width = 55)
        self.ent1.grid(row = 0, column = 1, columnspan = 2)

        self.lb2 = Label(self, text="Options").grid(row = 1, column = 1,sticky = E)

        self.lb3 = Label(self, text="Delivery Method:").grid(row = 2, column = 0)

        self.lb4 = Label(self, text="Addons").grid(row = 2, column = 2)

        self.options = StringVar()
        self.options.set(None)

        Radiobutton(self, text = "Flying Drone ($10)",
            variable = self.options,
            value = "Flying Drone").grid(row = 3, column = 0)


        Radiobutton(self, text = "Self Driving Car ($20)",
            variable = self.options,
            value = "Self Driving Car").grid(row = 4, column = 0)

        Radiobutton(self, text = "Giant Robot ($1000)",
            variable = self.options,
            value = "Giant Robot").grid(row = 5, column = 0)
        
        self.delivery = BooleanVar()
        Checkbutton(self, text = "Express Delivery (+$30)", 
					variable = self.delivery).grid(row = 3, column = 2)

        self.broken = BooleanVar()
        Checkbutton(self, text = "Mostly Not Broken (+$20)", 
					variable = self.broken).grid(row = 4, column = 2)


        self.smile = BooleanVar()
        Checkbutton(self, text = "With a Smile (+$1)", 
					variable = self.smile).grid(row = 5, column = 2)
        
        self.bttn1 = Button(self, text = "Confirm Delivery", command = self.update_text)
        self.bttn1.grid(row = 6, column = 1)

        
        self.results = Text(self, width = 90, height = 5, wrap = WORD)
        self.results.grid(row = 7, column = 0, columnspan = 3)


    def update_text(self):
        """ Update text widget and display user's final cost. """
        cost = 0
        addons = []
        reply = "You have selected to have a "
        
        reply += self.ent1.get()

        reply += " delivered by "
    
        reply += self.options.get()
        if self.options.get() == "Flying Drone":
            cost += 10
        elif self.options.get() == "Self Driving Car":
            cost += 20
        else:
            cost += 1000
        
        if not(self.delivery.get() and self.broken.get() and self.smile.get()):
            reply += " with no options"
        
        if self.delivery.get():
            addons.append("with express delivery")
            cost += 30

        if self.broken.get():
            addons.append("mostly not broken")
            
            cost += 20

        if self.smile.get():
            addons.append("with a smile")
            cost += 1
        reply += " "
        reply += (", ").join(addons)
        reply += "."

        reply += " Your total delivery fee comes to: $" + str(cost)

        self.results.delete(0.0, END)
        self.results.insert(0.0, reply)


# main
root = Tk()
root.title("Robot Delivery System")
root.geometry("800x400")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
