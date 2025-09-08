# Python Web Scraping (BeautifulSoup, Scrapy)

```python
# Using BeautifulSoup
from bs4 import BeautifulSoup
import requests

# Get HTML content
url = "https://www.example.com"
response = requests.get(url)
html = response.text

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Find elements
title = soup.title.text
print("Title:", title)

# Find all links
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# Find element by id
element = soup.find(id="main")
print(element)

# Find elements by class
items = soup.find_all(class_="item")
for item in items:
    print(item.text)

# Scrapy example (simplified, run in Scrapy project)
# import scrapy
# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     start_urls = ["https://www.example.com"]
#     def parse(self, response):
#         for title in response.css("h2::text"):
#             yield {"title": title.get()}
