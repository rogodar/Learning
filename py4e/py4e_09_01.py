# py4e - 9.2
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names :
#     if name not in counts:
#         counts[name] = 1
#     else :
#         counts[name] = counts[name] + 1
## Four up rows can be changed with one line with method .get
## The whole loop can be changed with this line
# counts[name] = counts.get(name, 0) + 1
# print(counts)

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names :
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# py4e - 9.3
 
# make an empty dictionary
counts = dict()     
print('Enter a line of text: ')
line = input('')
# splits the text in words based on empty spaces
words = line.split()    

print('Words: ', words)

print('Counting...')
# Loop
for word in words:         
# check if word exists in dictionary and if not - adds it with default value; if yes then adds +1
    counts[word] = counts.get(word, 0) + 1     
print('Counts', counts)

