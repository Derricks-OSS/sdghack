from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe0cad0adc0ff1f750b61e94c566d1fa2'
auth_token = '5bc8a5f9347360d81055a843ca03a247'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19292051436',
                     to='+16462676977'
                 )