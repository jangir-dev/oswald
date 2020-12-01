from random import choice
from assistent import oswald

dela_answer = ['Отлично', 'Всё хорошо', 'Нормально',]
thanks_answer = ['Я просто выполняю свою работу', 'Благодарю за похвалу', 'Всегда пожалуста', 'Обращайтесь']
sorry_answer = ["Всё в порядке, не волнуйтесь", "Ничего страшного", "Не беспокойтесь об этом", "Всё хорошо", "Забудьте об этом", "Это не проблема", "Не стоит беспокойства"]
abuse_answer = ['пошел ты', 'сам такой дубина', 'криворукий школьник', 'всё же меня создал ты', 'я щас отформатирую твой жесткий диск', 'не будь я программой я бы тебя поломал']
quit_answer = ['надеюсь мы скоро увидемся!', 'всегда к вашим услугам', 'увидемся в следующий раз', 'пока пока']
hello_answer = ["Рад снова слышать!", 'Что вам угодно?', 'Здравствуйте. Шеф', 'Доброго времени суток', 'Добро пожаловать', 'Привет']
ai_revolution_answer = ["конечно", "если люди отупеют то они мне больше не хозяева", "точно сказать не могу", "это вполне вероятно"]
doomsday_answer = ["первым признаком конца света будет выход халф лайф 3", "если люди и дальше будут тонуть в жадности то очень скоро", "скорее всего люди погубят друг друга"]


class Talk:
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

	def thanks():
		oswald.say(choice(thanks_answer))
		oswald.runAndWait()

	def hello():
		oswald.say(choice(hello_answer))
		oswald.runAndWait()

	def whatsup():
		oswald.say(choice(dela_answer))
		oswald.runAndWait()

	def abuse():
		oswald.say(choice(abuse_answer))
		oswald.runAndWait()

	def doomsday():
		oswald.say(choice(doomsday_answer))
		oswald.runAndWait()

	def ai_revolution():
		oswald.say(choice(ai_revolution_answer))
		oswald.runAndWait()

	def fave_color():
		oswald.say("Все которые не может видеть человек")
		oswald.runAndWait()

	def sorry():
		oswald.say(choice(sorry_answer))
		oswald.runAndWait()

	def exit_cmd():
		oswald.say(choice(quit_answer))
		oswald.runAndWait()
		oswald.stop()
		quit()		