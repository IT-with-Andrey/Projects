

from datetime import datetime

import uuid
import re

def add_note(data ,title, text):
   
    current_data = datetime.now().strftime('%Y-%m-%d %H:%M')

    key = str(uuid.uuid4())

    
    data[key] = {
        "title": title,
        "text": text,
        "data": current_data
    }
    print("Успешное сохранение ")

def valete_data(prompt,attempt=3, max_lenth=50,min_lenth=0):
    for try_count in range(attempt):
        try:
            value = input(prompt)
        except (EOFError, KeyboardInterrupt):
            
            print('Ввывод прерван ')
            return None
        
        
                                        # 2. Проверка на строку, состоящую только из цифр
        reminig= attempt - try_count - 1
        if not is_meaningful(value):
            if reminig > 0 :
                print(f"Ошибка: можно использовать только буквы, цифры, пробелы и знаки .,!?-. Осталось попыток: {reminig}")
            else:
                print("Короче конец братан")
            continue
        if value.isdigit():
            
            if reminig > 0 :
                print(f"Ошибка: текст не должен состоять только из цифр. Осталось попыток: {reminig}")
            else:
                print("Попытки закончились.")
            continue
                                                # Проверка на максимум длинны 
        if not value.split():
            print("Ошибка: строка не может быть пустой или состоять только из пробелов")
            continue

        if len(value) > max_lenth:
                
            if  reminig > 0 :
                print(f"Ошибка: текст слишком длинный (максимум {max_lenth} символов). Осталось попыток: {reminig}")
            else:
                print("Короче конец братан ")
            continue
                
        if len(value) < min_lenth:
            
            if reminig > 0 :
                print(f"Ошибка: текст слишком короткий (минимум {min_lenth} символов). Осталось попыток: {reminig}")
            else:
                print("Братец мой дорогой все закончилось ")
            continue
        return value
    return None
def is_meaningful(text):
    # Разрешены: буквы (любые), цифры, пробелы, . , ! ? -
    pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9\s.,!?-]+$'
    return bool(re.match(pattern, text))


def safe_int_input(prompt , max_attempts=3 , default=None):
    for attempt in range(max_attempts):
        try:
            return int(input(prompt))
        except (ValueError, EOFError , TypeError ):
            print('Хюстан у нас проблемы ')
            if attempt == max_attempts -1:
                print(f'Ну братан не повезло тебе по ходу {default}')
                return default
    

def show(data):
    GREEN = '\033[92m'
    RESET = '\033[0m'
    for i, (key, note) in enumerate(data.items(), start=1):
        print(f"{GREEN}─── Заметка #{i} ───{RESET}")
        print(f"Название: {note['title']}")
        print(f"Содержание: {note['text']}")
        print(f"Дата: {note.get('data', '—')}\n")


def delet(data, key_remove):
    
    keys = list(data.keys())                 # словарь → превращаем в список ключей, чтобы можно было работать по индексу.

    if 1 <= key_remove <= len(keys):        # Cравниваем с ответом от пользователя 
        key_remove = keys[key_remove - 1 ]  # Приводим к упорядочному индексу 
        del data[key_remove]                # Само дейсвие 
        print("Все успешно удаленно ")
    else:
        print("По моему ты ввел не тот ID ключь ",)


    
def search_notes(data , keyword):
    """
    Ищет заметки, содержащие keyword в заголовке или тексте.
    Возвращает список кортежей (индекс, ключ, заметка) для удобного отображения.
    """
    keyword_lower = keyword.lower().strip()

    if not keyword_lower:
        return []
    result = []
    for idx, (key , note) in enumerate(data.items() , start=1):
        title = note.get('title','').lower()
        text = note.get('text','').lower()
        if keyword_lower in title or keyword_lower in text:
            result.append((idx, key , note))
    
    return result        