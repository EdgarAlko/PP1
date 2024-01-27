import scrapy
import time
import logging

logging.basicConfig(
    filename='main.log',
    level=logging.DEBUG,
    format='%(asctime)s : %(message)s'
)

class CvbankasSpider(scrapy.Spider):
    name = "cvbankas"
    allowed_domains = ["www.cvbankas.lt"]
    start_urls = ["https://www.cvbankas.lt/?padalinys%5B%5D=76&keyw="]

    def parse(self, response, **kwargs):
        for job in response.css("article"):
            yield {
                "title": job.css("h3.list_h3::text").get(),
                "salary": job.css("span.salary_amount::text").get(),
                "location": job.css("span.list_city::text").get(),
                "firm": job.css("span.heading_secondary > span::text").get(),
            }
        time.sleep(5)
        next_page_urls = response.css('ul.pages_ul_inner li a:not(.prev_next)::attr(href)').getall()

        for next_page_url in next_page_urls:
            yield scrapy.Request(url=next_page_url, callback=self.parse)