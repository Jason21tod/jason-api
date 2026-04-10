import flask 
import logging
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def create_app():
    app = flask.Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/")
    def home():
        app.logger.info("hello from world")
        return "Salve world!"

    @app.route("/send_test_mail")
    def send_mail():
        server = "smtp.gmail.com"
        port = 587
        sender_email = str(os.environ.get("EMAIL_SENDER"))
        password = str(os.environ.get("EMAIL_APP_PASSWORD"))
        server = smtplib.SMTP(server, port)
        
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)

        msg = MIMEMultipart()
        body= "test"
        msg['Subject'] = "Hello From Test Subject"
        msg['From'] = sender_email
        msg['To'] = "gian.21.pereira@gmail.com"
        msg.attach(MIMEText(body))

        response = str(server.sendmail(sender_email, "gian.21.pereira@gmail.com", msg.as_string()))
        server.quit()
        return response


    return app
