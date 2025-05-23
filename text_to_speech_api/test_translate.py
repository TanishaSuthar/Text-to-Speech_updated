import argostranslate.translate

argostranslate.translate.load_installed_languages()
installed_languages = argostranslate.translate.get_installed_languages()

for from_lang in installed_languages:
    for to_lang in installed_languages:
        if from_lang != to_lang:
            translation = from_lang.get_translation(to_lang)
            if translation:
                print(f"Installed translation: {from_lang.code} → {to_lang.code}")
