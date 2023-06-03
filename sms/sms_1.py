from twilio.rest import Client

account_sid = '여러분이 발급받은 SID'
auth_token = '여러분이 발급받은 Auth Token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="twilio 문자 메시지 전송 테스트입니다",
                     from_='+여러분이 발급받은 twilio 전화번호',
                     to='+82여러분의 휴대폰 번호'
                 )

print(message.sid)