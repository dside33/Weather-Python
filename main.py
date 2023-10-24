import eel
import pyowm
import pyttsx3

owm = pyowm.OWM('93a9745bfd3edf03c94fdf627f7a958b')

@eel.expose
def get_weather(place):
	mgr = owm.weather_manager()

	observation = mgr.weather_at_place(place)
	w = observation.weather

	temp = w.temperature('celsius')['temp']

	return 'В городе ' + place + ' сейчас ' + str(temp) + ' градусов!'

@eel.expose
def voice_response(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

eel.init('web')
eel.start('main.html', size = (700,700))