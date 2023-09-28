from deep_translator import GoogleTranslator
from langdetect import detect,detect_langs

def TransLate(text: str, scr: str, dest: str):
    try:
        # Переклад тексту на вказану мову
        translated_text = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return str(e)


def LangDetect(text: str, set: str = "all"):
    detected_langs = detect_langs(text)
    primary_detection = detected_langs[0]
    detected_lang = primary_detection.lang
    confidence = primary_detection.prob

    if set == "lang":
        return detected_lang
    elif set == "confidence":
        return str(confidence)
    elif set == "all":
        return f"Detected(lang={detected_lang}, confidence={confidence})"
    else:
        return "Неправильний параметр set"


def CodeLang(lang: str):
    try:
        detected_lang = detect(lang)
        return detected_lang
    except:
        return "Мова не знайдена"



def LanguageList(out: str = "screen", text: str = None):
    header = "N Language      ISO-639 code Text"
    separator = "-" * 60
    translator = GoogleTranslator(source='auto', target='en')  # create an instance of GoogleTranslator
    supported = translator.get_supported_languages(as_dict=True)

    translations = []

    for index, (code, lang) in enumerate(supported.items(), 1):
        translated_text = TransLate(text, 'auto', dest=code) if text else ""
        translations.append(f"{index:<2} {lang:<12} {code:<12} {translated_text}")

    output = "\n".join([header, separator] + translations + ["Ok"])

    if out == "screen":
        return output
    elif out == "file":
        filename = "language_list_deept.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(output)
        return f"Таблиця збережена у файлі: {filename} \n Ok"
    else:
        return "Неправильний параметр out"
