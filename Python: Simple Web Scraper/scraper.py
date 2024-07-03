# scraper.py
import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h2')
    for title in titles:
        print(title.get_text())

if __name__ == "__main__":
    url = "https://example.com"
    html = get_html(url)
    parse_html(html)