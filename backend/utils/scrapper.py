import requests
from bs4 import BeautifulSoup
import os, json

class Scraper:
    def __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path

    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status()   
        return response.text

    def parse_countries(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        countries = soup.find_all('div', class_='col-md-4 country')
        
        data = []
        for country in countries:
            name = country.find('h3', class_='country-name').get_text(strip=True)
            capital = country.find('span', class_='country-capital').get_text(strip=True)
            population = country.find('span', class_='country-population').get_text(strip=True)
            area = country.find('span', class_='country-area').get_text(strip=True)
            
            country_data = {
                'name': name,
                'capital': capital,
                'population': population,
                'area': area
            }
            data.append(country_data)
            # print(country_data)
        return data

    def save_to_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(data))

    def scrape_and_store(self):
        html_content = self.fetch_page()
        data = self.parse_countries(html_content)
        # self.save_to_file(data)
        return data
