import json
import csv
from pathlib import Path
from typing import Union, Any


BASE_DIR = Path(__file__).resolve().parent.parent

def read_csv_as_json(filename: str) -> list:
    file_path = BASE_DIR / 'homework_4'/"data" / filename

    with open(file_path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))



def read_json(filename: str) -> Union[list, dict]:
    file_path = BASE_DIR /'homework_4'/ "data" / filename
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(filename: str, data: Any) -> None:
    file_path = BASE_DIR / 'homework_4'/ "data" / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def parse_users_and_create_new_users():
    try:
        users_data = read_json("users.json")
        books_data = read_csv_as_json("books.csv")

        users_count = len(users_data)
        books_count = len(books_data)
        base = books_count // users_count
        remainder = books_count % users_count

        users_array = []
        start_idx = 0

        for i, user in enumerate(users_data):
            count = base + (1 if i < remainder else 0)

            # Берем срез книг
            user_books = books_data[start_idx:start_idx + count]
            start_idx += count

            new_user = {
                "name": user.get("name"),
                "gender": user.get("gender"),
                "address": user.get('address'),
                "age": user.get('age'),
                "books": [
                    {
                        "title": book.get("Title"),
                        "author": book.get("Author"),
                        "pages": int(book.get("Pages")),
                        "genre": book.get("Genre"),

                    }

                        for book in user_books
                    ]
                }
            users_array.append(new_user)


        write_json("result.json", users_array)
        print(f'Успешно создан файл с {len(users_array)} пользователями')

    except FileNotFoundError:
        print('Ошибка: Файл users.json не найден в папке data/')
    except json.JSONDecodeError:
        print('Ошибка: Неверный формат JSON в файле users.json')
    except Exception as e:
        print(f'Непредвиденная ошибка: {e}')


if __name__ == "__main__":
    parse_users_and_create_new_users()

