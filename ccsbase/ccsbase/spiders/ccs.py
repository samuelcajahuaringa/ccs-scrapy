import scrapy
from ccsbase.items import CcsItem
import random

class CcsSpider(scrapy.Spider):
    name = "ccs"
    allowed_domains = ["ccsbase.net"]
    start_urls = ["https://ccsbase.net/query"]    

    custom_settings = {
        'FEEDS': {
            'ccsbase.json': {'format': 'json', 'overwrite': True},
        }
    }

    """
    user_agent_list = [
        'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0',
        'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
        'Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0',
        'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Safari/537.36',
        'Mozilla/5.0 (Android 7.0; Mobile; rv:62.0) Gecko/62.0 Firefox/62.0',
        'Mozilla/5.0 (iPod touch; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',        
    ]
    """

    def parse(self, response):
        # numbers of pages
        npages = 50 #int(response.css('a.btn-outline-info ::text').getall()[-1])
        # select values 
        full_info = response.css('tr')
        del full_info[0]
    
        for info in full_info:
            item = info.css('td ::text').getall()
            ccs_item = CcsItem()        
            ccs_item['id'] = item[0]
            ccs_item['name'] = item[1] 
            ccs_item['adduct'] = item[2]          
            ccs_item['mass'] = float(item[3])*float(item[7])
            ccs_item['ccs'] = float(item[4])
            ccs_item['smile'] = item[5]            
            ccs_item['charge'] = int(item[7])
            yield ccs_item

        for page in range(2, npages + 1):
            next_page = 'https://ccsbase.net/query?page='+str(page)
            yield response.follow(next_page,callback=self.parse) #, headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]})     
                    