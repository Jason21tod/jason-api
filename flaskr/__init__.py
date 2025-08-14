from flask import Flask


def create_app():
    # Application factory that create the app for us
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev', #this should be changed later for some random value that's secret, like a env
    )

    @app.route('/')
    def hello_world():
        return "hello world"

    return app