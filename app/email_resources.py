
import smtplib
import os

from dotenv import dotenv_values
from flask import current_app
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

values = dotenv_values(".env")


_SERVER_ADDRESS = "smtp.gmail.com"
_PORT = 587
_SENDER_EMAIL = str(values["EMAIL_SENDER"])
_RECEIVER_EMAIL = str(values["EMAIL_RECEIVER"])
_PASSWORD = str(values["EMAIL_APP_PASSWORD"])

if _SENDER_EMAIL == "None" or _RECEIVER_EMAIL == "None" or _PASSWORD == "None":
    raise Exception("Error on init: env vars not initialized")


class __MailSender():
    """Base class to send emails."""
    @classmethod
    def _setup_server(cls) -> smtplib.SMTP:
        """Setup the conection with the server.
        """
        server = smtplib.SMTP(_SERVER_ADDRESS, _PORT)
        server.ehlo()
        server.starttls()
        print(server.login(_SENDER_EMAIL, _PASSWORD))
        return server

    @classmethod
    def _setup_msg(cls, subject, body):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = _SENDER_EMAIL
        msg['To'] = _RECEIVER_EMAIL
        msg.attach(MIMEText(body))
        return msg
    
class ProposalSender(__MailSender):
    @classmethod
    def send_proposal(cls, subject: str, body: str):
        """Main function used to send proposals from customer to dev email directly.
        - subject: str -> Used to set the subject of the email.
        - body: str-> The body of the email
        """
        server: smtplib.SMTP = cls._setup_server()
        msg = cls._setup_msg(subject, body)
        response = str(server.sendmail(_SENDER_EMAIL, _RECEIVER_EMAIL, msg.as_string()))
        
        server.quit()
        current_app.logger.info("Proposal Sended...")
        return response