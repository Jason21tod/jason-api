import app

from dotenv import load_dotenv
load_dotenv()
app.create_app().run(host="0.0.0.0", port=8080)
