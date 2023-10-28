import requests
from bs4 import BeautifulSoup
import pandas as pd
data = []
response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select(".main_pack")
# print(posts)
for post in posts:
    title = post.select_one(".sub_tit").text
    data.append([title])
print(data)

