import smtplib
from email.mime.text import MIMEText

smpt_server = "smtp.naver.com"
smtp_port = 587

s = smtplib.SMTP(smpt_server, smtp_port)
s.starttls()

email = '여러분의 네이버 메일주소@naver.com'
email_pw = '이메일 비밀번호'

s.login(email, email_pw)

recv_email = "받는 사람 이메일 주소" # ex) kyohoonsim@gmail.com
subject = "고객 사은 이벤트에 당첨되셨습니다!"
text = '''
축하드립니다! 
고객님은 당사의 고객 사은 이벤트에 당첨되셨습니다.
'''

msg = MIMEText(text)
msg['From'] = email
msg['To'] = recv_email
msg['Subject'] = subject

s.sendmail(email, recv_email, msg.as_string())
s.quit()