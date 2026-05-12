

from service import NotesService

from storage import JSONStorage


def print_notes(notes):
    if not notes:
        return f'Заметок пока нет '

    for index, note in enumerate(notes, start=1):
        print(
            f"\n--- Заметка #{index} ---\n"
            f"ID: {note.id}\n"
            f"Заголовок: {note.title}\n"
            f"Текст: {note.text}\n"
            f"Дата: {note.created_at}"
        )


def get_non_input(prompt: str) -> str | None:
    try:
        value = input(prompt).strip()
    except EOFError:
        print('\nВвод прерван')
        return None

    if not value:
        print('Empty Enter')
        return None

    return value


def main():
    storage = JSONStorage('data.json')
    service = NotesService(storage)

    while True:
        print(""""
                1. Добавить заметку
                2. Найти заметку
                3. Показать все заметки
                4. Удалить заметку
                5. Выход 
                      """
              )

        choice = input("Выбери действие: ").strip()

        if choice == '1':
            title = get_non_input('Title')
            if title is None:
                continue

            text = get_non_input('Text')
            if text is None:
                continue

            note = service.add_note(title, text)
            print(f'Заметка добавлена. ID: {note.id}')

        elif choice == '2':
            keyword = get_non_input('Ключевое слово: ')
            if keyword is None:
                continue
            result = service.search_notes(keyword)
            print_notes(result)

        elif choice == '3':
            notes = service.get_all_notes()
            print_notes(notes)

        elif choice == '4':
            note_id = get_non_input('ID Заметка')
            if note_id is None:
                continue
            if service.delete_note(note_id):
                print('Заметка удалена ')
            else:
                print('Заметка не найдена ')

        elif choice == '5':
            print('Exit')
            break
        else:
            print('Нихуя не пойму тебя мой братик ')


if __name__ == '__main__':
    main()
