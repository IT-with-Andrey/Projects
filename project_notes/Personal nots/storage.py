
import json

import os 

from typing import Any


class JSONStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.temp_file = f'{file_path}. tmp'


    def load(self) -> dict[str,Any]:
        if not os.path.exists(self.file_path):
            return {}
        
        try:
            with open(self.file_path, 'r' , encoding='utf-8') as file:
                return json.load(file)
        
        except json.JSONDecodeError:
            return {}
        
    def save(self , data: dict[str , Any]) -> None:
        with open(self.temp_file, 'w' , encoding='utf-8') as file:
            json.dump(data , file , ensure_ascii=False , indent=2)


        os.replace(self.temp_file , self.file_path)