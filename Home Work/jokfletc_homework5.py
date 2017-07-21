#John Fletcher
#Homework 5


### 5.29
#Define the function as 'lastfirst' to take an argument 'lst'
def lastfirst(lst):
#Using list comprehension assgin a list 'names' split each group of names with a comma
#Then strip each of the name groupings
    name_list = [[name.strip() for name in names.split(",")] for names in lst]
#Using list comprehension again assign a list 'first_last' to have two embedded list
#the first embedded list will take the first name from each group while the second takes
#embedded list takes the second name from each grouping
    first_last = [[name[1] for name in name_list],[name[0] for name in name_list]]
#return the list 'first_last'
    return first_last


#Main
#Assign the variable 'result' to call the function 'lastfirst' to this string of names
result = lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob'])
print("Question 5.29")
print('\n')
#print the return results to the user
print(result)
print('\n')
print("-"*50)




# 5.39
#Define the function as 'exclamation' taking an arguement 'user_string'
def exclamation(user_string):
#assign a variable 'string' to be empty for now to be later assigned the new string
    string = ""
#Assign the variable 'vowels' to a list of vowels
    vowels = ["a", "e", "i", "o", "u"]
#Using a for loop to run through each letter in the string provided by the user
    for letter in user_string:
# If statement for if the letter is in the list 'vowels'
        if letter in vowels:
#variable 'string' will be added that letter times (*) 4
            string+=letter*4
        else:
#else if letter not in 'vowels' the letter is added to 'string' once
            string+=letter
#At the end of the for loop and the string is finished an exclamation
#point is added on the end of 'string'
    string+="!"
#return 'string'
    return string


#Main

print("Question 5.39")
print('\n')
#print out the results of the function 'exclamation'
print(exclamation("argh"))
print(exclamation("hello"))
print("-"*50)






# 5.43
#Define a function as 'evenrow' that takes an arguement 'integer_lst'
def evenrow(integer_lst):
#assign a variable 'count' to zero to add the numbers in each row
    count = 0
#Use a for loop too run through each row in the integer_lst
    for row in integer_lst:
#Use another for loop to run through the integers in each row of the integer_lst
        for integer in row:
#Add the integer in each row to the variable 'count'
            count += integer
#If the division of the sum of the row is not zero when divided by two
    if not count % 2 == 0:
#The function will return False
        return False
#If the count is even the function will return True
    return True

#Main

print("Question 5.43")
print("\n")
#Print the results of the function call to 'evenrow'
print(evenrow([[1,3],[2,4],[0,6]]))
print(evenrow([[1,3,2],[3,4,7],[0,6,2]]))
print(evenrow([[1,3,2],[3,4,7],[0,5,2]]))
