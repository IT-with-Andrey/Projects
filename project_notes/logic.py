<<<<<<< HEAD
=======


from datetime import datetime

import uuid
import re


def add_note(data ,title, text):
   
    

    note_id = str(uuid.uuid4())

    
    data[note_id] = {
        "title": title,
        "text": text,
        "date": datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    
    return note_id

def is_meaningful(text):
    # Разрешены: буквы (любые), цифры, пробелы, . , ! ? -
    pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9\s.,!?-]+$'
    return bool(re.fullmatch(pattern, text))


def safe_int_input(prompt , max_attempts=3 , default=None):
    for attempt in range(max_attempts):
        try:
            raw = input(prompt).strip()
            return int(raw)
        except (ValueError, EOFError , TypeError  ):
            print('Хюстан у нас проблемы ')
            if attempt == max_attempts -1:
                print(f'Ну братан не повезло тебе по ходу {default}')
                return default
    

def format_notes(data):
    result= []
    for i ,(note_id,note )in enumerate(data.values(),start=1):
        result.append({
            'index' : i ,
            'title': note.get('title', 'Без названия'),
            'text': note.get('text', ''),
            'date': note.get('date','-')
        })
    return result

def delet(data, number):
    
    items = list(data.items())                 # словарь → превращаем в список ключей, чтобы можно было работать по индексу.

    if 1 <= number <= len(items):        # Cравниваем с ответом от пользователя 
        note_id = items[number - 1][0]  # Приводим к упорядочному индексу 
        del data[note_id]                # Само дейсвие 
        return True
    return False


    
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
>>>>>>> 3f31007f31c62fba8dc88b890b1f31fcce416156
