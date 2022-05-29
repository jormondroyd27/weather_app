# This python file is where we will create the Flask Application and make calls to the weather API.
import requests, os

# load_dotenv() will first look for a .env file and it will load the environment variables from the file and make them accessible
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('api_key')
def get_weather(place):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={place}&appid={API_KEY}'
    response = requests.get(api_url)
    return response.json()