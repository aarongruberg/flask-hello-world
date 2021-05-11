
# Example with index.html
from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/')
def index():
    time.sleep(40)
    return render_template('index.html')
