# This python file is where we will create the Flask Application and make calls to the weather API.
from flask import Flask, render_template


app = Flask(__name__)

# map this application to a route
@app.route('/')
def index():
    return render_template('index.html')