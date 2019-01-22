import re
hand = open('D:\WWW\Learning\py4e\mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From (\S+@\S+)', line)
    if len(x) > 0:
        print(x)
