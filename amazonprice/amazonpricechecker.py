import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.in/BATA-Jorah-Formal-Shoes-8-8216017/dp/B079R8JWH8/ref=sr_1_1_sspa?crid=1SMS0M4ZJAB8K&keywords=formal+shoes+for+men&qid=1573122191&sprefix=formal+sho%2Caps%2C371&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVVNOWjg2S0xRQTNGJmVuY3J5cHRlZElkPUEwNTE0NjkwUVo0SThUV0MxMVZNJmVuY3J5cHRlZEFkSWQ9QTAwMjMyODMzVVBGVEw3Qko2Qk1KJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='


headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

page = requests.get(URL,headers=headers)


soup=BeautifulSoup(page.content,"html.parser")


title = soup.find(id="productTitle")  

print(title)