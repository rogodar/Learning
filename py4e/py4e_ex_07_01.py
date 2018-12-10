fname = input('Write file to be opened: ')
try:
    fhand = open(fname)
except:
    print('File', fname, 'cannot be opened: ')
    quit
for line in fhand:
    print(line.capitalize)
