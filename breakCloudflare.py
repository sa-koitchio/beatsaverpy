from typing import Dict
import cloudscraper
import json

def scrape_url(url : str):
    scraper = cloudscraper.create_scraper()
    scrapedText = scraper.get(url).text
    #scrapedText = scrapedText.encode("ascii","ignore")
    #scrapedText = scrapedText.decode()
    return json.loads(scrapedText)
