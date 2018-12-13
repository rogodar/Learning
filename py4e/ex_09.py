fname = input('Enter file: ')
if len(fname) < 1 : fname = 'D:\WWW\Learning\py4e\clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

print(di)