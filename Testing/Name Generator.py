import random
loop = 0
while loop < 1:
    f = open('Human Male Names.txt')
    lines = list(f)
    print (random.choice(lines))
    loop +=1
