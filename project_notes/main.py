

from logic import add_note, delet, search_notes,  format_notes, safe_int_input, is_meaningful

from storage import load_data, save_data


def vailete_data(prompt, attempt=3, max_lenth=50):
    for try_count in range(attempt):
        try:
            value = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print('Ввывод прерван ')
            return None
            # 2. Проверка на строку, состоящую только из цифр
        reminig = attempt - try_count - 1
        if not is_meaningful(value):
            if reminig > 0:
                print(
                    f"Ошибка: можно использовать только буквы, цифры, пробелы и знаки .,!?-. Осталось попыток: {reminig}")
            else:
                print("Короче конец братан")
            continue
        if value.isdigit():

            if reminig > 0:
                print(
                    f"Ошибка: текст не должен состоять только из цифр. Осталось попыток: {reminig}")
            else:
                print("Попытки закончились.")
            continue
            # Проверка на максимум длинны
        if not value.split():
            print(
                "Ошибка: строка не может быть пустой или состоять только из пробелов")
            continue

        if len(value) > max_lenth:
            print(f' Слишком длинный текст {max_lenth}')
            continue
            
        return value
    return None


def main():
    data = load_data()


    while True:
        print("\n--- Меню ---")
        print("1. Добавить заметку")
        print("2. Поиск заметок")
        print("3. Показать все")
        print("4. Удалить")
        print("5. Выход")
        
        answer = input("Enter any action ")

        if answer == "1":
            title = vailete_data('Enter any headling  ')
            if title is None:
                continue
            text = vailete_data('Enter any text ..')

            if text is None:
                continue
            add_note(data, title ,text)
            save_data(data)
            print('Remark added')



        elif answer =="2":
            keyword = vailete_data("Enter key-word...")
            if not keyword:
                continue
                

            result = search_notes(data,keyword)

            if not result:
                print('Nothing found')
            else:
                print(f'\n Found : {len(result)}')
                for idx , key , note in result:
                    print(f"{idx}. {note['title']} -- {note.get('date', '-')}")
                    preview = (
                        note['text'][:50] + "..."
                        if len(note['text']) > 50
                        else note['text']
                    )
                    print(f' {preview}\n')
        # 3. Показать все
        elif answer == "3":
            notes = format_notes(data)
            if not notes:
                print("Remark nothing")
                continue
            for note in notes:
                print(f'{note['index']}. {note['title']} -- {note['date']}')
                print(f'   {note['text']}\n')
        # Remove remarks
        elif answer == "4":
            key_remove = safe_int_input("Enter number what you want")
            if key_remove is None:
                print('deletion canceled')
                continue
            if delet(data , key_remove):
                save_data(data)
                print('Deleted')
            else:
                print("Number is wrong")
        
        elif answer == "5":
            print('Exit')
            break

        
        else:
            print('Хуйня какайто братан жи есть ')




if __name__ == "__main__":
    main()