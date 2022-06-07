from flask import Flask, url_for
from flask import render_template
import requests

app = Flask(__name__)

def get_weather_data():
  r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
  return r.json()

@app.route('/')
def index():
  data = get_weather_data()
  return data