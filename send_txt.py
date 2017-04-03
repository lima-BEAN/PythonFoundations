# inside twilio is a folder called rest and inside that folder there's a class called TwilioRestClient
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC4d3f95c750171540fd08d585636cc043"
auth_token = "ecdc2590f798adf83aab9ef54fc339d9"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+18329045678",
    from_="+16606754209",
    body="Here's limaBEAN")
