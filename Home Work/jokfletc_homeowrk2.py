#John Fletcher

#Homework 2

###3.19
a,b,c = 3,4,5

    ##a
# if statement, for if a is less than b it prints "OK".
if a < b:
    print("OK")
#Else statement so that when a is not less than b it prints "NOT OK"
else:
    print("NOT OK")

    ##b
# if statement, for if c is less than b it prints "OK".
if c < b:
    print("OK")
#Else statement so that when c is not less than b it prints "NOT OK"
else:
    print("NOT OK")

    ##c
# if statement, for if a plus b  is equivalent to c, it prints "OK".
if (a+b) == c:
    print("OK")
#Else statement so that when the sum of a and b is not
#equivalent to c, it prints "NOT OK"
else:
    print("NOT OK")


    ##d
# if statement, for if a squared plus b squared  is equivalent to c squared, it prints "OK".
if ((a * a) + (b * b)) == (c * c):
    print("OK")
#Else statement so that when the sum of a squared and b squared is not
#equivalent to c squared, print "NOT OK"
else:
    print("NOT OK")


###3.24
#word_list is the variable set to equal a users input with an eval function
#to handle the manual added list of words into its correct data type
word_list = eval(input("Enter  list of words: "))
#For statement to go through each word in the list
for word in word_list:
#If statement so if the word is  not equivalent to "secret",
#it will print the word
    if word != "secret":
        print(word)


###3.30
#User input numbers one through four with eval function
#so input will be handled as an integer
num_1 = eval(input("Enter first number: "))
num_2 = eval(input("Enter second number: "))
num_3 = eval(input("Enter third number: "))
num_4 = eval(input("Enter last number: "))
#if statement taking the sum of the first three numbers,dividng
#them by three to get their average and seeing if that number is
#equivalent to the fourth user input
if ((num_1 + num_2 + num_3)/3) == num_4:
#if it is equivalent print "Equal"
    print("Equal")
#Else statement so if it's not equivalent, print "Not Equal"
else:
    print("Not Equal")


###3.34
#Start by definging function as "pay" with wage and hours
#as its two arguements
def pay(wage,hours):
#if statement, for if hours worked are less than or equal to 40 hours
    if hours <= 40:
# if so pay equals wage multiplied by hours since there is no overtime
        pay = (wage*hours)
#elif statement stating else if hours are greater than 40 than...
    elif hours > 40:
# pay = wage multiplied by 40 plus the product of (wage times 1.5)
# and (hours - 40) which is the hours you worked over time
        pay = ((wage * 40) + ((wage * 1.5) * (hours - 40)))
#return the answer pay
    return pay
        
