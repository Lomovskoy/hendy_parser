from urllib.request import urlopen
from urllib.parse import urljoin

class Site_Struct:

    # Конструктор класса. Вызывается при создании экземпляра класса
    def __init__(self,url):
        self.url = url
        
    def pars(self):
        f = urlopen(self.url)
        list_html = f.read().decode('utf-8')
        return list_html
