import requests  
from lxml import html

class get_query:
    
    response = []
    parsed_body = []
    
    def __init__(self,url):# Конструктор класса.
        self.url = url
        self.response = requests.get(self.url)
        self.parsed_body = html.fromstring(self.response.text)

    def get_title(self):
        print (self.parsed_body.xpath('//title/text()')) # Получить title страницы

    def get_href(self):
        #for x in self.parsed_body.xpath('//a/@href'): print(x)
        print('\n'.join(self.parsed_body.xpath('//a/@href')))
        
url = 'http://lomovskoykirill.h1n.ru/'

Query = get_query(url)
Query.get_title()
Query.get_href()
