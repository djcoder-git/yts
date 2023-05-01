import scrapy

class YtsSpider(scrapy.Spider):
    name = 'yts'
    start_urls = ['https://yts.mx']

    def parse(self, response):
        for movie in response.css('div.browse-movie-wrap'):
            title = movie.css('div.browse-movie-bottom a.browse-movie-title::text').get()
            year = movie.css('div.browse-movie-year::text').get()
            rating = movie.css('h4.rating::text').get()
            yield {
                'title': title,
                'year': year,
                'rating': rating,
            }
