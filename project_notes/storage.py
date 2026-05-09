import json
import os
<<<<<<< HEAD
from typing import Any 


=======

import tempfile
FILE_NAME = "data.json"


def save_data(data):
    dir_name = os.path.dirname(FILE_NAME) or  "."
    with tempfile.NamedTemporaryFile(
        'w',
        encoding='utf-8',
        dir=dir_name,
        delete=False
>>>>>>> 3f31007f31c62fba8dc88b890b1f31fcce416156

    )   as tmp:
        json.dump(data, tmp , ensure_ascii=False , indent=2)
        temp_name = tmp.name

    os.replace(temp_name, FILE_NAME)

<<<<<<< HEAD
class JSONStorage:
    def __int__(self,file_path: str):
        self.file_path = file_path
        self.temp_file = f'{file_path}. tmp '

    def load(self) -> dict[str , Any]:
        if not os.path.exists(self.file_path):
            return {}
        try:
            with open(self.file_path, 'r' , encoding='utf-8') as file:
                return json.load(file)
        except json. JSONDecodeError:
            return {}
        
        def save(self,data: dict[str , Any]) -> None:
            with open(self.temp_file, 'w' , encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False , indent=2)

            os.replace(self.temp_file, self.file_path)
=======
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
>>>>>>> 3f31007f31c62fba8dc88b890b1f31fcce416156
