import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())


fh = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for x in fh:
    print(x.decode().strip())