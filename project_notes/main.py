


from logic import add_note ,delet, search_notes,  show , safe_int_input , valete_data ,search_notes

from storage import load_data , save_data


data  = load_data()



while 1 :
    print("""
            1.Add a note:
            2. Search:
            3. Show all notes 
            4. Remove remark  
            5. Exit:
              """)
    answer = input("Choose:...")
    if answer  == "1":
        title = valete_data("Title your remark ....", max_lenth=50,min_lenth=10)
        if title is None:
            continue
        text = valete_data("Your core remark >...",min_lenth=10 , max_lenth=100)
        if text is None:
            continue
        add_note(data , title , text)
        save_data(data)

    elif answer == "2":
        keyword = input("Введите ключевое слово для поиска: ").strip()
        if not keyword:
            print("Ключевое слово не может быть пустым.")
            continue
        result = search_notes(data , keyword) 
        if not result:
            print("НЕ его не найденно")
        else:
            print(f'\nНайденно заметок ...{len(result)}')
            for idx , key , note in result:
                print(f'{idx} . {note["title"]} -- {note['data']}')
                preview = note['text'][:50] + "..." if len(note['text']) > 50 else note['text']
                print(f"   {preview}\n")



    elif answer == "3":
        show(data)
        
    elif answer == "4":
        
        key_remove = safe_int_input("Enter remark ...")
        

        delet(data,key_remove)
        save_data(data)
        
            

    elif answer =="5":
        print("До свидания мой дорогой друг ")
        break




