import scrapy


class NbaScoreboardSpider(scrapy.Spider):
    name = "nba_scoreboard"
    allowed_domains = ["cbssports.com"]
    start_urls = ["https://www.cbssports.com/nba/scoreboard/"]

    def parse(self, response):
        box_scores = response.xpath('// *[contains(text(), "Box Score")]')
        for box_score in box_scores:
            box_score_href = box_score.css('a').attrib['href']
            box_score_url = "https://www.cbssports.com" + box_score_href
            yield scrapy.Request(url=box_score_url, callback=self.parse_box_score)



    def parse_box_score(self, response):
        starters_stats = response.css('.starters-stats .no-hover.data-row')
        bench_stats = response.css('.bench-stats .no-hover.data-row')
        # header = response.css('.starters-stats .header-row')[0]
        # header_list = ['Name']

        # for category in header.css('*:not(.name-element):not(.header-row)'):
        #     header_list.append(category.css('::text').get())

        for player_stats in starters_stats:
            stats = []
            # i = 0
            for value_holder in player_stats.css('*:not(.no-hover.data-row):not(.name-element):not(.number-element.for-mobile)'):
                value = value_holder.css('::text').get()
                stats.append(value)
                # stats.append((header_list[i], value)
                # i += 1
            yield {
                'Name' : stats[0],
                'REB' : stats[1],
                'PTS' : stats[2],
                'AST' : stats[3],
                'FG' : stats[4],
                '3PT' : stats[5],
                'FT' : stats[6],
                'PF' : stats[7],
                'MIN' : stats[8],
                'STL' : stats[9],
                'BLK' : stats[10],
                'TO' : stats[11],
                '+-' : stats[12],
                'FPTS' : stats[13]
            }
            # for stat in stats:
            #     yield {
            #         stat[0] : stat[1]
            #     }

        for player_stats in bench_stats:
            stats = []
            for value_holder in player_stats.css('*:not(.no-hover.data-row):not(.name-element):not(.number-element.for-mobile)'):
                value = value_holder.css('::text').get()
                stats.append(value)
        
            if stats[1] == '-':
                continue

            yield {
                'Name' : stats[0],
                'REB' : stats[1],
                'PTS' : stats[2],
                'AST' : stats[3],
                'FG' : stats[4],
                '3PT' : stats[5],
                'FT' : stats[6],
                'PF' : stats[7],
                'MIN' : stats[8],
                'STL' : stats[9],
                'BLK' : stats[10],
                'TO' : stats[11],
                '+-' : stats[12],
                'FPTS' : stats[13]
            }
