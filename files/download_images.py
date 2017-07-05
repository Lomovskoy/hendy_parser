import requests  
from lxml import html  
import sys  
import urllib.parse

class Download_Images:
    def __init__(self,url):# Конструктор класса.
        self.url = url
        self.response = requests.get(url)  

    def save_image(self): 
        parsed_body = html.fromstring(self.response.text)

        # Парсим ссылки с картинками
        images = parsed_body.xpath('//img/@src')  
        if not images:  
            sys.exit("Found No Images")

        # Конвертирование всех относительных ссылок в абсолютные
        images = [urllib.parse.urljoin(self.response.url, url) for url in images]  
        print ('Found %s images' % len(images))

        # Скачиваем только первые 10
        for url in images[0:10]:
            r = requests.get(url)
            save = 'save'
            file = 'downloaded_images'
            f = open(save + '/' + file + '/%s' % url.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()
            
        ansver = 'Изображения сохранены'
        ansver_list = [ save, file, ansver ]
        return ansver_list
