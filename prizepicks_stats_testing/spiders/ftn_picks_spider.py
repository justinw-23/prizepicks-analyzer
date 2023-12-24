import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.http import TextResponse


class FtnPicksSpider(scrapy.Spider):
    name = 'ftn_picks_spider'
    start_urls = ['https://ftnnetwork.shinyapps.io/ppNBA/']

    def start_requests(self):
        picks_table_selector = '.reactable.html-widget.html-widget-output.shiny-bound-output'
        next_button_selector = '.rt-next-button.rt-page-button'
        yield scrapy.Request(
            self.start_urls[0],
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod('wait_for_selector', picks_table_selector),
                    PageMethod('wait_for_selector', next_button_selector)
                ]
            )
        )

    async def parse(self, response):
        page = response.meta['playwright_page']
        selector = '.reactable.html-widget.html-widget-output.shiny-bound-output .rt-tr-group [role="row"]'
        picks = response.css(selector)
        for player_picks in picks:
            values = []
            for value_holder in player_picks.css('[role="cell"]'):
                value = value_holder.css('::text').get()
                values.append(value)

            yield {
                'NAME': values[0],
                'TEAM': values[1],
                'STAT': values[2],
                'LINE': values[3],
                'BET': values[4],
                'WIN%': values[5]
            }

        while True:
            await page.locator('button:text("Next")').click()
            picks_table_selctor = '.reactable.html-widget.html-widget-output.shiny-bound-output'
            picks_table = await page.query_selector_all(picks_table_selctor)

            for element in picks_table:
                html_contents = await element.inner_html()
                new_response = TextResponse(
                    url='https://ftnnetwork.shinyapps.io/ppNBA/',
                    body=html_contents, encoding='utf-8')
                picks = new_response.css('.rt-tr-group [role="row"]')
                for player_picks in picks:
                    values = []
                    for value_holder in player_picks.css('[role="cell"]'):
                        value = value_holder.css('::text').get()
                        values.append(value)

                    yield {
                        'NAME': values[0],
                        'TEAM': values[1],
                        'STAT': values[2],
                        'LINE': values[3],
                        'BET': values[4],
                        'WIN%': values[5]
                    }

            disabled = await page.query_selector_all('[aria-disabled="true"]')
            if disabled:
                break
