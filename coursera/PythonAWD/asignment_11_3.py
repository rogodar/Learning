import re
fhand = open('D:\WWW\Learning\coursera\PythonAWD\regex_sum_148678.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    numex = re.findall('', line)
    num = int(numex[0])
    numlist.append(num)

print('The sum is : ', sum(numlist))