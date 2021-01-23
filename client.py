import os
from decouple import config
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# server = smtplib.SMTP_SSL('smtp.gmail.com', 25)
# server.connect("smtp.example.com", 465)
# server.ehlo()
# server.starttls()
# server.ehlo()

# with open('password.txt', 'r') as f:
#     password = f.read()

# server.login('sohanshetty2001@gmail.com', password)

######################################################################

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

######################################################################

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

server.login("sohanshetty2001@gmail.com", config('PASSWORD'))

######################################################################

msg = MIMEMultipart()
msg["From"] = 'sohanshetty2001@gmail.com'
msg['To'] = '2019sohan.shetty@ves.ac.in'
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
server.sendmail("sohanshetty2001@gmail.com",
                "2019sohan.shetty@ves.ac.in", text)

server.quit()
