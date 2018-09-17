import random
loop = 0
f = open('Human_Male_Names.txt') #Open name file
lines = list(f) #Write each line of the file into a list
loop = int(input("How many names would you like"))
while 0 < loop: #Number is how many names you want
    print (random.choice(lines)) #Print a random element from list
    loop -=1
