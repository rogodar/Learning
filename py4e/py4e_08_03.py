# abc = 'With three words'
# stuff = abc.split()
# for i in stuff:
#     print(i)
# print(stuff)
# print(len(stuff))
# print(stuff[0])

fhand = open('D:\WWW\Learning\py4e\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[1])

# numlist = list()
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average: ', average)
