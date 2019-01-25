# ofile = open('D:\WWW\Learning\py4e\mbox.txt')
# count = 0
# for line in ofile:
#     count +=1
# print('line count', count)

fhand = open('D:\WWW\Learning\py4e\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line[+6:])
