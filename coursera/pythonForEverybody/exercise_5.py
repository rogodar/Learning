# Assignment 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

tot = 0.0
count = 0
while True:
    en = input('Enter number :')
    if en == 'done':
        break
    try:
        fen = float(en)
    except:
        print('Bad value')
        continue
    print(fen)
    count +=1
    tot = tot + fen

print('Numbers: ',count,'Total value: ',tot,'Average value: ',tot/count)
