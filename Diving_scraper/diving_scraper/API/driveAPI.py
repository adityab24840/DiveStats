from flask import Flask
from flask_restful import Api, Resource
from scrapy.crawler import CrawlerProcess
import sys
sys.path.append(r'D:\DiveStats\Diving_scraper')  # Add the correct path to your project

from diving_scraper.diving_scraper.spiders.diving import DivingSpider

app = Flask(__name__)
api = Api(app)

def run_spider():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
    process.crawl(DivingSpider)
    process.start()

class ScrapeResource(Resource):
    def get(self):
        run_spider()
        return {"message": "Scraping completed successfully!"}

api.add_resource(ScrapeResource, '/scrape')

if __name__ == '__main__':
    app.run(debug=True)
    