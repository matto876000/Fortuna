f = open('Mind Flayer Names.txt')
lines = list(f)
dupes = [x for n, x in enumerate(lines) if x in lines[:n]]
print (dupes)
