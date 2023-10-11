from flask import Flask, render_template, redirect, url_for
import os
import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'sidhantyadav92@gmail.com'

msg.set_content('This is a plain text with falsk')

    
@app.route("/")
def home():
    return render_template('home.html')
    
@app.route("/send", methods=["POST", "GET"])
def send():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    return redirect(url_for("home"))
    
    
if __name__ == '__main__' :
   app.run(debug=False, port=0.0.0.0)
