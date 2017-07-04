import requests

class get_query:
    
    response = {}
    
    def __init__(self,url):# Конструктор класса.
        self.url = url
        self.response = requests.get(url)
        
    def get_status(self):
        print (self.response.status_code,'\n') # Код ответа

    def get_header(self):
        for i in self.response.headers:# Заголовки ответа
            print(i,' - ',self.response.headers[i])

url = 'http://opgames.h1n.ru/'

Query = get_query(url)
Query.get_status()
Query.get_header()
