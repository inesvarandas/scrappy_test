from scrapy.cmdline import execute


def __main__():

    execute("scrapy crawl author".split())
    execute("scrapy crawl quotes -o quotes.json")