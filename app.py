
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


app.config.update(
    DEBUG=True,
    SECRET_KEY='...'
)

# export FLASK_APP=app.py
# flask run
