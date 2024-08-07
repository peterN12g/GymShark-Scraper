import json
import requests
from bs4 import BeautifulSoup
import os

def product_scrape():
    url = 'https://www.gymshark.com/collections/outlet/mens?collections=shorts&activities=lifting'
    response = requests.get(url)
    products = []
    soup = BeautifulSoup(response.content, "html.parser")

    main_product = soup.find_all('article',class_=['product-card_product-card__gB8_b', 'product-card_product-card__CIqIf'])

    for product in main_product:
        title_tag = product.find('a', class_='product-card_product-title-link__jDI6f')
        if title_tag:
            title = title_tag.get('title')
        else:
            title = 'Title not found'

        link_tag = product.find('a', class_='product-card_product-title-link__jDI6f')
        if link_tag:
            link = link_tag.get('href')
        else:
            link = 'Link not found'
        
        color_tag = product.find('p', class_='product-card_product-colour__94Hbd')
        if color_tag:
            color = color_tag.text.strip()
        else:
            color = 'Color not found'
        
        price_container = product.find('div', class_='product-card_price-container__hHyGb')
        if price_container:
            price_tag = price_container.find('span', class_='product-card_product-price__VOOyf product-card_product-price--sale__G6M00')
            if price_tag:
                price = price_tag.text.strip()
                price = float(''.join(filter(str.isdigit, price))) / 100
            else:
                price = 'Price not found'
            
            compare_price_tag = price_container.find('span', class_='product-card_compare-at-price__Fq3Vl')
            if compare_price_tag:
                compare_price = compare_price_tag.text.strip()
                compare_price = float(''.join(filter(str.isdigit, compare_price))) / 100
            else:
                compare_price = 'Compare price not found'
                    
        if title_tag and color_tag and price_container and link_tag:
            name = title + ' ' + color
            discount_percentage = 100 - ((price/compare_price))
            discount = f"{discount_percentage:.0f}% off"
            source = link


            products.append({
                'title': name,
                'price': price,
                'discount': discount,
                'source': source 
            })
        
    return products

if __name__ == "__main__":
    # scrape_and_notify()
    scraped_products = product_scrape()