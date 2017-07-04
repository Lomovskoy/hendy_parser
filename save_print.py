class Save_or_Answer():#Этот класс отвечает за сохранение ответов в документы

    # Конструктор класса. Вызывается при создании экземпляра класса
    def __init__(self,saveOk,inform,choice):
        self.saveOk = saveOk
        self.inform = inform
        self.choice = choice
        
    def check_and_execution(self):
        if self.choice == 1:
            if self.saveOk == 1:
                directory = 'save'
                file = 'save_html.txt'
                print('='*35+'Сохранение'+'='*35)
                f = open(directory + '/' + file, 'a', encoding='utf-8')
                line = '='*130
                f.write(self.inform+'\n'+line)
                f.close()
                print('\t\tИнформация сохранена в папку '+directory+' в файл '+file)
            elif self.saveOk == 2:
                print('='*37+'Печать'+'='*37)
                print(self.inform)
            else:
                print('='*37+'Отмена'+'='*37)
        elif self.choice == 2:
            if self.saveOk == 1:
                directory = 'save'
                file = 'save_header_query.txt'
                print('='*35+'Сохранение'+'='*35)
                f = open(directory + '/' + file, 'a', encoding='utf-8')
                line = '='*130
                
                str_inform = ''
                for i in self.inform:# Заголовки ответа
                    str_inform += str(i) + ' - ' + str(self.inform[i])+'\n'
                    
                f.write(str_inform+'\n'+line)
                f.close()
                print('\tИнформация сохранена в папку '+directory+' в файл '+file)
            elif self.saveOk == 2:
                print('='*37+'Печать'+'='*37)
                for i in self.inform:# Заголовки ответа
                    print(i,' - ',self.inform[i])
                
            else:
                print('='*37+'Отмена'+'='*37)
