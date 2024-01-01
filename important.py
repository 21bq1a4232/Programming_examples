import csv
import requests
from bs4 import BeautifulSoup
import sys
class Scraper:
    def __init__(self):
        self.base_url = ''
    def make_request(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch data from {url}")
            return None
    def scrape_superkicks(self):
        url = 'https://superkicks.in/product-category/footwear/'
        self.base_url = 'https://superkicks.in'
        page = 1
        while True:
            data = self.make_request(url)
            if not data:
                break
            soup = BeautifulSoup(data, 'html.parser')
            products = soup.find_all('li', class_='product')
            for product in products:
                item_url = self.base_url + product.find('a')['href']
                name = product.find('h2').text.strip()
                price = product.find('span', class_='price').text.strip()
                brand = product.find('span', class_='brand').text.strip()
                sizes = product.find('span', class_='sku').text.strip()
                sku = product.find('span', class_='sku').text.strip()
                categories = product.find('span', class_='category').text.strip()
                description = product.find('div', class_='description').text.strip()
                images = product.find_all('img')
                image_urls = [self.base_url + img['src'] for img in images]
                self.write_to_csv(item_url, name, price, brand, sizes, sku, categories, description, image_urls)
            next_link = soup.find('a', class_='next page-numbers')
            if next_link:
                url = next_link['href']
                page += 1
            else:
                break
    def scrape_copunderdog(self):
        url = 'https://www.copunderdog.com/product-category/sneakers/'
        self.base_url = 'https://www.copunderdog.com'
        page = 1
        while True:
            data = self.make_request(url)
            if not data:
                break
            soup = BeautifulSoup(data, 'html.parser')
            products = soup.find_all('div', class_='product-small')
            for product in products:
                item_url = self.base_url + product.find('a')['href']
                name = product.find('h2').text.strip()
                price = product.find('span', class_='woocommerce-Price-amount').text.strip()
                brand = ''
                sizes = ''
                sku = ''
                categories = ''
                description = ''
                images = product.find_all('img')
                image_urls = [img['src'] for img in images]
                self.write_to_csv(item_url, name, price, brand, sizes, sku, categories, description, image_urls)
            next_link = soup.find('a', class_='next page-number')
            if next_link:
                url = next_link['href']
                page += 1
            else:
                break
    def write_to_csv(self, item_url, name, price, brand, sizes, sku, categories, description, image_urls):
        with open('superkicks.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([item_url, name, price, brand, sizes, sku, categories, description, ', '.join(image_urls)])
scraper = Scraper()
website = sys.argv[0].lower()
print(website)
if website == 'superkicks':
    scraper.scrape_superkicks()
elif website == 'copunderdog':
    scraper.scrape_copunderdog()
else:
    print("Invalid website name. Please provide either 'superkicks' or 'copunderdog' as the argument.")