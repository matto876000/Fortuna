import random
namenum = int(input("how many characters?"))
while namenum > 0:
    print(random.choice(list(open('Matt_Test_Names.txt'))))
    namenum = namenum -1
    
