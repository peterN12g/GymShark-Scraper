import requests
from bs4 import BeautifulSoup
import http.client, urllib
from dotenv import load_dotenv
import os

url = "https://www.gymshark.com/products/gymshark-react-5-short-black-ss23"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

load_dotenv()
USER_TOKEN = os.environ.get('USER_TOKEN')
API_KEY = os.environ.get('API_KEY')

#Finding Product Information from HTML
title_tag = soup.find("title")
name = title_tag.text if title_tag else "Name not found"
print(f"Product Name: {name}")

meta_tag = soup.find("meta", attrs={"name": "twitter:data1"})
price = meta_tag["content"] if meta_tag else "Price not found"
curr_price = 36
#remove $ from price to convert int
priceConv = ''.join(c for c in price if c.isdigit() or c == '.')
priceInt = int(priceConv)
print(f"Product Price: {price}")
if priceInt is not None and priceInt < curr_price:
    #Use Pushover app for Push Notifications
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "USER_TOKEN",
        "user": "API_KEY",
        "message": f"Price drop: {name} - {price}!",
    }), { "Content-type": "application/x-www-form-urlencoded" })
    response = conn.getresponse()



