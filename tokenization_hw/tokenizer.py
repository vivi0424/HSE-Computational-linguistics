"""
Модуль для токенизации текста различными способами.
Содержит класс TextTokenizer с тремя методами токенизации:
- simple_tokenize: простая токенизация (по пробелам/знакам препинания)
- nltk_tokenize: токенизация через NLTK (word_tokenize)
- spacy_tokenize: токенизация через spaCy (en_core_web_sm)
"""

import re

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        pass

    def simple_tokenize(self, text):
        """
        Простая токенизация по пробелам и знакам препинания

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов
        """
        # Реализация простой токенизации
        if not isinstance(text, str):
            raise TypeError("simple_tokenize ожидает строку (str).")

        pattern = r"[A-Za-zА-Яа-яЁё0-9]+(?:'[A-Za-zА-Яа-яЁё0-9]+)?"
        return re.findall(pattern, text) 

    def nltk_tokenize(self, text):
        """
        Токенизация с использованием NLTK

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация NLTK токенизации
        if not isinstance(text, str):
            raise TypeError("nltk_tokenize ожидает строку (str).")

        try:
            from nltk.tokenize import word_tokenize
        except Exception as e:
            return f"NLTK не установлен или недоступен: {e}. Установите пакет 'nltk'."

        try:
            return word_tokenize(text)
        except LookupError:
            return (
                "Данные NLTK для токенизации не найдены. "
                "Установите ресурсы (выполните в Python):\n"
                ">>> import nltk\n"
                ">>> nltk.download('punkt')\n"
                "или при необходимости:\n"
                ">>> nltk.download('punkt_tab')"
            )
        except Exception as e:
            return f"Ошибка NLTK токенизации: {e}"

    def spacy_tokenize(self, text):
        """
        Токенизация с использованием spaCy

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация spaCy токенизации
        if not isinstance(text, str):
            raise TypeError("spacy_tokenize ожидает строку (str).")

        try:
            import spacy
        except Exception as e:
            return f"spaCy не установлен или недоступен: {e}. Установите пакет 'spacy'."

        try:
            nlp = spacy.load("en_core_web_sm")
        except OSError:
            return (
                "Модель spaCy 'en_core_web_sm' не найдена.\n"
                "Установите модель командой:\n"
                "python -m spacy download en_core_web_sm"
            )
        except Exception as e:
            return f"Ошибка загрузки spaCy модели: {e}"

        try:
            doc = nlp(text)
            return [t.text for t in doc]
        except Exception as e:
            return f"Ошибка spaCy токенизации: {e}"

    def tokenize_all(self, text):
        """
        Применяет все доступные методы токенизации

        Args:
            text (str): Входной текст

        Returns:
            dict: Словарь с результатами всех методов
        """
        # Реализация вызова всех методов
        return {
            "simple": self.simple_tokenize(text),
            "nltk": self.nltk_tokenize(text),
            "spacy": self.spacy_tokenize(text),
        }

def demo():
    """Демонстрационная функция: запускает токенизацию примерного текста всеми методами."""
    # Пример использования
    sample_text = "Hello, world! This is a test sentence."
    tk = TextTokenizer()
    results = tk.tokenize_all(sample_text)
    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    demo()