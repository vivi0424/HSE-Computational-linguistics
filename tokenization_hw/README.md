# Tokenization Homework
# Описание проекта
Этот проект реализует модуль `tokenizer.py`, который выполняет токенизацию текста тремя способами:
1. Простая токенизация по пробелам и знакам препинания
2. Токенизация с использованием NLTK
3. Токенизация с использованием spaCy

## Структура проекта
tokenization_hw/
├── tokenizer.py # основной модуль с классом TextTokenizer
├── demo.py # демонстрационный скрипт
├── requirements.txt # список зависимостей (nltk, spacy)
└── README.md # этот файл

## Установка
1. Создать и активировать виртуальное окружение (рекомендуется Python 3.12, так как на Python 3.14 библиотека spaCy пока не поддерживается)
2. Установить зависимости
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
3. Скачать данные для NLTK
```bash
python -m nltk.downloader punkt punkt_tab
```
4. Запустить демонстрацию
```bash
python demo.py
```
## Пример вывода
simple: ['Hello', 'world', 'This', 'is', 'a', 'test', 'sentence', 'How', 'are', 'you', 'today']
nltk: ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'test', 'sentence', '.', 'How', 'are', 'you', 'today', '?']
spacy: ['Hello', ',', 'world', '!', 'This', 'is', 'a', 'test', 'sentence', '.', 'How', 'are', 'you', 'today', '?']

## Описание методов
`simple_tokenize(text)`: Делит строку на слова и числа по пробелам и знакам препинания
`nltk_tokenize(text)`: Токенизация через `nltk.word_tokenize`                        
`spacy_tokenize(text)`: Токенизация с помощью модели `en_core_web_sm`
`tokenize_all(text)`: Возвращает словарь с результатами всех трёх методов

## Обработка ошибок
Если библиотека не установлена, метод возвращает сообщение с подсказкой, как ее поставить.
