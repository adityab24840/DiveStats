from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from diving_scraper.diving_scraper.spiders.diving import DivingSpider

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(DivingSpider)
    process.start()

