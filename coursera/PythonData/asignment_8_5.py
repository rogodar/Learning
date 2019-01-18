fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "D:\WWW\Learning\py4e\mbox-short.txt"

fh = open(fname)
count = 0
for line in fh :
    line = line.rstrip()
    if line.startswith('From:'):
        mail = line.split()
        count +=1
        print(mail[1])
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
