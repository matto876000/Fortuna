import random
import math
Race = ['Aarakocra', 'Dragonborn', 'Drow', 'Dwarf', 'Elf', 'Gnoll', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Kenku', 'Kobold', 'Lizardfolk', 'Mind Flayer', 'Minotaur', 'Orc', 'Tiefling', 'Yuan-ti']
Race = ['Human']
Gender = ['Male', 'Female']
Character_Race = (random.choice(Race))
print (Character_Race)
if Character_Race == "Human":
    fHuman = open('Names/Human Male Names.txt')
    HumanLines = list(fHuman)
    print (random.choice(HumanLines))
    RawAge = random.betavariate(2.25,4.2)
    RawAge = (RawAge*100)
    Age = round (RawAge)
    print (Age)
    
