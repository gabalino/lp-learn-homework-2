"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

import requests


def download_file(url: str, filename: str) -> str | None:
    response = requests.get(url, allow_redirects=True, timeout=30)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
            return filename
    else:
        print('Failed to download file', filename)
        return None


def get_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def save_file(filename: str, text: str) -> bool:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return True


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    file_url = 'https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=1'
    file_name = 'referat.txt'
    text = get_file(filename=download_file(file_url, file_name))
    print(f'Файл {file_name}')
    file_length = len(text)
    print(f'Длина: {file_length}')
    word_count = len(text.split())
    print(f'Слова: {word_count}')
    text.replace('.', '!')
    file_name = 'referat2.txt'
    save_file(file_name, text)
    print(f'Файл {file_name} сохранен')


if __name__ == "__main__":
    main()
