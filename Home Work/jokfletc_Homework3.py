#John Fletcher
#Homework 3

###3.20
lst = ["January","February","March"]
for i in lst:
    print(i[0] + i[1] + i[2])


###3.25

students = eval(input("Enter a list of students: "))
["Ellie","Steve","Sam","Owen","Gavin"]
for i in students:
    if i[0].upper() in "ABCDEFGHIJKLM":
        print(i)


###3.41

def lastF(FirstName,LastName):
    name = LastName + " , " + FirstName[0] + "."
    return name



####3.44

def distance(time):
    kilometers = (340.29 * time) / 1000
    return kilometers


import random
###Random Cinema

def movie(words):
    title = random.choice(words) + " " + random.choice(words) + " " + random.choice(words)
    return title



#main
lst = eval(input("Please enter a list of words: "))
number = eval(input("Please enter a number of movies you'd like to generate: "))
print("Welcome to Randoplex! Currently playing movies are: ")

for i in range(number):
    result = movie(lst)
    print(result)
