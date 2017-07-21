#2.11
#a
num = sum(range(-7,0))
print(num)


#b
total = (17*9)+(24*10)+(21*11)+(27*12)
kids = 17+24+21+27
average = total/kids
print(round(average,1))


#c
num = 2**-20
print(num)


#d
num = 4356//61
print(num)


#e
num = 4356%61
print(num)


#2.14

s = 'goodbye'

#a
letter_a = s[0]
print(letter_a == 'g')

#b
letter_b = s[6]
print(letter_b == 'g')

#c
letter_c = s[0:2]
print(('g'and 'a') in letter_c)

#d
print(s[len(s)-2] == 'x')

#e
print(s[3] == 'd')

#f
print(s[0] == s[6])

#g
print(s[3:7] == 'tion')


#2.16
#a
a=6
b=7

#b
c = (a+b)/2
print(c)

#c
inventory = ['paper','staples','pencils']

#d
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'

#e
fullname = first+ ' '+middle+' '+last
print(fullname)

#2.17
#a
num = (-9+17)
print(num < 10)

#b
print((len(inventory)) > (5*len(fullname)))

#c
print(c <= 24)

print(a < 6.75 < b)

#d
mid = len(middle)
fir = len(first)
las = len(last)

print((mid > fir) and (mid < las))

#f
amount = len(inventory)
print((amount == 0) or (amount == 10))


#2.18
#a

flowers = ['rose','bougainvillea', 'yucca', 'marigold', 'daylilly ','lilly of the valley']

#b
print('potato' not in flowers)

#c
thorny = flowers[0:3]

#d
poisonous = [flowers[-1]]

#e
print(poisonous)
print(thorny)
dangerous = thorny + poisonous
print(dangerous)

#2.22
lst = [3,7,-2,12]
num_max = max(lst)
num_min = min(lst)
num = abs(num_max)+abs(num_min)
print(num)


#2.28
#a
print(int((len(lst)/2)))

#b
print(lst[int((len(lst)/2))])

#c
print(sorted(lst, reverse = True))

#d
print(lst[1:]+[lst[0]])
