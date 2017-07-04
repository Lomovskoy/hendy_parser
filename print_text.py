class PrintText:#Здесь находится метод выводящий сообщения для пользователя
    
    def print_hello(self):#Этот метод выводит приветствие пользователю
        print('*'*32,'HENDY PARSER','*'*31)
        print('\t\t   Добро пожаловать в программу HENDY PARSER')
        print('\t\t   -----------------------------------------')
        print('\t     Которая поможет вам лего получить данные с любого сайта')
        print('_'*80)

    def query_url(self):#Этот метод выводит запрос адреса сайта пользователю
        #url = input('\n\tВведите адрес сайта для парсинга: ')
        url = 'http://opgames.h1n.ru/'
        return url
    
    def user_choice(self):#Этот метод выводит запрос выбора пользователю
        print('Выберите действие:')
        print('1.Получить HTML структуру сайта')
        print('2.Получить статус сервера и шапку ответа с информацией о нём')
        choice = int(input())
        return choice
    
    def save_choice(self):
        print('Получин ответ:')
        print('1.Сохранить в документ')
        print('2.Вывести на экран')
        print('3.назад')
        save = int(input())
        return save
