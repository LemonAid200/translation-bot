import translators as ts
import translators.server as tss

def translate(text, from_lang = 'en', to_lang = 'ru'):
	try:
		return tss.google(text, from_lang, to_lang)
	except:
		return 'Я пока глупый бот, перевожу только черный текст на белом фоне, и то не всегда :( Но вы можете перепечатать текст, я его переведу!'