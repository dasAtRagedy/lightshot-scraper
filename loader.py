import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup

if not os.path.exists('i.imgur.com'):
    os.makedirs('i.imgur.com')

if not os.path.exists('image.prntscr.com'):
    os.makedirs('image.prntscr.com')

myPath1 = os.getcwd()+"\\i.imgur.com"
myPath2 = os.getcwd()+"\\image.prntscr.com"

print(myPath1)
print(myPath2)


stringletters = "qwertyuiopasdfghjklzxcvbnm1234567890"
firstletters = input("First 4 letters: ")
opener = urllib.request.build_opener()
opener.addheaders = [
    (
        "User-Agent",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    )
]
urllib.request.install_opener(opener)
for a in stringletters:
	for e in stringletters:
		url = 'https://prnt.sc/'
		url = url + firstletters + a + e
		print(url)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
		page = requests.get(url, headers=headers)
		contents = page.content

		soup = BeautifulSoup(contents, 'html.parser')
		link = soup.find_all('a')
		#print(link)
		#print (link[34])
		sphere = str(link[33])
		sphere = sphere.replace('<a href="http://www.google.com/searchbyimage?image_url=', '')
		sphere = sphere.replace('"><i class="icon-camera"></i><strong>find similar</strong></a>', '')
		print(sphere)

		if "https://i.imgur.com/" in sphere:
			filename = sphere.replace('https://i.imgur.com/', '')
			
			fullfilename = os.path.join(myPath1, filename)
			print(fullfilename)

			try:
				urllib.request.urlretrieve(sphere, fullfilename)
			except:
				print("Exception: Forbidden")
		
		if "image.prntscr.com" in sphere:
			filename = sphere.replace('https://image.prntscr.com/image/', '')
			
			fullfilename = os.path.join(myPath2, filename)
			print(fullfilename)

			try:
				urllib.request.urlretrieve(sphere, fullfilename)
			except:
				print("Exception: Forbidden")