for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print ("Fizzbuzz")
        continue
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)

for i in range(10):
    print (i)

for num in [100, 200, 300]:
    print (num)

for key, value in {'a': 1, 'b': None, 'c': True, 'd': [1,2,3]}.items():
    print (f"Key --> {key} : value -->{value}") 

for i, num in enumerate([100, 200, 300]):
    print (i, num)

num = 1
while num < 101:
    if num % 3 == 0 and num % 5 == 0:
        print ("Fizzbuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
    num += 1

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        continue
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)

num = 1
while num < 101:
    if num % 3 == 0 and num % 5 == 0:
        print ("Fizzbuzz")
        break 
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
    num += 1

even_numbers = [num for num in range(1, 101) if num % 2 == 0]

import string 
alphabet_dict = {number: alphabet for number, alphabet in zip(range(26), string.ascii_lowercase)}

