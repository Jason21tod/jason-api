import flask 
import logging


def create_app():
    app = flask.Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/")
    def home():
        app.logger.info("hello from world")
        return "Salve world!"

    @app.route("/send_test_mail")
    def send_mail():

        return response


    return app
