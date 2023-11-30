#full working drive meet 1

import scrapy

class DivingSpider(scrapy.Spider):
    name = "diving"
    #start_urls = ["https://secure.meetcontrol.com/divemeets/system/profile.php?number=16213"]
    start_urls =["https://secure.meetcontrol.com/divemeets/system/profile.php?number=75312"]
    def parse(self, response):
        # Extract tournament names	
        tournaments = response.css('td[colspan="3"] strong::text').extract()

        # Loop through tournaments
        for tournament in tournaments:
            # Extract event details
            events = response.xpath('//td[strong[text()="{}"]]/following::tr'.format(tournament))

            for event in events:
                event_name = event.xpath('td[1]//text()').get()
                score_link = event.xpath('td[3]/a/@href').get()

                if score_link:
                    yield response.follow(score_link, self.parse_scoresheet, meta={'event_name': event_name})
                else:
                    self.logger.warning(f"Skipping entry with no score_link for event {event_name}, URL: {response.url}")

    def parse_scoresheet(self, response):
        event_name = response.meta['event_name']

        scoresheet_rows = response.xpath('//tr[td]')
        round_number = None

        for row in scoresheet_rows:
            # Check if the row contains the round number
            if row.xpath('td[1]//text()').get():
                round_number = row.xpath('td[1]//text()').get()
                
            dive_number = row.xpath('td[2]//text()').get()
            height = row.xpath('td[3]//text()').get()
            name = row.xpath('td[4]//text()').get()
            dd = row.xpath('td[5]//text()').get()
            total = row.xpath('td[12]//text()').get()
            points = row.xpath('td[13]//text()').get()
            score = row.xpath('td[14]//text()').get()

            yield {
                'Event': event_name,
                'Round Number': round_number,
                'Dive Number': dive_number,
                'Height': height,
                'Name': name,
                'DD': dd,
                'Total': total,
                'Points': points,
                'Score': score,
            }


