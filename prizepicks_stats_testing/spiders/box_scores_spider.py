import scrapy


class BoxScoresSpiderSpider(scrapy.Spider):
    name = "box_scores_spider"
    allowed_domains = ["basketball.realgm.com"]
    start_urls = ["https://basketball.realgm.com/nba/scores"]

    def parse(self, response):
        box_scores = response.xpath('// *[contains(text(), "Box Score")]')
        for box_score in box_scores:
            if 'href' in box_score.attrib:
                box_score_href = box_score.css('a').attrib['href']
                box_score_url = "https://basketball.realgm.com" + box_score_href
                yield scrapy.Request(url=box_score_url, callback=self.parse_box_score)

    def parse_box_score(self, response):
        header_tag = response.css('.tablesaw.compact thead')
        categories = list()

        # Loop through each text node inside the parent tag
        for text_node in header_tag[0].css('*::text').extract():
            if not text_node.isspace():
                categories.append(text_node.strip())

        player_tags = response.css('.tablesaw.compact tbody tr')
        stats = list()
        for player_tag in player_tags:
            for text_node in player_tag.css('*::text').extract():
                if not text_node.isspace():
                    stats.append(text_node.strip())

            yield {
                categories[0]: stats[0],
                categories[1]: stats[1],
                categories[2]: stats[2],
                categories[3]: stats[3],
                categories[4]: stats[4],
                categories[5]: stats[5],
                categories[6]: stats[6],
                categories[7]: stats[7],
                categories[8]: stats[8],
                categories[9]: stats[9],
                categories[10]: stats[10],
                categories[11]: stats[11],
                categories[12]: stats[12],
                categories[13]: stats[13],
                categories[14]: stats[14],
                categories[15]: stats[15],
                categories[16]: stats[16],
                categories[17]: stats[17]
            }        

            # Clear the list
            stats = list()
        


