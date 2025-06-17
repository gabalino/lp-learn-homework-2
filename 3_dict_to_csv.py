"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv


def get_data() -> list[dict]:
    data = [
        {"name": "Иван", "age": 28, "job": "инженер"},
        {"name": "Мария", "age": 34, "job": "врач"},
        {"name": "Алексей", "age": 45, "job": "учитель"},
        {"name": "Елена", "age": 23, "job": "дизайнер"},
        {"name": "Дмитрий", "age": 31, "job": "программист"},
        {"name": "Ольга", "age": 29, "job": "маркетолог"},
        {"name": "Сергей", "age": 40, "job": "менеджер"},
        {"name": "Анна", "age": 26, "job": "бухгалтер"},
        {"name": "Павел", "age": 38, "job": "архитектор"},
        {"name": "Татьяна", "age": 33, "job": "юрист"}
    ]
    return data


def create_csvfile(filename: str, data: list[dict]):
    with open(filename, "w", newline="", encoding='utf-8') as file:
        fildnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fildnames)
        writer.writeheader()
        writer.writerows(data)
    return


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    employees = get_data()
    create_csvfile('employees.csv', employees)


if __name__ == "__main__":
    main()
