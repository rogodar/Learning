import re

file = open('D:\WWW\Learning\coursera\PythonAWD\\regex_sum_148678.txt')
numlist = list()

for line in file:
    line = line.rstrip()
    line = re.findall('([0-9]+)', line)
    for i in line:
        i = int(i)
        numlist.append(i)

print(sum(numlist))