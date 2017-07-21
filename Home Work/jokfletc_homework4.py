#John Fletcher
#Homework 4


###4.13

s = 'abcdefghijklmnopqrstuvwxyz'

##a
if (s[1]+s[2]) == 'bc':
    result = "True"
else:
    result = "False"
print(result)

##b
if 'abcdefghijklmn' == s[0:14]:
    result = "True"
else:
    result = "False"
print(result)

##c
if 'opqrstuvwxyz' == s[14:26]:
    result = "True"
else:
    result = "False"
print(result)

##d
if 'bcdefghijklmnopqrstuvw' == s[1:25]:
      result = "True"
else:
    result = "False"
print(result)



###4.16(By dictionary order)

#Assign variable 'word_1' to user's first input
word_1 = input("Enter first word: ")
#Assign variable 'word_2' to user's second input
word_2 = input("Enter second word: ")
#Assign variable 'word_3' to user's third input
word_3 = input("Enter third word: ")
#Assign variable 'string' to an empty list
string = []
#Add 'append' each word to list 'string' in the order they were entered
#by the user
string.append(word_1)
string.append(word_2)
string.append(word_3)
#Create an if statement for if the order the words were inputed being the
#list 'string' is equivalent to the list sorted in alphabetical order
if string == sorted(string,key=str.lower):
#if the original list 'string' is equivalent to the sorted list 'string'
#the program prints "True"
   print("True")




   
###4.20
sender = 'tim@abc.com'
recipient = 'tom@xyz.org'
subject = 'Hello!'
#set variable 'output' to the format position of each piece of information
#and using \n for proper break positioning
output = "From: {0} \nTo: {1} \nSubject: {2}"
#print the output format using the format function and placing the varibales
#in the correct order they need to be placed in the format print statement
print(output.format(sender,recipient,subject))






###4.23 (to clarify, the function should take no arguments
###and should have an input statement within the function)

def average():
#Create variable 'num' to count the number of letters in user's
#sentence
    num = 0
#Ask the user to enter a sentence and assign it to the variable
#'string'
    string = input("Enter a sentence: ")
#assign the variable 'string' to string.split() to create a list of
#words in the string
    string = string.split()
#create for loop to run through each word in sentence
    for word in string:
#add the number of letters in the word to the variable 'num'
        num += len(word)
#assign variable 'letter_average' to num divided by number of
#words in user's sentence
    letter_average = num / len(string)
#print 'letter_average'
    print(letter_average)







###4.25
    
#create function 'vowelCount'
def vowelCount(string):

#Assign varibale 'a' to 0 to count the number of times letter
# a arises
    a = 0
#Assign varibale 'e' to 0 to count the number of times letter
# e arises
    e = 0
#Assign varibale 'i' to 0 to count the number of times letter
# i arises
    i = 0
#Assign varibale 'o' to 0 to count the number of times letter
# o arises
    o = 0
#Assign varibale 'u' to 0 to count the number of times letter
# u arises
    u = 0

#Create for loop to run through each letter in user's string 
    for letter in string.lower():
        if letter == 'a':
            a += 1
        if letter == 'e':
            e += 1
        if letter == 'i':
            i += 1
        if letter == 'o':
            o += 1
        if letter == 'u':
            u += 1
#Create output format and positioning for print statement
    output = "a, e, i, o, and u appear, respectively, {0}, {1}, {2}, {3}, {4} times."
#Use print statement and format function using variables positioned correctly
#to print output format string
    print(output.format(a,e,i,o,u))
