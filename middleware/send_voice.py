from twilio.rest import Client
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse



account_sid = 'ACe0cad0adc0ff1f750b61e94c566d1fa2'
auth_token = '5bc8a5f9347360d81055a843ca03a247'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        # url='https://github.com/Derricks-Open-Source-Quest/sdghack/blob/master/middleware/voice.xml',
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+16462676977',
                        from_='+19292051436'
                    )

print(call.sid)

