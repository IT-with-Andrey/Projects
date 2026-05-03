

import json

FILE_NAME = "data.json"


def save_data(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as f :
        json.dump(data, f  , ensure_ascii=False, indent=2)


def load_data():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        
        print("ОШИБОЧКА БРАЧУ ")
        return {}
    except json.JSONDecodeError:
        
        print("Хуйня какайто у нас братан ")
        return {}