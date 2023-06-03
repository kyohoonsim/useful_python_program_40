import string
import random
import smtplib
from email.mime.text import MIMEText


def make_temp_password():
    new_pw = ""

    for i in range(5):
        new_pw += random.choice(string.ascii_letters)

    for i in range(3):
        new_pw += random.choice(string.digits)

    for i in range(2):
        new_pw += random.choice("!@#$%^&*")
    
    new_pw_shuffle = "".join(random.sample(new_pw, len(new_pw)))
    return new_pw_shuffle


class EmailSender:
    __smpt_server = "smtp.naver.com"
    __smtp_port = 587

    def __init__(self, email, email_pw):
        self.email = email
        self.email_pw = email_pw

    def send_email(self, recv_email):
        s = smtplib.SMTP(EmailSender.__smpt_server, EmailSender.__smtp_port)
        s.starttls()

        s.login(self.email, self.email_pw)

        subject = "임시 비밀번호 발송"
        text = f"임시 비밀번호: {make_temp_password()}"

        msg = MIMEText(text)
        msg['From'] = self.email
        msg['To'] = recv_email
        msg['Subject'] = subject

        s.sendmail(self.email, recv_email, msg.as_string())
        s.quit()


email_sender = EmailSender('여러분의 네이버 메일주소@naver.com', '이메일 비밀번호')
email_sender.send_email('받는 사람 이메일 주소')