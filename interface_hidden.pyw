from interface import Waiter

try:
	while True:
		Waiter.waiter()
except KeyboardInterrupt:
	exit()