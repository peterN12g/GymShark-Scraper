import json
import requests
from bs4 import BeautifulSoup
import os

def product_scrape():
    url = 'https://www.gymshark.com/collections/outlet/mens?collections=shorts&features=zip+pocket'
    response = requests.get(url)
    products = []
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    main_product = soup.find_all('article', class_='product-card_product-card__gB8_b')
    
    def footer_product(product):
        parent_ul = product.find_parent('ul', class_='carousel_carousel__P18iO')
        return parent_ul is not None
    
    filter_main_products = [product for product in main_product if not footer_product(product)]
    
    for product in filter_main_products:
        title_tag = product.find('a', class_='product-card_product-title-link__7fUTe')
        if title_tag:
            title = title_tag.get('title')
        else:
            title = 'Title not found'
        
        link_tag = product.find('a', class_='product-card_product-title-link__7fUTe')
        if link_tag:
            link = link_tag.get('href')
        else:
            link = 'Link not found'
        
        color_tag = product.find('p', class_='product-card_product-colour__JApvJ')
        if color_tag:
            color = color_tag.text.strip()
        else:
            color = 'Color not found'
        
        price_container = product.find('div', class_='product-card_price-container__9HpcE')
        if price_container:
            price_tag = price_container.find('span', class_='product-card_product-price__bNBmg')
            if price_tag:
                price = price_tag.text.strip()
                price = float(''.join(filter(str.isdigit, price))) / 100
            else:
                price = 'Price not found'
            
            compare_price_tag = price_container.find('span', class_='product-card_compare-at-price__2MQSu')
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
    scraped_products = product_scrape()