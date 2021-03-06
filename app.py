from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route("/")
def index():
    send()
    return "Sending email from: " + os.environ['EMAIL_USER'] + " to " + os.environ['EMAIL_RECIPIENT']


def send():
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=os.environ['EMAIL_USER'],
                      recipients=[os.environ['EMAIL_RECIPIENT']], # use your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)
