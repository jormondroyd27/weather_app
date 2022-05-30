from flask import Flask, render_template, request, url_for, redirect
from api import get_weather
import requests, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/city', methods=['POST'])
def post_weather():
    city = request.form['city']
    data = get_weather(city)
    temp = data['main']['temp']
    min = data['main']['temp_min']
    max = data['main']['temp_max']
    description = data['weather'][0]['main']
    location = data['name']
    country = data['sys']['country']
    return render_template('results.html', city=data, temp=temp, description=description, location=location, country=country, min=min, max=max)

# ensures the app only runs once and multiple instances are not created
if __name__ == '__main__':
    app.run()