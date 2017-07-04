import requests

class Status_and_Headers:
    response = []
    # Конструктор класса. Вызывается при создании экземпляра класса
    def __init__(self,url):
        self.url = url
        response = requests.get(self.url)
        print(response)
    def get_status(self):
        print(self.response.status_code()) # Код ответа
    
    def get_headers(self):
        print(self.response.headers()) # Заголовки ответа


