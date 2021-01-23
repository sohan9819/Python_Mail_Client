import os
from decouple import config
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

######################################################################

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

server.login("sender@gmail.com", config('PASSWORD'))

######################################################################

msg = MIMEMultipart()
msg["From"] = 'sender@gmail.com'
msg['To'] = 'reciever@gmail.com'
msg['Subject'] = 'Just A test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'MU_SEM3_4_Admission.pdf'
attachment = open(filename, 'rb')

p = MIMEBase('appplication', 'octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail("sender@gmail.com",
                "reciever@gmail.com", text)

server.quit()
