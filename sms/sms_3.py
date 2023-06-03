from twilio.rest import Client
import pandas as pd

account_sid = '여러분이 발급받은 SID'
auth_token = '여러분이 발급받은 Auth Token'
client = Client(account_sid, auth_token)

df = pd.read_excel('./회원정보.xlsx')
print(df, "\n")

for idx, row in df.iterrows():
    try:
        phone_num = row['전화번호'].replace("-", "")

        message = client.messages \
                            .create(
                                body=f'''안녕하십니까. {row['이름']} 회원님. 두사랑산악회 회장 심교훈입니다.

2022년 9월 24일 토요일 오전 8시에 북한산 등반이 예정되어 있사오니, 모두들 참석해주시기 바랍니다.''',
                                from_='+여러분이 발급받은 twilio 전화번호',
                                to='+82' + phone_num
                            )

        print(message.status)
    except Exception as e:
        print(e)