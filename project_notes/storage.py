

import json
import os

import tempfile
FILE_NAME = "data.json"


def save_data(data):
    dir_name = os.path.dirname(FILE_NAME) or  "."
    with tempfile.NamedTemporaryFile(
        'w',
        encoding='utf-8',
        dir=dir_name,
        delete=False

    )   as tmp:
        json.dump(data, tmp , ensure_ascii=False , indent=2)
        temp_name = tmp.name

    os.replace(temp_name, FILE_NAME)

def load_data():
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        broken_name = FILE_NAME + ".broken"
        os.replace(FILE_NAME, broken_name)
        print(f"Файл данных повреждён. Он сохранён как {broken_name}")
        return {}

    if not isinstance(data, dict):
        print("Ошибка: файл данных должен содержать словарь.")
        return {}

    return data