import scrapy


class PinePicksSpiderSpider(scrapy.Spider):
    name = "pine_picks_spider"
    allowed_domains = ["pine-sports.com"]
    start_urls = ["https://www.pine-sports.com/PrizePicks/NBA/"]

    def parse(self, response):
        header = response.css('thead')[0]
        fields = header.css('th::text').getall()
        
        table = response.css('tbody')[0]
        players = table.css('tr')
        for player in players:
            stats = player.css('td::text').getall()
            # Extract the bet (over or under) due to funny formatting on the website
            bet = player.css('td a::text').get()
            stats.append(bet)
            yield {field: stat for field, stat in zip(fields, stats)}
            
