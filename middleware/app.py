from flask import Flask, render_template
from twilio.rest import Client
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sms')
def send_text():
    account_sid = 'ACe0cad0adc0ff1f750b61e94c566d1fa2'
    auth_token = '5bc8a5f9347360d81055a843ca03a247'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        body="Welcome to the SDG Hackathon",
                        from_='+19292051436',
                        to='+16462676977'
                    )

if __name__ == '__main__':
    app.run()

