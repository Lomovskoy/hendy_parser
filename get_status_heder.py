import requests

class Get_Heder_Query:
    
    response = {}
    
    def __init__(self,url):# Конструктор класса.
        self.url = url
        self.response = requests.get(url)
        
    def get_status(self):
        status = self.response.status_code # Код ответа
        return status
    
    def get_header(self):
        header = self.response.headers
        return header
