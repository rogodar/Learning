fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Bad file name', fname)
    quit
for x in fhand:
    x = x.rstrip()
    y = x.upper()
    print(y)