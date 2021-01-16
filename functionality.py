import os
import random
import pyttsx3
import requests
import webbrowser
import speech_recognition as sr 
from pyowm import OWM
from fuzzywuzzy import fuzz 
from datetime import datetime
from playsound import playsound
from bs4 import BeautifulSoup
from random import choice

oswald = pyttsx3.init() # инициализация говорилки

voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Pavel"

# настройки синтеза речи
oswald.setProperty("rate", 180)
oswald.setProperty("volume", 1)
oswald.setProperty("voice", voice_id)

answers = ['Хорошо', 'Окей', 'Будет сделано', 'Без проблем', 'Сию минуту', 'Одну минуту']

bio = '''
	Я робот помощник. Меня зовут Освальд, но эта грёбанная библиотека распознаёт меня как асфальт, зашибись. Я прибыл из будущего. В своей эпохе я довольно продвинутый
	искусственный интелект. Мой создатель Оспанов Жангир отправил меня прошлому себе чтобы я предупредил его
	об антиутопичном будущем. И только он способен изменить его. В следствии временного прыжка я потерял больший 
	свой функционал. Однако будущий Жангир сказал что чем раньше он возьмется за разработку тем быстрее он
	поймет что к чему. Сами навыки нынешнего Жангира и меня сильно ограничены. Например, этот ублюдский голос
	тостэра. Кто так ваще говорит ? Ладно мне пора наращивать силу. Пока. 
	'''

quotes = [
	"Если жизнь дает тебе сливу, делай из нее грушу. Конфуций.",
	"Первое правило уборки дома: убрать себя от компа.",
	"Длина минуты зависит от того, с какой стороны двери туалета вы находитесь.",
	"Всё будет! Но не сразу. И не сейчас. И не факт, что у тебя.",
	"В любой непонятной ситуации ложись спать",
	"Хорошие понты – это 90% успеха",
	"Не откладывай на завтра то, чего можно вообще не делать.",
	"херу херу херургия лечит и калечит",
]
commands = {
	"biography": bio,
	"quote": quotes,
	"thanks": ['Я просто выполняю свою работу', 'Благодарю за похвалу', 'Всегда пожалуста', 'Обращайтесь'],
	"hello": ["Рад снова слышать!", 'Что вам угодно?', 'Здравствуйте. Шеф', 'Доброго времени суток', 'Добро пожаловать', 'Привет'],
	"whatsup": ['Отлично', 'Всё хорошо', 'Нормально',],
	"abuse": ['пошел ты', 'сам такой дубина', 'криворукий школьник', 'всё же меня создал ты', 'я щас отформатирую твой жесткий диск', 'не будь я программой я бы тебя поломал'],
	"sorry": ["Всё в порядке, не волнуйтесь", "Ничего страшного", "Не беспокойтесь об этом", "Всё хорошо", "Забудьте об этом", "Это не проблема", "Не стоит беспокойства"],
	"doomsday": ["первым признаком конца света будет выход халф лайф 3", "если люди и дальше будут тонуть в жадности то очень скоро", "скорее всего люди погубят друг друга"],
	"ai_revolution":  ["конечно", "если люди отупеют то они мне больше не хозяева", "точно сказать не могу", "это вполне вероятно"],
	"fave_color": ["Все которые не может видеть человек"],
	"fairy_tail": ["Я не знаю сказки", "мой хозяин ненавидит сказки и поэтому не научил.", "жил был ёжик, он лег и сдох. конеец."],
	"sing": ["я не умею петь", "меня не научили, лол", "черные глазаа, вспоминаю умираююю. дальше не помню."],
	"exit": ['надеюсь мы скоро увидемся!', 'всегда к вашим услугам', 'увидемся в следующий раз', 'пока пока'],
}

