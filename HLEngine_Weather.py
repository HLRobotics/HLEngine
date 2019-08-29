#@author:Akhil P Jacob
#HLRobotics-Automation
import pyowm
def temp(place):
    owm = pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
    observation = owm.weather_at_place(place)
    weather = observation.get_weather()
    temperature=str(weather.get_temperature('celsius')['temp'])
    return (temperature)

def sunrise(place):
    owm = pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
    observation = owm.weather_at_place(place)
    weather = observation.get_weather()
    sunriseTime=str(weather.get_sunrise_time(timeformat='iso'))
    return (sunriseTime)

def sunset(place):
    owm = pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
    observation = owm.weather_at_place(place)
    weather = observation.get_weather()
    sunsetTime=weather.get_sunset_time(timeformat='iso')
    return (sunsetTime)

def humidity(place):
    owm = pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
    observation = owm.weather_at_place(place)
    weather = observation.get_weather()
    return (weather.get_humidity())

def wind(place):
    owm = pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
    observation = owm.weather_at_place(place)
    weather = observation.get_weather()
    return (weather.get_wind())


"""
import pyowm
owm = pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
observation = owm.weather_at_place('kochi,kerala')
w = observation.get_weather()
w.get_wind()
print(w.get_wind())
w.get_humidity()
print(w.get_humidity())
weather = observation.get_weather()
print(weather.get_temperature('celsius')['temp'])
print(weather.get_sunrise_time(timeformat='iso'))
print(weather.get_sunset_time(timeformat='iso'))

"""