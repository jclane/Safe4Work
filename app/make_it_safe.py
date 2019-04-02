import requests
import html2text
from bs4 import BeautifulSoup


def make_it_safe(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, features="html.parser")
    article = soup.find(id="article") or soup.find("div", class_="article") or soup.find("article")
    return html2text.html2text(article)


