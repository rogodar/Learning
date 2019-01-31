# ------- Normal Program --------------------------
# hand = open('D:\WWW\Learning\py4e\mbox-short.txt')
# for line in hand:
#         line = line.rstrip()
#         if line.find('From:') >= 0:
#                 print(line)

# ------- Program using RE ------------------------
# import re

# hand = open('D:\WWW\Learning\py4e\mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line) :
#         print(line)

# -------------------------------------------------
# ------- Normal Program --------------------------
# hand = open('D:\WWW\Learning\py4e\mbox-short.txt')
# for line in hand:
#         line = line.rstrip()
#         if line.startswith('From:') :
#                 print(line)

# ------- Program using RE ------------------------
import re

hand = open('D:\WWW\Learning\py4e\mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)

# --------------------------------------------------
