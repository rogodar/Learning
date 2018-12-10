# print('Exercise 6.5')
str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)
piece = str[ipos+2:]
print(piece)
value = float(piece)
print(value)
