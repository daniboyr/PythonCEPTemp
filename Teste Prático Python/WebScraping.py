from bs4 import BeautifulSoup
import requests

page = requests.get("https:google.com")

soup = BeautifulSoup(page.content, "html.paser")

for meta in soup.head:
