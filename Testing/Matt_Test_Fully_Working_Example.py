import random
namenum = int(input("how many characters?")) #taking numeric input
while namenum > 0: #runs as many times as the input due to line 5
    print(random.choice(list(open('Matt_Test_Names.txt')))) #printing a random name
    namenum = namenum -1
