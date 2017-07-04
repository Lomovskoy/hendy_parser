from print_text import PrintText
from structure_site import Site_Struct
from save_print import Save_or_Answer
from get_status_heders import Status_and_Headers
def main():
    #Выводим приваетствие
    Print = PrintText()
    Print.print_hello()

    #Запрашиваем адрес сайта
    url = Print.query_url()

    #Спрашиваем у пользователя выбор
    choice = Print.user_choice()
    
    #Проверяем ответ
    if choice == 1:
        Struct = Site_Struct(url)
        list_html = Struct.pars()

        #Запрашиваем действие с ответом
        saveOk = Print.save_choice()
        Action = Save_or_Answer(saveOk,list_html)
        Action.check_and_execution()
        
    if choice == 2:
        #Делаем запрос к серверу
        GetInfo = Status_and_Headers(url)
        
        status = GetInfo.get_status()
        headers = GetInfo.get_headers()

        print(status)
        print(headers)
if __name__ == "__main__":
    main()
