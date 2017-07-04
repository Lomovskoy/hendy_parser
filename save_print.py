class Save_or_Answer():#Этот класс отвечает за сохранение ответов в документы

    # Конструктор класса. Вызывается при создании экземпляра класса
    def __init__(self,saveOk,list_html):
        self.saveOk = saveOk
        self.list_html = list_html
        
    def check_and_execution(self):
        if self.saveOk == 1:
            directory = 'save'
            file = 'save_html.txt'
            print('='*35+'Сохранение'+'='*35)
            f = open(directory + '/' + file, 'a', encoding='utf-8')
            line = '='*130
            f.write(self.list_html+'\n'+line)
            f.close()
            print('\t\tИнформация сохранена в папку '+directory+' в файл '+file)
        elif self.saveOk == 2:
            print('='*37+'Печать'+'='*37)
            print(self.list_html)
        else:
            print('='*37+'Отмена'+'='*37)
        
    
