import os
import time
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

oswald = pyttsx3.init() # инициализация говорилки

voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\TokenEnums\\RHVoice\\Aleksandr"

# настройки синтеза речи
oswald.setProperty("rate", 180)
oswald.setProperty("volume", 1)
oswald.setProperty("voice", voice_id)

answers = ['Хорошо', 'Окей', 'Будет сделано', 'Без проблем', 'Сию минуту', 'Одну минуту']

# Основной класс, функциональность

class Oswald:
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
			print("start")
			content_data = data.listen(source, phrase_time_limit=5) 

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
		os.chdir("C:\\Users\\Жангир\\Music") # Меняю директорию на music

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
			print("говорите...")
			content_data = data.listen(source, phrase_time_limit=5) 

		try:
			content = data.recognize_google(content_data, language="ru-RU")
			print(content)
			webbrowser.open(f'https://yandex.kz/search/?text={content}')
		except sr.UnknownValueError:
			pass

	def shutdown_os():
		oswald.say(random.choice(answers))
		oswald.runAndWait()
		os.system("shutdown /s /t 30")
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

	def telegram():
		oswald.say(random.choice(answers))	
		os.system("start D:\\Telegram\\Telegram.exe")
		oswald.runAndWait() 

	def currency_rate():
		URL = "https://yandex.kz/"	
		HEADERS = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
		}

		query = requests.get(URL, headers = HEADERS)
		soup = BeautifulSoup(query.content, "html.parser")

		items = soup.findAll("span", class_="inline-stocks__value_inner")

		oswald.say(f"Нынешний курс доллара сейчас составляет {items[0].get_text(strip=True)} тенге.")
		oswald.say(f"Нынешний курс евро сейчас составляет {items[1].get_text(strip=True)} тенге.")
		oswald.say(f"Нынешний курс рубля сейчас составляет {items[2].get_text(strip=True)} тенге.")

		oswald.runAndWait()

	def news(): #последние новости
		URL = "https://tengrinews.kz/"
		HEADERS = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
		}

		query = requests.get(URL, headers = HEADERS)
		soup = BeautifulSoup(query.content, "html.parser")

		latest_news = soup.findAll("span", class_="tn-main-news-title")

		for news in latest_news:
			oswald.say(f"{news.get_text(strip=True)} \n")
			oswald.runAndWait()