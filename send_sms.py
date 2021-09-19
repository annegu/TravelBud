from twilio.rest import Client
import random

verificationCode = random.randint(10000, 99999)

def send_message( phoneNumber ):
    # Your Account SID from twilio.com/console
    account_sid = "ACa00d8bfebadfbd113e237bceb367af4c"
    # Your Auth Token from twilio.com/console
    auth_token  = "8bbf8971f4d70839cc92e40bb258d74e"

    client = Client(account_sid, auth_token)

    #6479377285
    
    message = client.messages.create(
        to=phoneNumber, 
        from_="+16479579581",
        body="Your verification code is " + str(verificationCode))

    print(message.sid)
    return


