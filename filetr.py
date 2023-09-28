import json
from Translation_Package.gtarns_module import *

def read_config(config_file):
    try:
        with open(config_file, "r", encoding="utf-8") as file:
            config_data = json.load(file)
        return config_data
    except Exception as e:
        print(f"Помилка при зчитуванні конфігураційного файлу: {e}")
        return None

def process_text(config):
    try:
        source_file = config["source_file"]
        target_language = config["target_language"]
        output_type = config["output_type"]
        max_characters = config["max_characters"]
        max_words = config["max_words"]
        max_sentences = config["max_sentences"]

        with open(source_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Зберігаємо реальний розмір тексту
        original_text_length = len(text)
        words = text.split()
        sentences = text.split(".")

        # Отримайте інформацію про текст без обмежень (кількість символів, слів, речень)
        print("Кількість символів (Без обмеження):", original_text_length)
        print("Кількість слів (Без обмеження):", len(words))
        print("Кількість речень (Без обмеження):", len(sentences))

        # Обмеження кількості символів
        if original_text_length > max_characters:
            text = text[:max_characters]

        # Обмеження кількості слів
        if len(words) > max_words:
            words = words[:max_words]
            text = ' '.join(words)

        # Обмеження кількості речень
        if len(sentences) > max_sentences:
            sentences = sentences[:max_sentences]
            text = '. '.join(sentences)



        # Отримайте інформацію про текст (кількість символів, слів, речень) з обмеженнями
        text_length = len(text)
        word_count = len(words)
        sentence_count = len(sentences)

        print("Кількість символів (обмежено):", text_length)
        print("Кількість слів (обмежено):", word_count)
        print("Кількість речень (обмежено):", sentence_count)
        print("Мова тексу:", LangDetect(text, "lang"))

        # Виконайте переклад тексту
        translated_text = TransLate(text, "auto", target_language)

        if output_type == "screen":
            print("Мова перекладу:", CodeLang(target_language))
            print("Перекладений текст:")
            print(translated_text)
        elif output_type == "file":
            output_file = source_file.replace(".txt", f"_{target_language}.txt")
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(translated_text)
            print("Ok")
            print(f"Результат збережено у файлі: {output_file}")
        else:
            print("Недійсний тип виведення у конфігураційному файлі.")

    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    config_file = "config.json"
    config = read_config(config_file)

    if config:
        process_text(config)