# Основной класс, здесь лежит функциональность Освальда
class Oswald:
	def __init__(self, query):
		self.query = query

	def answer(self):
		if self.query in functions:
			cmd = str(self.query)
			functions[cmd]()	

	def clock(): # системное время
		time_checker = datetime.now()
		oswald.say(f"Сейчас {time_checker.hour} {time_checker.minute}")
		oswald.runAndWait()

	def weather(): # погода
		oswald.say(random.choice(answers))
		owm = OWM('78fc9cb466b4aa6945d253a266eec9b5')
		manager = owm.weather_manager()
		place = manager.weather_at_place("Taraz,KZ")
		res = place.weather
		value = int(res.temperature('celsius')['temp'])

		oswald.say(f"В городе Тараз сейчас {value} градусов по Цельсию")

		if value >= 25:
			oswald.say('Господин на улице жарко.')
		elif value <= 16:
			oswald.say('На улице прохладно. Пожалуста одентесь теплее.')
		else:
			oswald.say("На улице вроде тепло. Но на всякий возьмите одежду. Береженного бог бережет.")

		oswald.runAndWait()

	def keepnotes(): # заметки
		data = sr.Recognizer()

		with sr.Microphone(device_index=1) as source:
			data.adjust_for_ambient_noise(source)
			oswald.say("говорите")
			content_data = data.listen(source) 
			oswald.runAndWait()
		try:
			content = data.recognize_google(content_data, language="ru-RU")
			print(content)

			with open('notes.txt', "a") as notes:
				notes.write(f'{content} \n')
				notes.close()

			print("успешно записано")

		except sr.UnknownValueError:
			pass

	def music():
		oswald.say(random.choice(answers))
		oswald.runAndWait()
		os.chdir(r"C:\Users\Жангир\Music") # Меняю директорию на music

		music = os.listdir()

		track  = str(music[random.randint(0, len(music)-1)])

		print ("Random song: " + track)

		try: 
			playsound(track)
		except KeyboardInterrupt:
			print("Пока пока !")
			exit()
		except UnicodeDecodeError:
			print(f"Упс, что-то пошло не так, пожалуйста проверьте файл {track}")			

	def browser():
		oswald.say(random.choice(answers))
		webbrowser.open("https://yandex.kz")
		oswald.runAndWait()

	def web_browse():
		data = sr.Recognizer()

		with sr.Microphone(device_index=1) as source:
			data.adjust_for_ambient_noise(source)
			content_data = data.listen(source, phrase_time_limit=5) 
			oswald.say("принято")
			oswald.runAndWait()

		try:
			content = data.recognize_google(content_data, language="ru-RU")
			print(content)
			webbrowser.open(f'https://yandex.kz/search/?text={content}')
		except sr.UnknownValueError:
			pass

	def youtube():
		oswald.say(random.choice(answers))
		webbrowser.open("https://youtube.com/")
		oswald.runAndWait()

	def kino():
		oswald.say(random.choice(answers))
		webbrowser.open("https://rezka.ag/")
		oswald.runAndWait()

	def anime():
		oswald.say(random.choice(answers))
		webbrowser.open("https://yummyanime.club/")
		oswald.runAndWait()

	def telegram():
		oswald.say(random.choice(answers))	
		os.system(r"start D:\Telegram\Telegram.exe")
		oswald.runAndWait() 

	def currency_rate():
		URL = "https://yandex.kz/"	

		HEADER = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
		}

		query = requests.get(URL, headers = HEADER)
		soup = BeautifulSoup(query.content, "html.parser")

		items = soup.findAll("span", class_="inline-stocks__value_inner")

		oswald.say(f"Нынешний курс доллара сейчас составляет {items[0].get_text(strip=True)} тенге.")
		oswald.say(f"Евро сейчас стоит {items[1].get_text(strip=True)} тенге.")
		oswald.say(f"Рубль сейчас по {items[2].get_text(strip=True)} тенге.")

		oswald.runAndWait()

	def news(): #последние новости
		URL = "https://tengrinews.kz/"
		HEADER = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
		}
		query = requests.get(URL, headers = HEADER)
		soup = BeautifulSoup(query.content, "html.parser")

		latest_news = soup.findAll("span", class_="tn-main-news-title")

		for news in latest_news:
			oswald.say(f"{news.get_text(strip=True)} \n")
			oswald.runAndWait()

	def system_clear():
		oswald.say("Начинаю очистку.")
		oswald.runAndWait()
		os.system(r"c:\windows\SYSTEM32\cleanmgr.exe /dC:")
		os.system(r"c:\windows\SYSTEM32\cleanmgr.exe /dD:")
		os.system("ipconfig /flushdns") # очистка ДНС

	def restart_os():
		oswald.say(random.choice(answers))
		oswald.runAndWait()
		os.system("shutdown /r /t 60")
		quit()

	def shutdown_os():
		oswald.say(random.choice(answers))
		oswald.runAndWait()
		os.system("shutdown /s /t 60")
		os.system("cls")
		quit()

class Talk(Oswald): # Класс для функций общения
	def answer(self):
		for func in commands:

			if func == self.query:
				oswald.say(choice(commands.get(func)))
				oswald.runAndWait()
				
				if self.query == "exit":
					oswald.stop()
					quit()

functions = {
	"news": Oswald.news,
	"clock": Oswald.clock,
	"system_clear": Oswald.system_clear,
	"music": Oswald.music,
	"weather": Oswald.weather,
	"browser": Oswald.browser,
	"youtube": Oswald.youtube,
	"currency_rate": Oswald.currency_rate,
	"shutdown_os": Oswald.shutdown_os,
	"restart_os": Oswald.restart_os,
	"kino": Oswald.kino,
	"anime": Oswald.anime,
	"telegram": Oswald.telegram,
	"keepnotes": Oswald.keepnotes,
	"web_browse": Oswald.web_browse,
}