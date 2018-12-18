fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'D:\WWW\Learning\py4e\clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

# print(di)

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)
tmp = sorted(tmp, reverse=True)
# print('Sorted', tmp)

for v,k in tmp[:6] :
    print(v,k)