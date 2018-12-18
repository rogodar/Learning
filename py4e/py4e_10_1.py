# 10.1 - Tuples 

# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k,v) in d.items():
#     print(k,v)

# tups = d.items()
# print(tups)

# 10.2 - Sorting Lists of Tuples

# d = {'a':10, 'b':1, 'c':22}

# t = sorted(d.items())
# print(t)
# for k,v in sorted(d.items()):
#     print(k, v)

# The top 10 most common words

# fhand = open('E:\Learning\WEB\Learning\py4e\mbox-short.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     if not line.startswith('From') : continue
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# # lst = list()
# for key,val in sorted(counts.items()):
#    print(key,' : ',val)
# #     newtup = (key, val)
# #     lst.append(newtup)
# # lst = sorted(lst)
# # print(lst)

<<<<<<< HEAD
fhand = open("D:\WWW\Learning\py4e\clown.txt")
=======
fhand = open('E:\Learning\WEB\Learning\py4e\mbox-short.txt')
>>>>>>> 7e50da4d825fd8f6c4d9aa19f3cd7dcf5e1fe08c
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

<<<<<<< HEAD
lst = list()                            #       Shorter version for these lines:
for key,val in counts.items():          #       print(sorted([(v, k) for k, v in counts.items()]))
    newtup = (val, key)                 #
    lst.append(newtup)                  #

lst = sorted(lst, reverse=True)         #
for val, key in lst:                    #
        print(key,val)                  #

=======
lst = list()
for key,val in counts.items():
        print(key,' : ',val)
        newtup = (key, val)
        lst.append(newtup)
lst = sorted(lst)
print(lst)
>>>>>>> 7e50da4d825fd8f6c4d9aa19f3cd7dcf5e1fe08c
