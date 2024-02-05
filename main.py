import os
import json
import requests
from bs4 import BeautifulSoup
import http.client
import urllib

API_TOKEN = os.environ.get("API_TOKEN")
USER_KEY = os.environ.get("USER_KEY")

def send_notification(name, price):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": API_TOKEN,
                     "user": USER_KEY,
                     "message": f"Price drop: {name} - {price}!",
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()
    print(f"Notification response: {response.status} - {response.reason}")

def lambda_handler(event, context):
    url_black_shorts = "https://www.gymshark.com/products/gymshark-react-5-short-black-ss23"
    req_black_shorts = requests.get(url_black_shorts)
    soup_black_shorts = BeautifulSoup(req_black_shorts.content, "html.parser")

    # Finding Product Information from HTML
    title_tag = soup_black_shorts.find("title")
    name_black_shorts = title_tag.text if title_tag else "Name not found"

    meta_tag = soup_black_shorts.find("meta", attrs={"name": "twitter:data1"})
    price_black_shorts = meta_tag["content"] if meta_tag else "Price not found"
    curr_price_black_shorts = 25.2
    target_price_black_shorts = (curr_price_black_shorts - 25.2 * 0.25)
    priceConv_black_shorts = ''.join(c for c in price_black_shorts if c.isdigit() or c == '.')
    
    try:
        priceFloat_black_shorts = float(priceConv_black_shorts)
        priceInt_black_shorts = int(round(priceFloat_black_shorts))
    except ValueError:
        print(f"Could not convert {priceConv_black_shorts} to a number.")
        return
    
    if priceInt_black_shorts is not None and priceInt_black_shorts < target_price_black_shorts:
        send_notification(name_black_shorts, price_black_shorts)
        print("Notification sent!")

if __name__ == "__main__":
    lambda_handler(None, None)
