# xfile = open('D:\WWW\py4e\mbox.txt')

# print mbox.txt file by lines
# for cheese in xfile:
#     print(cheese)

# counting the lines
# fhand = open('D:\WWW\py4e\mbox.txt')
# count = 0
# for line in fhand:
#     count += 1
# print("Line Count:", count)

# counting number characters
# fhand = open("D:\WWW\py4e\mbox.txt")
# inp = fhand.read()
# print(len(inp))
# printing characters from 0 to 200
# print(inp[:200])

# print line that me et criteria

fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot bre opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
Print('There were', cont, 'subject lines in', fname)
