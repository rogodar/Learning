# The program will use urllib to read the HTML from the data files below, 
# and parse the data, extracting numbers and compute the sum of the numbers in the file.

# Data Format
# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:
# <tr > <td > Modu < /td > <td > <span class = "comments" > 90 < /span > </td > </tr >
# <tr > <td > Kenzie < /td > <td > <span class = "comments" > 88 < /span > </td > </tr >
# <tr > <td > Hubert < /td > <td > <span class = "comments" > 87 < /span > </td > </tr >

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
