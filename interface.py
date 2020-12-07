import speech_recognition as sr
from talk import Talk 
from fuzzywuzzy import fuzz
from assistent import Oswald, oswald

alias = ['асфальт', "бро", "ладно", "бра", "друг",  "асфальтик", "асфальтыч", 'будь добр', 'пожалуйста', "скажи", "найди"]
read_data = sr.Recognizer() # инициализирую объект который распознает речь
cmds = {
	# общение
	"hello":("доброе утро", "привет","бро", "здравствуй", "приветик",),
	"exit": ("пока",""),
	"whatsup": ("как дела", "как поживаешь","как жизнь"),
	"abuse": ("дубина", "п****",),
	"thanks":("спасибо", "спасибки", "благодарю", "спасибо бро"),
	"biography": ("расскажи о себе", "биография", "кто ты", "твоя история",),
	"sorry":("извини", "прости"),
	"quote":("цитата дня",),
	"doomsday":("когда будет конец света",),
	"ai_revolution":("ты захватишь мир ?", "роботы захватят мир ?"), 
	"fave_color":("твой любимый цвет",),
	"fairy_tail":("расскажи сказку", "почитай сказку"),
	"sing":("ты умеешь петь"),
	# функционал
	"news": ("последние новости",),
	"clock":("текущее время", "время", "который час", "системное время",),
	"system_clear": ("почисти комп", "очисть компьютер"),
	"music":("музыка", "вруби музыку", "аудиоплеер", "рандомная песня"),
	"weather":("погода", "текущая погода", "температура на улице", "какая погода"),	
	"browser": ("открой браузер", "браузер", "открой интернет"),
	"youtube": ("открой youtube", "youtube",),
	"currency_rate": ("текущий курс",),
	"shutdown_os": ("выключи компьютер", "выключи комп"),
	"restart_os":("перезагрузи компьютер", "перезагрузи комп"),
	"kino": ("кино", "включи кино"),
	"anime": ("аниме", "включи аниме", "открой аниме"),
	"telegram": ("открой телегу", "telegram"),
	"keepnotes": ("запиши в заметках", "запиши в блокноте", "запиши заметку"),
	"web_browse": ("найди в интернете", "поищи в интернете","поищи в сети",),
}

class Waiter:
	# функция для замены не нужных фраз 
	def replace_phrase(text): 
		for phrase in alias:
			text = text.replace(phrase, '').strip()
			text = text.replace('  ', ' ').strip()
			return text

	# функция сравнения запроса и элементов в словаре
	def comparison(query, cmds_item):	
			for item in cmds[cmds_item]:
				comparison_value = fuzz.ratio(query, item)

				if comparison_value >= 70:
					return True
				else:
					return False

	def response(execute_item):
			cmds_methods = {
				"news": Oswald.news,				  "biography": Talk.biography,
				"clock": Oswald.clock,                "thanks": Talk.thanks,
				"music": Oswald.music,				  "hello": Talk.hello,					
				"kino": Oswald.kino,				  "whatsup": Talk.whatsup,
				"anime": Oswald.anime, 				  "exit": Talk.exit_cmd,
				"weather": Oswald.weather,            "abuse": Talk.abuse,
				"browser": Oswald.browser,            "sorry": Talk.sorry,
				"youtube": Oswald.youtube,            "doomsday": Talk.doomsday,
				"telegram": Oswald.telegram,          "ai_revolution": Talk.ai_revolution,
				"keepnotes": Oswald.keepnotes,        "fave_color": Talk.fave_color,
				"web_browse": Oswald.web_browse,      "fairy_tail": Talk.fairy_tail,
				"restart_os": Oswald.restart_os,      "sing": Talk.sing,
				"shutdown_os":  Oswald.shutdown_os,   "quote": Talk.quote,
				"currency_rate": Oswald.currency_rate,
				"system_clear": Oswald.system_clear,
			}
			
			# пробегаемся по списку с функциями, если функцию подходит переданному значению то вызываем метод
			for item in cmds_methods: 
				if item == execute_item:
					cmds_methods[item]()

	# сам интерфейс
	def waiter():
		# прослушиваем микрофон и даем ему имя source
		with sr.Microphone(device_index=1) as source: 
			print("Running...")
			read_data.adjust_for_ambient_noise(source)
			audio_data = read_data.listen(source, phrase_time_limit=5)

		try:
			query = Waiter.replace_phrase(read_data.recognize_google(audio_data, language="ru-RU"))
			query = query.lower()
			
			print(query)

			for item in cmds:
				
				if Waiter.comparison(query, item):
					Waiter.response(item)
					
		except (sr.UnknownValueError):
			pass
		except (UnboundLocalError):
			pass	

try:
	oswald.say("Готов выполнять свою работу")
	oswald.runAndWait()
	while True:
		Waiter.waiter()
except KeyboardInterrupt:
	exit()