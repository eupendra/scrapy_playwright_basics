from helper import should_abort_request 
BOT_NAME = 'dynamic_pw'

SPIDER_MODULES = ['dynamic_pw.spiders']
NEWSPIDER_MODULE = 'dynamic_pw.spiders'

ROBOTSTXT_OBEY = True

PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": False}

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 100000

# PLAYWRIGHT_ABORT_REQUEST = should_abort_request
