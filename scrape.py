import requests
from bs4 import BeautifulSoup

# This program finds the pizza for the week from the cheeseboard website

url = 'http://cheeseboardcollective.coop/pizza/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

# print soup.prettify()

pizzas = soup.find("div", class_="pizza-list")

days = pizzas.find_all("article")
for day in days:
    print day.get_text()
