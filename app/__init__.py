import flask 
import logging


def create_app():
    app = flask.Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/")
    def home():
        app.logger.info("hello from world")
        return "Salve world!"

    return app
