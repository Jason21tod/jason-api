import flask 
import logging
from app.email_resources import ProposalSender


def create_app():
    app = flask.Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/")
    def home():
        app.logger.info("hello from world")
        return "Salve world!"

    @app.route("/send_test_mail", methods=["GET", "POST"])
    def send_mail():
        response = ProposalSender.send_proposal("Proposta de ", "Uma nova proposta")
        return response

    return app
