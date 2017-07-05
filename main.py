from print_text import PrintText
from structure_site import Site_Struct
from save_print import Save_or_Answer
from get_status_heder import Get_Heder_Query
from get_attribute import Get_Attribute
from download_images import Download_Images

def main():
    #Выводим приваетствие
    Print = PrintText()
    Print.print_hello()

    #Запрашиваем адрес сайта
    url = Print.query_url()
    
    while True:
        #Спрашиваем у пользователя выбор
        choice = Print.user_choice()
        
        #Проверяем ответ
        if choice == 1:
            #Делаем запрос к серверу
            Struct = Site_Struct(url)
            
            #Получаем нужную информацию
            list_html = Struct.pars()

            #Запрос решения пользователя
            saveOk = Print.save_choice()
            Action = Save_or_Answer(saveOk,list_html,choice)
            Action.check_and_execution()
            
        elif choice == 2:
            #Делаем запрос к серверу
            GetInfo = Get_Heder_Query(url)
            
            #Получаем нужную информацию
            status = GetInfo.get_status()
            headers = GetInfo.get_header()
            headers['Status']=str(status)

            #Запрос решения пользователя
            saveOk = Print.save_choice()
            Action = Save_or_Answer(saveOk,headers,choice)
            Action.check_and_execution()

        elif choice == 3:
            #Делаем запрос к серверу
            Attribute = Get_Attribute(url)

            #Получаем нужную информацию
            tytle = Attribute.get_title()
            attr = Attribute.get_attr()
            tytle = ''.join(tytle)
            attr.append(tytle)
            attr.reverse()
            
            #Запрос решения пользователя
            saveOk = Print.save_choice()
            Action = Save_or_Answer(saveOk,attr,choice)
            Action.check_and_execution()
            
        elif choice == 4:
            #Делаем запрос к серверу
            GetImages = Download_Images(url)

            #Получаем нужную информацию
            ansver_list = GetImages.save_image()
            
            #Запрос решения пользователя
            saveOk = 1
            
            #Ответ пользователю
            Action = Save_or_Answer(saveOk,ansver_list,choice)
            Action.check_and_execution()

        elif choice == 5:
            #Запрашиваем адрес сайта
            url = Print.query_url()

        elif choice == 6:
            #Звершеине работы
            print('='*30+'Завершение программы'+'='*30)
            break
        
if __name__ == "__main__":
    main()
