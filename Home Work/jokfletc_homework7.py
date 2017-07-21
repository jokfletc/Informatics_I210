#John Fletcher
#Homework 7


#8.20

class BankAccount(object):

   
#constructor set amount to equal None so function can handle if arguement is
#not entered
    def __init__(self,amount=None):
#if statement so if arguement isn't entered amount equals zero
        if amount == None:
            amount = 0
#self.amount equals amount with a float so cents can be calculated        
        self.amount=float(amount)
#withdraw function will subtract amount value from self.amount
    def withdraw(self,amount):
        self.amount-=float(amount)
#add amount arguement to self.amount
    def deposit(self,amount):
        self.amount+=float(amount)
#return the balance by rounding the float value of self.amount to two decimals
    def balance(self):
        balance = round(self.amount,2)
        return balance
#Main
print("\n")        
print("\n")
print("Problem 8.20")
print("-"*70)


x = BankAccount(700)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(7)
print(x.balance())



#8.22

class Worker(object):
#self.name equals name
#self.rate equals rate
    def __init__(self,name,rate):
        self.name = name

        self.rate = rate
#to change rate to the new rate set self.rate equal to new_rate
    def changeRate(self,new_rate):
        self.rate = new_rate
#If the worker isn't classified as salary or hourly the program will print
# "Not Implemented"
    def pay(self,hours):
        print("Not Implemented")
#Create class for hourly worker 
class HourlyWorker(Worker):
#pay function is passed to this if classified as hourly
    def pay(self,hours):
#pay equals to hours times self.rate if worker works 40 hours or less            
        if hours <= 40:
            p1 = hours * self.rate
#else if worker works more than 40 hours then any time over 40 is times by 2
#and times the self.rate
        else:
            p1 = hours * self.rate
            p1 += ((hours - 40)*2) * self.rate
#print the workers pay
        print(p1)
        

#Create class for salaried worker    
class SalariedWorker(Worker):
#if worker is classified as salary worker the pay function is passed to here
    def pay(self,hours = 40):
#salary workers automatically are set to 40 hours because they are
#paid the same no matter hours worked
        hours = 40
#Pay is equal to self.rate times hours        
        p2 = self.rate * hours
#print pay
        print(p2)

        
print("\n")        
print("\n")
print("Problem 8.22")
print("-"*70)


w1=Worker('Joe',15)
w1.pay(35)

w2=SalariedWorker('Sue',14.50)
w2.pay()
w2.pay(60)

w3=HourlyWorker('Dana',20)
w3.pay(25)
w3.changeRate(35)

w3.pay(25)


    
#8.35
#Create class Stack
class Stack(object):
#Create list self.items to hold items as a container 
    def __init__(self):
        self.container = []
#create function to deliver length of list
    def __len__(self):
        return len(self.container)
        
        
#function to put item into self.container
    def push(self,item):
#append adds item to self.container
        self.container.append(item)
#pop function removes last item to be added to self.container
    def pop(self):
#uses .pop() to achieve this removal
        item_pop = self.container.pop()
#returns the value of the item in self.container removed
        return item_pop
#string function to return the self.container list
    def __str__(self):
        return str(self.container)
# isEmpty function to return the boolean value True or False if
#self.container is an empty list '[]'
    def isEmpty(self):
        return self.container == []
print("\n")        
print("\n")
print("Problem 8.35")
print("-"*70)


s = Stack()
s.push('plate 1')
s.push('plate 2')
s.push('plate 3')
print(s)
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())





#8.40
class BankAccount(object):

    

    def __init__(self,amount=None):
#Just like the original 8.20 problem if user doesn't enter value for
#amount arguement then amount is set to zero
        if amount == None:
            amount = 0
#try statement to see if amount is negative using less than zero
#if it is negative then ValueError is raised
        try:
            
            if amount < 0:
                raise ValueError
#Else If amount is not negative then self.amount equals the amount with float to
#account for cents
            else:
                self.amount = float(amount)
#If ValueError is passed print 'Illegal Balance
        except ValueError:
            print("Illegal Balance")
            
    def withdraw(self,amount):
        try:
#If withdraw amount is greater than the current balance(self.amount)
#then raise the ValueError
            if amount > self.amount:
                raise ValueError
#else balance(self.amount) has function's amount subtracted from it
            else:
                self.amount -= float(amount)
#if ValueError is raised the program prints 'Overdraft'
        except ValueError:
            print("Overdraft")

    def deposit(self,amount):
        try:
#If deposit amount is negative or less than zero the ErrorValue is raised
            if amount < 0:
                raise ValueError
#else self.amount has the function's amount added to it for the
#bank account's balance
            else:
                self.amount += amount
#if ValueError is raised then 'Negative deposit' is printed
        except ValueError:
            print("Negative deposit")
        

    def balance(self):
#balance equals the rounding of self.amount to two decimals
        balance = round(self.amount,2)
#return the balance
        return balance

print("\n")        
print("\n")
print("Problem 8.40")
print("-"*70)


x = BankAccount(50)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(-7)
print(x.balance())
 


