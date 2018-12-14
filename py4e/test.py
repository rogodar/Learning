import re

# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+' ,x)
# print(y)

# x = 'From: Using the : character'
# y = re.findall('F.+?:', x)          # adding '?' makes it not greedy and desplays only first character till ':'
# print(y)

# Extract email from string 
# x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('\S+@\S+' ,x)            # Match '@' and get all to the left and right till white space
# print(y)

# Extract email from string that starts with "From"
x = open('E:\Learning\WEB\Learning\py4e\mbox-short.txt')
counts = dict()
for line in x:
    words = line.rstrip()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
y = re.findall('^From (\S+@\S+)' ,x)            
print(y)