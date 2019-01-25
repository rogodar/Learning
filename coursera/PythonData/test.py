fh = input('Enter file: ')
if len(fh) < 1 :
    fh = "D:\WWW\Learning\py4e\mbox-short.txt"
handle = open(fh)


mailbox = dict()
for inmail in handle :
    inmail = inmail.rstrip()
    if inmail.startswith('From '):
        x = inmail.split()
        y = (x[5])
        y = y.split(':')
        z = (y[0])
        mailbox[z] = mailbox.get(z, 0) + 1
    else:
        continue
ls = list()
for k,v in mailbox.items():
    mtime = (k,v)
    ls.append(mtime)
ls = sorted(ls)
for k,v in ls:
    print(k,v)
        
        
# .........................
