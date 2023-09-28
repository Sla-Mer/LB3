from googletrans import Translator, LANGUAGES
import pandas as pd
from tabulate import tabulate  # Імпортуємо бібліотеку для форматування таблиці

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        # Переклад тексту на вказану мову
        translator = Translator()
        translated_text = translator.translate(text, src=scr, dest=dest)
        return translated_text.text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all"):
    try:
        # Визначення мови тексту
        translator = Translator()
        result = translator.detect(text)

        # Вибір детектированої мови та confidence
        detected_lang = result.lang
        confidence = result.confidence

        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return confidence
        else:
            return detected_lang, confidence
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    # Створіть екземпляр класу Translator
    translator = Translator()
    lang = lang.lower()
    # Перевіримо, чи lang є кодом мови
    if lang in LANGUAGES:
        # Якщо так, перекладемо код мови на назву мови
        language_name = LANGUAGES[lang]
        return language_name.capitalize()
    else:
        # Якщо не знайдено, спробуємо знайти код мови за назвою
        try:
            # Перекладемо назву мови на код мови
            translation = translator.translate(lang, src='en', dest='en')
            for code, name in LANGUAGES.items():
                if name.lower() == translation.text.lower():
                    return code
            # Назва мови не знайдена
            return "Не знайдено мову"
        except Exception as e:
            # Обробити помилки, якщо такі є (наприклад, відсутність з'єднання)
            return str(e)
def LanguageList(out="screen", text=None):
    try:
        # Створення списку мов та їх кодів
        languages = list(LANGUAGES.values())
        codes = list(LANGUAGES.keys())

        # Створення DataFrame з даними
        data = {"N": range(1, len(languages) + 1), "Language": languages, "ISO-639 code": codes}
        if text:
            # Якщо передано текст для перекладу, то додаємо колонку з перекладом
            translations = [TransLate(text, "auto", lang) for lang in codes]
            data["Text"] = translations

        df = pd.DataFrame(data)

        if out == "screen":
            # Виведення таблиці на екран
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
            return "Ok"
        elif out == "file":
            # Виведення таблиці в файл (тип файлу на розсуд студента)
            filename = "language_list_gtrans.txt"
            with open(filename, "w", encoding='utf-8') as file:
                file.write(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
            return f"Таблиця збережена у файлі: {filename} \n Ok"

        else:
            return "Недійсний параметр 'out'"

    except Exception as e:
        return f"Помилка: {e}"

