import os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = "yrishu71@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = MIMEMultipart()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'sidhantyadav92@gmail.com'

msg.attach(MIMEText('This is a plain text email', 'plain'))

msg.attach(MIMEText("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", 'html'))

# Attach PDF file
pdf_filename = './file.pdf'
with open(pdf_filename, 'rb') as pdf_file:
    pdf_attach = MIMEApplication(pdf_file.read(), _subtype="pdf")
    pdf_attach.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_filename)}')
    msg.attach(pdf_attach)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
