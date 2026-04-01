import flask 


app = flask.Flask(__name__)


def create_app():
    
    
    @app.route("/")
    def home():
        return "Salve world!"

    return app


if __name__ == "__main__":
    app.run(debug=True)