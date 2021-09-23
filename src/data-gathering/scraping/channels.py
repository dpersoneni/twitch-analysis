import scrapy
import time

class QuotesSpider(scrapy.Spider):
    name = "channels"
    allowed_domains = ['https://twitchtracker.com']
    print('Hello World!')
    def start_requests(self):
        urls = [
            'https://twitchtracker.com/channels/most-followers/italian?page=1',
            'https://twitchtracker.com/channels/most-followers/italian?page=2',        
            'https://twitchtracker.com/channels/most-followers/italian?page=3',
            'https://twitchtracker.com/channels/most-followers/italian?page=4',        
            'https://twitchtracker.com/channels/most-followers/italian?page=5',
            'https://twitchtracker.com/channels/most-followers/italian?page=6',
            'https://twitchtracker.com/channels/most-followers/italian?page=7',        
            'https://twitchtracker.com/channels/most-followers/italian?page=8',
            'https://twitchtracker.com/channels/most-followers/italian?page=9',        
            'https://twitchtracker.com/channels/most-followers/italian?page=10',
            'https://twitchtracker.com/channels/most-followers/italian?page=11',        
            'https://twitchtracker.com/channels/most-followers/italian?page=12',
            'https://twitchtracker.com/channels/most-followers/italian?page=13',        
            'https://twitchtracker.com/channels/most-followers/italian?page=14',
            'https://twitchtracker.com/channels/most-followers/italian?page=15',
            'https://twitchtracker.com/channels/most-followers/italian?page=16',        
            'https://twitchtracker.com/channels/most-followers/italian?page=17',
            'https://twitchtracker.com/channels/most-followers/italian?page=18'
        ]
        headers = {
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
       
        
        for url in urls:
            
            yield scrapy.Request(url=url,  headers=headers, callback=self.parse)
            

    def parse(self, response):
        names = response.css('table#channels').xpath('.//tr/td/a/@href').getall()
        names = list(dict.fromkeys(names))
        channels = []
        for name  in names:
            channels.append(name.replace('/', ''))
            #print(name.replace('/', ''))
            
        
        print(channels)
        page = response.url[-1]
        filename = 'channels' + page +'.txt'
        f = open(filename, "w+")
        for channel in channels:
            f.write("%s\n" % channel)
        f.close()
       
   
       