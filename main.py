import json
import requests
from bs4 import BeautifulSoup
import http.client
import urllib
from dotenv import load_dotenv
import os

load_dotenv()
USER_TOKEN = os.environ.get('USER_TOKEN')
API_KEY = os.environ.get('API_KEY')

def send_notification(name, price):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": API_KEY,
                     "user": USER_TOKEN,
                     "message": f"Price drop: {name} - {price}!",
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()

def scrape_and_notify():
    url_black_shorts = "https://www.gymshark.com/products/gymshark-react-5-short-black-ss23"
    req_black_shorts = requests.get(url_black_shorts)
    soup_black_shorts = BeautifulSoup(req_black_shorts.content, "html.parser")

    # Finding Product Information from HTML
    title_tag = soup_black_shorts.find("title")
    name_black_shorts = title_tag.text if title_tag else "Name not found"

    meta_tag = soup_black_shorts.find("meta", attrs={"name": "twitter:data1"})
    price_black_shorts = meta_tag["content"] if meta_tag else "Price not found"
    curr_price_black_shorts = 36
    target_price_black_shorts = (curr_price_black_shorts - 36 * 0.25)
    # remove $ from price to convert int
    priceConv_black_shorts = ''.join(c for c in price_black_shorts if c.isdigit() or c == '.')
    priceInt_black_shorts = int(priceConv_black_shorts)

    if priceInt_black_shorts is not None and priceInt_black_shorts < target_price_black_shorts:
        send_notification(name_black_shorts, price_black_shorts)
        print("Notification sent!")

if __name__ == "__main__":
    scrape_and_notify()
