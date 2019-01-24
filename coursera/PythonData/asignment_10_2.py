# 10.2 Write a program to read through the mbox-short.txt and figure out 
# the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1:
    name = "D:\WWW\Learning\py4e\mbox-short.txt"
fh = open(name)
mbox = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        mail = line.split()
        x = (mail[5])
        x = x.split(':')
        y = x[0]
        mbox[y] = mbox.get(y, 0) + 1
    else:
        continue
mlist = list()
print(sorted([(k,v) for k,v in mlist.items()]))
# for k,v in mbox.items():
#     mh = (k,v)
#     mlist.append(mh)
# mlist = sorted(mlist)
# for k,v in mlist:
#     print(k,v)
