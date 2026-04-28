from flask import Flask, request, redirect
import logging
from app.email_resources import ProposalSender


def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/")
    def home():
        app.logger.info("hello from world")
        return "Salve world!"

    @app.route("/send_test_mail", methods=["GET", "POST"])
    def send_test_mail():
        response = ProposalSender.send_proposal("Proposta de ", "Uma nova proposta")
        return response

    @app.route("/send_proposal_mail", methods=["POST"])
    def send_proposal_mail():
        app.logger.info("Sending Mail")
        app.logger.info(request.form)
        formated_subject = f"Nova proposta de {request.form['name']}"
        formated_body = f"PROPOSTA: {request.form['proposal']}"
        ProposalSender.send_proposal(subject=formated_subject, body=formated_body)
        return redirect("https://www.jasonuniverse.com.br")

    return app
