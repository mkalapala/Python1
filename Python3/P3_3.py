import urllib
from BeautifulSoup import *
import re

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
count = 0

tags = soup('span')
for tag in tags:
	x = str(tag)
	y = re.findall('[0-9]+', x)
	for num in y:
		num = int(num)
		count = count + num

print count
   