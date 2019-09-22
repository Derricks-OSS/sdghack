from flask import Flask, render_template
from twilio.rest import Client
import pyowm
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sms')
def send_text():
    msg = 'Welcome to the SDG Hackathon!'
    account_sid = 'ACe0cad0adc0ff1f750b61e94c566d1fa2'
    auth_token = '5bc8a5f9347360d81055a843ca03a247'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        body="{}".format(msg),
                        from_='+19292051436',
                        to='+16462676977'
                    )
    return msg


@app.route('/weather')
def get_weather():
    city = 'New York'
    owm = pyowm.OWM('7b455f897e82a55c1aa80ed8f1d3428d')
    observation = owm.weather_at_place('{}, US'.format(city))
    weather = observation.get_weather()
    temperature = weather.get_temperature('fahrenheit')['temp']
    wind = weather.get_wind('miles_hour')['speed']
    humi = weather.get_humidity()
    status = weather.get_detailed_status()
    rain = weather.get_rain()
    ans = ' Weather of {}:\ntemperature: {} (F), \nwind speed: {} (mph), \nhumidity: {}, \nstatus: {}, \nrain: {} '.format(city, temperature, wind, humi,status,rain)
    ans = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'\n'+ ans
    return ans


if __name__ == '__main__':
    app.run()

