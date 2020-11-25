import os
import pyttsx3
import webbrowser
import random
import time
import speech_recognition as sr 
from fuzzywuzzy import fuzz 
from playsound import playsound
from datetime import datetime
from pyowm import OWM

oswald = pyttsx3.init() # инициализация говорилки

voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\TokenEnums\\RHVoice\\Aleksandr"

# настройки синтеза речи
oswald.setProperty("rate", 170)
oswald.setProperty("volume", 1)
oswald.setProperty("voice", voice_id)

hello_answer = ["Рад снова вас слышать!", 'Что вам угодно?', 'Здравствуйте. Шеф', 'Доброго времени суток', 'Добро пожаловать', 'Привет']
thanks_answer = ['Я просто выполняю свою работу', 'Благодарю за похвалу', 'Всегда пожалуста', 'Обращайтесь']
dela_answer = ['Отлично', 'Всё хорошо', 'Нормально', 'Кееремет']
quit_answer = ['надеюсь мы скоро увидемся!', 'рад был помочь', 'всегда к вашим услугам', 'увидемся в следующий раз', 'пока пока']
answers = ['Хорошо', 'Окей', 'Будет сделано', 'Без проблем', 'Сию минуту', 'Одну минуту']

# Основной класс, функциональность

class Oswald:

	def biography(): # биография 
		bio = '''
		Я робот помощник. Меня зовут Освальд, но эта грёбанная библиотека распознаёт меня как асфальт, зашибись. Я прибыл из будущего. В своей эпохе я довольно продвинутый
		искусственный интелект. Мой создатель Оспанов Жангир отправил меня прошлому себе чтобы я предупредил его
		об антиутопичном будущем. И только он способен изменить его. В следствии временного прыжка я потерял больший 
		свой функционал. Однако будущий Жангир сказал что чем раньше он возьмется за разработку тем быстрее он
		поймет что к чему. Сами навыки нынешнего Жангира и меня сильно ограничены. Например, этот ублюдский голос
		тостэра. Кто так ваще говорит ? Ладно мне пора наращивать силу. Пока. 
		'''
		oswald.say(bio)
		oswald.runAndWait()	

	def welcome():
		oswald.say(random.choice(hello_answer))
		oswald.runAndWait()	

	def clock(): # системное время
		time_checker = datetime.now()
		oswald.say(f"{time_checker.hour} часов {time_checker.minute} минут")
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

	def keep_notes(): # заметки
		data = sr.Recognizer()

		with sr.Microphone(device_index=1) as source:
			data.adjust_for_ambient_noise(source)
			print("start")
			content_data = data.listen(source, phrase_time_limit=5) 

		try:
			content = data.recognize_google(content_data, language="ru-RU")
			print(content)

			with open('notes.txt', "w") as notes:
				notes.write(f'{content} \n')
				notes.close()

			print("успешно записано")

		except sr.UnknownValueError:
			pass

	def random_music():
		oswald.say(random.choice(answers))
		oswald.runAndWait()
		os.chdir("C:\\Users\\Жангир\\Music") # Меняю директорию на music

		music = os.listdir()

		track  = str(music[random.randint(0, len(music)-1)])

		print ("Random song: " + track)

		try: 
			playsound(track)
		except KeyboardInterrupt:
			print("Пока пока !")
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
			oswald.say("Что мне искать ?")
			content_data = data.listen(source, phrase_time_limit=5) 

		try:
			content = data.recognize_google(content_data, language="ru-RU")
			print(content)
			webbrowser.open(f'https://yandex.kz/search/?text={content}')
		except sr.UnknownValueError:
			pass

		oswald.runAndWait()

	def shutdown_os():
		oswald.say(random.choice(quit_answer))
		oswald.runAndWait()
		os.system("shutdown /s /t 10")
		os.system("cls")
		quit()

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

	def dela():
		oswald.say(random.choice(dela_answer))
		oswald.runAndWait()

	def telegram_open():
		oswald.say(random.choice(answers))	
		os.system("start D:\\Telegram\\Telegram.exe")
		oswald.runAndWait()

	def thanks():
		oswald.say(random.choice(thanks_answer))
		oswald.runAndWait()

	def hello():
		oswald.say(random.choice(hello_answer))
		oswald.runAndWait()

	def exit_cmd():
		oswald.say(random.choice(quit_answer))
		oswald.runAndWait()
		oswald.stop()
		quit()
