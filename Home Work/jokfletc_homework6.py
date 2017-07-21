#John Fletcher
#Homework 6

##6.20

#Function reverse with an arguement phonebook
def reverse(phonebook):
#phonebook_2 uses the dict function to assign x as key and y as value and then
# then assign value for key and key for value 
    phonebook_2 = dict((y,x) for x,y in phonebook.items())
    return phonebook_2

#Main
phonebook ={'Smith, Jane':'123-45-67','Doe, John':'987-65-43','Baker, David':'567-89-01'}
result = reverse(phonebook)
print('Question 6.20')
print('\n')
print(result)



##6.22

#The function mirror takes string as an arguement
def mirror(string):
#assign variable non_reverse to the list of letters that are un-reversable
    non_reverse = ['a','e']
#set string to the flipped version of the string
    string = string[::-1]
#for loop to run through flipped string
    for i in string:
#if i in string is equivalent to 'd' then replace it with 'b'
        if i == 'd':
            string = string.replace('d','b')
#if i is 'b' then replace it with 'd'
        if i == 'b':
            string = string.replace('b','d')
#if i is in the list 'non_reverse' then string is set to 'INVALID'
        if i in non_reverse:
            string = "INVALID"
            
    return string


#Main
print('-'*70)
print("Question 6.22")
print("\n")

#Book Examples
print(mirror('vow'))
print(mirror('wood'))
print(mirror('bed'))





##6.24

def names():
#dictionary to hold the names and their count of occurence
  name_dict = {}
#While loop to continuously ask for user input
  while True:
      user_input = input("Enter next name: ")
#If user enters an empty set break while loop
      if user_input == '':
          break
#elif statement for if user_input is in dictionary then
#add 1 to that key's value    
      elif user_input in name_dict:
            name_dict[user_input] = name_dict[user_input] + 1
#else statement for if name isn't in dictionary to add it with the value of 1 
      else:
          name_dict[user_input] = 1
#for loop to run through dictionary data once while loop is broken(user enters empty set)              
  for key, value in name_dict.items():
#if key's value is equivalent to 1 then print this string
      if value == 1:
          
          print("There is 1 student named "+ key)
#if key's value is greater than 1 then print this string
      else:
          print("There is "+ str(value) + ' students named ' + key)
          
                    

#Main
print('-'*70)
print("Question 6.24")
print("\n")
names()



##6.28

def translate(phrase):
#dictionary to hold tranlation values for key words
    translation_dict = {"hello":"Hallo","world":"Welt"}
#variable 'result' is set to empty to hold translated phrase
    result = ''
#split phrase into a list of it's words
    word_list = phrase.split(" ")
#for loop to run through list of phrase's words
    for word in word_list:
#if word is in dictionary add the translation to the newly translated phrase
        if word.lower() in translation_dict:
            result += translation_dict[word.lower()] + " "
        else:
#else statement for if word not in dictionary then add a dash to the new phrase
            result += "-"
            
    return result
 


#Main
print('-'*70)
print("Question 6.28")
print("\n")
#input statement for user to enter phrase
user_input = input("Enter a phrase to be translated: ")
#print the result of the translated phrase
print(translate(user_input))



##6.33

#import random to simulate a dice roll
import random
def diceprob(guess):
#variable 'rolls' will keep track of the total rolls it takes to get guess 100 times
    rolls = 0
#variable 'count' will keep track of the amount of times the guess is achieved
    count = 0
#while loop to keep running code while count does not equal 100
    while count != 100:
#variable 'roll' is eqaul to the random roll of two dice using randint ranging from
#a dices lowest possible value 2 and it's highest 12
        roll = random.randint(2,12)
#Add a roll attempt to variable 'rolls'
        rolls += 1
#if roll is equivalent to the number guessed
        if roll == guess:
#Add 1 to variable 'count'
            count +=1
#varibale result is equal to this string stating how many rolls it took to
#roll the user's guess 100 times
    result = "It took " + str(rolls) + ' to get 100 rolls of '+ str(guess)
    return result


#Main
print('-'*70)
print("Question 6.33")
print("\n")
#Examples to run function for grading purposes

print(diceprob(5))
print(diceprob(7))
print(diceprob(10))
