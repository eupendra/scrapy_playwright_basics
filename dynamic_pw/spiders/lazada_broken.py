import logging

import scrapy
from scrapy_playwright.page import PageMethod

from helper import should_abort_request


class LazadaBrokenSpider(scrapy.Spider):
    name = "lazada_broken"

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.lazada.com.my/shop-laptops-gaming/"
        )

    def parse(self, response):
        products_selector = response.css('[data-tracking="product-card"]')

        for product in products_selector:
            link = response.urljoin(product.xpath('.//a[text()]/@href').get())
            yield scrapy.Request(link, callback=self.parse_product)

    def parse_product(self, response):
        yield {
            'Product': response.css('.pdp-mod-product-badge-title ::Text').get(),
            'Price': response.css('.pdp-price_color_orange ::Text').get()
        }
