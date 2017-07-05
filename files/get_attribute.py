import requests  
from lxml import html

class Get_Attribute:
    
    response = []
    parsed_body = []
    
    def __init__(self,url):# Конструктор класса.
        self.url = url
        self.response = requests.get(self.url)
        self.parsed_body = html.fromstring(self.response.text)

    def get_title(self):
        tytle = self.parsed_body.xpath('//title/text()') # Получить title страницы
        return tytle
    
    def get_attr(self):
        href = self.parsed_body.xpath('//a/@href') # Получить аттрибут href для всех ссылок
        return href
