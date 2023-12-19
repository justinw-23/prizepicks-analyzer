import scrapy


class NbaScoreboardSpider(scrapy.Spider):
    name = "nba_scoreboard"
    allowed_domains = ["cbssports.com"]
    start_urls = ["https://www.cbssports.com/nba/scoreboard/"]

    def parse(self, response):
        box_scores = response.xpath('// *[contains(text(), "Box Score")]')
        for box_score in box_scores:
            box_score_href = box_score.css('a').attrib['href']
            url = "https://www.cbssports.com" + box_score_href
            yield scrapy.Request(url=url, callback=self.parse_box_score)

    def parse_box_score(self, response):
        starters_stats = response.css('.starters-stats .no-hover.data-row')
        bench_stats = response.css('.bench-stats .no-hover.data-row')

        for player_stats in starters_stats:
            stats = []
            selector = '''
            *:not(.no-hover.data-row)
            :not(.name-element)
            :not(.number-element.for-mobile)'''

            for value_holder in player_stats.css(selector):
                value = value_holder.css('::text').get()
                stats.append(value)

            yield {
                'Name': stats[0],
                'REB': stats[1],
                'PTS': stats[2],
                'AST': stats[3],
                'FG': stats[4],
                '3PT': stats[5],
                'FT': stats[6],
                'PF': stats[7],
                'MIN': stats[8],
                'STL': stats[9],
                'BLK': stats[10],
                'TO': stats[11],
                '+-': stats[12],
                'FPTS': stats[13]
            }

        for player_stats in bench_stats:
            stats = []
            selector = '''*:not(.no-hover.data-row)
            :not(.name-element)
            :not(.number-element.for-mobile)'''

            for value_holder in player_stats.css(selector):
                value = value_holder.css('::text').get()
                stats.append(value)

            if stats[1] == '-':
                continue

            yield {
                'Name': stats[0],
                'REB': stats[1],
                'PTS': stats[2],
                'AST': stats[3],
                'FG': stats[4],
                '3PT': stats[5],
                'FT': stats[6],
                'PF': stats[7],
                'MIN': stats[8],
                'STL': stats[9],
                'BLK': stats[10],
                'TO': stats[11],
                '+-': stats[12],
                'FPTS': stats[13]
            }
