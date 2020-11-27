import speech_recognition as sr
import time
from fuzzywuzzy import fuzz
from assistent import Oswald
from talk import Talk 

alias = ['асфальт', "бро", "бра", "друг",  "асфальтик", "асфальтыч", 'не мог бы ты', 'пожалуйста', "скажи", "найди"]

read_data = sr.Recognizer() # инициализирую объект который распознает речь

cmds = {
	"hello":("привет", "асфальт", "бро", "братан", "эй ты", "здарова", "здравствуй", "приветик",),
	"dela": ("как дела", "как поживаешь","как жизнь"),
	"clock":("текущее время", "время", "который час", "системное время", "часы"),
	"music":("музыка", "вруби музыку", "аудиоплеер", "рандомная песня"),
	"weather":("погода", "текущая погода", "температура на улице", "какая погода"),
	"biography": ("биография", "кто ты", "твоя история", "расскажи о себе",),
	"browser": ("открой браузер", "браузер", "открой интернет"),
	"youtube": ("открой youtube", "youtube",),
	"shutdown_os": ("выруби комп", "выключи компьютер"),
	"kino": ("кино", "включи кино"),
	"anime": ("аниме", "включи аниме", "открой аниме"),
	'telegram': ("открой телегу", ),
	'thanks':('спасибо', 'спасибки', 'благодарю', 'спасибо бро'),
	'keepnotes': ('запиши в заметках', 'запиши в блокноте', 'сделай заметку'),
	'web_browse': ('найди в интернете', 'поищи в интернете','поищи в сети',),
	'exit': ('пока', 'закройся', 'уйди',),
}

# функция для замены не нужных фраз 
def replace_phrase(text): 
	for phrase in alias:
		text = text.replace(phrase, '').strip()
		text = text.replace('  ', ' ').strip()
		return text

# функция сравнения запроса и элементов в словаре
def comparison(query, cmds_item):
	
		for i in cmds[cmds_item]:
	
			comparison_value = fuzz.ratio(query, i)

			if comparison_value >= 60:
				return True
			else:
				return False


def response(execute_item):
		cmds_methods = {
			"clock": Oswald.clock,
			"music": Oswald.music,
			"kino": Oswald.kino,
			"anime": Oswald.anime,
			"weather": Oswald.weather,
			"browser": Oswald.browser,
			"youtube": Oswald.youtube,
			"shutdown_os":  Oswald.shutdown_os,
			'telegram': Oswald.telegram,
			'keepnotes': Oswald.keepnotes,
			'web_browse': Oswald.web_browse,
			"biography": Talk.biography, 
			'thanks': Talk.thanks,
			"hello": Talk.hello,
			"dela": Talk.dela,
			'exit': Talk.exit_cmd,
		}

		# пробегаемся по списку с функциями, если функцию подходит переданному значению то вызываем метод
		
		for i in cmds_methods: 
			if i == execute_item:
				cmds_methods[i]()

# сам интерфейс
def waiter():
	# прослушиваем микрофон и даем ему имя source
	with sr.Microphone(device_index=1) as source: 
		print("Running...")
		read_data.adjust_for_ambient_noise(source)
		audio_data = read_data.listen(source, phrase_time_limit=5)

	try:
		query = replace_phrase(read_data.recognize_google(audio_data, language="ru-RU"))
		query = query.lower()
		print(query)
	except (sr.UnknownValueError):
		pass	

 	# пробегаемся по словарю cmds, проверяем текст и если условие верно то вызываем метод и передаем имя кортежа

	for i in cmds:
		if comparison(query, i):
			response(i)
try:
	waiter()
except KeyboardInterrupt:
	exit()