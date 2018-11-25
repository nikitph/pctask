from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from cyclonescrape.cyclonescrape.spiders.cyclone import CycloneSpider

process = CrawlerProcess(get_project_settings())
process.crawl(CycloneSpider)
process.start()