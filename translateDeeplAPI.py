import deepl
import config

translator = deepl.Translator(config.DEEPL_AUTH_KEY)

def translate(text_to_translate, source_lang = "EN", target_lang = "FR"):
	return translator.translate_text(text_to_translate, source_lang=source_lang, target_lang=target_lang).text
