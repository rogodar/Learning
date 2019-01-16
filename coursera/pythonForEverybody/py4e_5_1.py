# 5.3 Loops and Iteration
# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in (9, 41, 12, 3, 74, 15):
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)

# print('After', largest_so_far)

# 5.4 Loops and Iteration
# zork = 0
# print('Before', zork)
# for thing in (9, 41, 12, 3, 74, 15):
#     zork +=1
#     print(zork, thing)
# print('After', zork)

# count = 0
# sum = 0
# print('Before', count, sum)
# for value in (9, 41, 12, 3, 74, 15):
#     count +=1
#     sum = sum + value
#     print(count, sum, value)
# print('After :', count, sum, sum / count)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)
    
    try:
        fnum = int(num)
        # for lvolue in fnum :
        if largest is None:
            largest = fnum
        elif fnum > largest:
            largest = fnum
        # for svolue in fnum :
        if smallest is None:
            smallest = fnum
        elif fnum < smallest:
            smallest = fnum
        
    except:
        print('bad input')
        continue
print('Minimum', smallest)
print("Maximum", largest)
# print(fnum)