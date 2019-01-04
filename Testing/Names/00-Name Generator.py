import random
loop = 0
while loop < 1000: #Number is how many names you want
    f = open('Human Male Names.txt') #Open name file
    lines = list(f) #Write each line of the file into a list
    print (random.choice(lines)) #Print a random element from list
    loop +=1
