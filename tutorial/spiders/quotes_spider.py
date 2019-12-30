import scrapy

class data_toscrap(scrapy.Spider):
    name = 'jobscrap'
    start_urls = ['https://iefponline.iefp.pt/IEFP/pesquisas/search.do?cat=ofertaEmprego']

    def parse(self, response):
        for elem in response.xpath('//*[@class="right-click-article"]/@href').extract():
            # titulos = elem.strip()
            yield response.follow(elem, self.parse_job)

    def parse_job(self, response):
        def extract_with_xpath(query):
            for titulo in response.xpath(query).extract():
                s = titulo.strip()
            return s

            yield {
                'Titulo': extract_with_xpath('//*[@class="nomargins"]/text()')
            }
