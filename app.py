import app

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, override=True)
app.create_app().run(host="0.0.0.0", port=8080)
