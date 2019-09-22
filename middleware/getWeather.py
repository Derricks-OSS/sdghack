import pyowm
city = 'New York'
owm = pyowm.OWM('7b455f897e82a55c1aa80ed8f1d3428d')
observation = owm.weather_at_place('{}, US'.format(city))
weather = observation.get_weather()
temperature = weather.get_temperature('fahrenheit')['temp']
print('The temperature in {} is:'.format(city),temperature)

print(weather.get_time)