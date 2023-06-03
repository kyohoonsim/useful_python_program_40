import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pandas as pd

smpt_server = "smtp.naver.com"
smtp_port = 587

email = '여러분의 네이버 메일주소@naver.com'
email_pw = '이메일 비밀번호'

s = smtplib.SMTP(smpt_server, smtp_port)
s.starttls()
s.login(email, email_pw)

df = pd.read_excel('./회원리스트.xlsx')
df_lucky = df[df['이벤트 당첨 여부']=='O']

for idx, row in df_lucky.iterrows():
    recv_name = row['이름']
    recv_email = row['이메일주소']

    subject = f"{recv_name}님, 고객 사은 이벤트에 당첨되셨습니다!"
    text = f'''
    <p>안녕하세요. {recv_name}님.</p>
    <p style="color: dodgerblue; font-size: 20px;">축하드립니다!</p> 
    <p>고객님은 당사의 <span style="background-color: hotpink; color: white;">고객 사은 이벤트</span>에 당첨되셨습니다.</p>
    <p><span style="font-style: italic;">첨부파일</span>을 꼭 확인해주세요.</p>
    '''

    msg = MIMEMultipart()
    msg_text = MIMEText(text, 'html')
    msg.attach(msg_text)

    with open('./당첨자분들께.docx', 'rb') as f:
        msg_file = MIMEApplication(f.read())
        msg_file.add_header('Content-Disposition', 'attachment', filename="당첨자분들께.docx")
        msg.attach(msg_file)

    msg['From'] = email
    msg['To'] = recv_email
    msg['Subject'] = subject

    s.sendmail(email, recv_email, msg.as_string())
    
s.quit()