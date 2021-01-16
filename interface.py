import speech_recognition as sr
from fuzzywuzzy import fuzz
from functionality import Oswald, Talk, oswald

alias = ['асфальт', "бро", "ладно", "бра", "друг",  "асфальтик", "асфальтыч", 'будь добр', 'пожалуйста', "скажи", "найди"]
read_data = sr.Recognizer()

cmds = {
	# общение
	"talk": {
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
	},
	# функционал
	"oswald": {
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
}

class Interface:
	def replace_phrase(text): # Удаляет ненужные фразы, очищает запрос пользователя
		for to_replace in alias:
			text = text.replace(to_replace, "").strip()
			text = text.replace("  ", " ")

		return text

	def response(item):
		for i in cmds["talk"]:   # Ответ бота
			if item in cmds["talk"][i]:
				response = Talk(i)
			else:
				for i in cmds["oswald"]:
					if item in cmds["oswald"][i]:
						response = Oswald(i)
		try:
			response.answer()
		except AttributeError:
			pass			
	
	def hear(): # Функция для приема запросов пользователя через микрофон
		# прослушиваем микрофон и даем ему имя source
		with sr.Microphone(device_index=1) as source: 
			print("Running...")
			read_data.adjust_for_ambient_noise(source)
			audio_data = read_data.listen(source, phrase_time_limit=5)

		try:
			query = Interface.replace_phrase(read_data.recognize_google(audio_data, language="ru-RU")).lower()
			print(query)
			Interface.response(query)
					
		except (sr.UnknownValueError, UnboundLocalError):
			pass

try:
	oswald.say("Готов к работе")
	oswald.runAndWait()

	while True:
		Interface.hear()

except KeyboardInterrupt:
	pass