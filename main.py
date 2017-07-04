from print_text import PrintText
from structure_site import Site_Struct
from save_print import Save_or_Answer
from get_status_heder import Get_Heder_Query

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
        Action = Save_or_Answer(saveOk,list_html,choice)
        Action.check_and_execution()
        
    if choice == 2:
        #Делаем запрос к серверу
        GetInfo = Get_Heder_Query(url)
        
        #Запрашиваем действие с ответом
        status = GetInfo.get_status()
        headers = GetInfo.get_header()
        headers['Status']=str(status)

        saveOk = Print.save_choice()
        Action = Save_or_Answer(saveOk,headers,choice)
        Action.check_and_execution()
        
if __name__ == "__main__":
    main()
