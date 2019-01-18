# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names :
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# counts = dict()
# line = input('Enter line of text : ')
# words = line.split()
 
# print('Words: ', words)
# print('Counting...')

# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('Counts', counts)
