import argostranslate.package
import argostranslate.translate

def print_installed_languages():
    installed_languages = argostranslate.translate.get_installed_languages()
    print(f"Installed languages: {[lang.code for lang in installed_languages]}")

def print_installed_translations():
    installed_languages = argostranslate.translate.get_installed_languages()
    print("Installed translation pairs:")
    for from_lang in installed_languages:
        for to_lang in installed_languages:
            if from_lang != to_lang:
                translation = from_lang.get_translation(to_lang)
                if translation:
                    print(f"  {from_lang.code} → {to_lang.code}")

print("Before installation:")
print_installed_languages()
print_installed_translations()

# Install English → Hindi model
model_en_hi = "translate-en_hi-1_1.argosmodel"  # path to your English→Hindi model
argostranslate.package.install_from_path(model_en_hi)

# Install Hindi → English model
model_hi_en = "translate-hi_en-1_1.argosmodel"  # path to your Hindi→English model
argostranslate.package.install_from_path(model_hi_en)

# Reload languages after installation
argostranslate.translate.load_installed_languages()

print("\nAfter installation:")
print_installed_languages()
print_installed_translations()
