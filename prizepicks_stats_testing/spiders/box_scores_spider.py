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
                url = "https://basketball.realgm.com" + box_score_href
                yield scrapy.Request(url=url, callback=self.parse_box_score)

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

            yield {category: stat for category, stat in zip(categories, stats[:len(categories)])}

            # Clear the list
            stats = list()
