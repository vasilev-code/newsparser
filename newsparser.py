import requests
from bs4 import BeautifulSoup

url = 'https://hackware.ru/'

response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

hackware_titles_box = []
hackware_links_box = []
links = soup.find_all('a',{'class':'read-more'})
title = soup.find_all('h3',{'class':'ftitle'})
for link in links:
    hackware_links_box.append(link['href'])

for titles in title:
    hackware_titles_box.append(titles.text)

for title_index,title_value in enumerate(hackware_titles_box):
    for link_index,link_value in enumerate(hackware_links_box):
        if title_index != link_index:
            continue
        else:
            print(title_value,link_value)