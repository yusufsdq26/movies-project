import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url=url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

image = og_image['content']
title = og_title['content']
desc = og_description['content']

print(image)
print(title)
print(desc)