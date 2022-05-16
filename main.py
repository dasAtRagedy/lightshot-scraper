import os
import string
import requests
import urllib.request
from bs4 import BeautifulSoup

save_dir = 'saved'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
local_path = os.getcwd()

base_url = 'https://prnt.sc/'

opener = urllib.request.build_opener()
opener.addheaders = [(
        'User-Agent',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    )]
urllib.request.install_opener(opener)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

possibilities = string.ascii_lowercase + string.digits
input_first = input('Random 4 letters and/or digits:')

for i in possibilities:
    for j in possibilities:
        full_url = base_url + input_first + i + j

        page_content = requests.get(full_url, headers=headers).content

        soup = BeautifulSoup(page_content, 'html.parser')
        link = soup.select_one('img#screenshot-image')
        link = str(link)[135:-3]

        file_name = link.replace('https://i.imgur.com/', '').replace('https://image.prntscr.com/image/', '')
        full_path = os.path.join(local_path, save_dir, file_name)
        
        print(link)
        #print(full_path)

        try:
            urllib.request.urlretrieve(link, full_path)
        except:
            print('Exception: Forbidden')