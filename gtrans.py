from Translation_Package.gtarns_module import *

text = "Lang Lebe Der König!"
print(f"Текст: {text}")
print(LangDetect(text))
print("------------------------")

dest_lang = "en"
print(f"Перекладено з {LangDetect(text, 'lang')} на {dest_lang}: {TransLate(text, scr='auto', dest=dest_lang)}")
print("------------------------")

lang_name = "English"
print(f"Код мови для {lang_name}: {CodeLang(lang_name)}")
print("------------------------")

lang_code = "en"
print(f"Мова для {lang_code}: {CodeLang(lang_code)}")
print("------------------------")

print("\nLanguageList функція:")
print(LanguageList(out="screen", text="Lang Lebe Der König"))