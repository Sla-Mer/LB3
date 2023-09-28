from Translation_Package.DeepT_Funcs import *

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

print("\nLanguageList функція:")
print(LanguageList(out="screen", text="Lang Lebe Der König"))