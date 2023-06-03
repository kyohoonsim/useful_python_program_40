from twilio.rest import Client

account_sid = '여러분이 발급받은 SID'
auth_token = '여러분이 발급받은 Auth Token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="사랑하는 누구누구야, 너와 함께 해서 행복해. 그런데 내가 누구게?",
                     from_='+여러분이 발급받은 twilio 전화번호',
                     to='+82문자 받을 사람 휴대폰 번호'
                 )

print(message.sid)