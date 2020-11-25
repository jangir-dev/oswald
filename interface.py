import speech_recognition as sr
import time
from fuzzywuzzy import fuzz
from assistent import Oswald 

alias = ['асфальт', "бро", "бра", "друг",  "асфальтик", "асфальтыч", 'не мог бы ты', 'пожалуйста', "скажи", "найди"]

cmds = {
	"hello":("привет", "асфальт", "бро", "братан", "эй ты", "здарова", "здравствуй", "приветик",),
	"dela": ("как дела", "как поживаешь","как жизнь"),
	"clock":("текущее время", "время", "который час", "системное время", "часы"),
	"music":("музыка", "вруби музыку", "аудиоплеер", "рандомная песня"),
	"weather":("погода", "текущая погода", "температура на улице", "какая погода"),
	"biography": ("биография", "твоя история", "расскажи о себе", "кто ты"),
	"browser": ("открой браузер", "браузер", "открой интернет"),
	"youtube": ("открой youtube", "youtube",),
	"shutdown_os": ("выруби комп", "выключи компьютер"),
	"kino": ("кино", "включи кино"),
	"show_cmds": ("твои команды", "команды"),
	"anime": ("аниме", "включи аниме", "открой аниме"),
	'telegram': ("открой телегу", "открой телеграм"),
	'thanks':('спасибо', 'спасибки', 'благодарю', 'спасибо бро'),
	'keepnotes': ('запиши в заметках', 'запиши в блокноте', 'сделай заметку'),
	'web_browse': ('найди в интернете', 'поищи в интернете','поищи в сети',),
	'exit': ('пока', 'закройся', 'уйди',),
}


# сторонние функции
# функция для замены не нужных фраз 
def replace_phrase(text): 
	for phrase in alias:
		text = text.replace(phrase, '').strip()
		text = text.replace('  ', ' ').strip()
		return text

# функция сравнения запроса и элементов в словаре
def comparison(query, cmds_item):
	if query in cmds[cmds_item]:
		for i in cmds[cmds_item]:
			comparison_value = fuzz.partial_ratio(query, i)

			if comparison_value >= 40:
				return True
			else:
				return False

read_data = sr.Recognizer() # инициализирую объект который распознает речь

# сам интерфейс
def waiter():
	with sr.Microphone(device_index=1) as source: # прослушиваем микрофон и даем ему имя source
		print("Running...")
		read_data.adjust_for_ambient_noise(source)
		audio_data = read_data.listen(source, phrase_time_limit=5)

	try:
		query = replace_phrase(read_data.recognize_google(audio_data, language="ru-RU"))
		text = query.lower()
		print(text)
		time.sleep(6)
	except sr.UnknownValueError:
		pass 


	if comparison(text, "weather"):
		Oswald.weather()
	elif comparison(text, "clock"):
		Oswald.clock()
	elif comparison(text, "music"):
		Oswald.random_music()
	elif comparison(text, "youtube"):
		Oswald.youtube()
	elif comparison(text, "biography"):
		Oswald.biography()
	elif comparison(text, "browser"):
		Oswald.browser()	
	elif comparison(text, "shutdown_os"):
		Oswald.shutdown_os()
	elif comparison(text, "anime"):
		Oswald.anime()
	elif comparison(text, "dela"):
		Oswald.dela()
	elif comparison(text, "show_cmds"):
		Oswald.show_cmds()
	elif comparison(text, "kino"):
		Oswald.kino()
	elif comparison(text, "telegram"):
		Oswald.telegram_open()
	elif comparison(text, "thanks"):
		Oswald.thanks()
	elif comparison(text, "hello"):
		Oswald.hello()
	elif comparison(text, "exit"):
		Oswald.exit_cmd()
	elif comparison(text, 'keepnotes'):
		Oswald.keep_notes()
	elif comparison(text, 'web_browse'):
		Oswald.web_browse()

Oswald.welcome()

try:
	while True:
		waiter()
except KeyboardInterrupt:
	pass