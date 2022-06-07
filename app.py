from flask import Flask, request, jsonify
from flask import render_template
import requests
from weather_au import api


app = Flask(__name__)

def getForecastsIn(searchText):
  result = api.WeatherApi(search=searchText, debug=0)
  obsrvtns = result.forecasts_daily()

  return obsrvtns

@app.route('/getData', methods=['GET', 'POST'])
def get_weather_data():
  if request.method == "POST":
    print("---- REQUESTING WEATHER DATA ----")
    searchParam = request.get_data().decode('utf8')
    print(f"keyword: {searchParam}")
    result = getForecastsIn(searchParam)
    print(result)

    return jsonify(result)
    # observations = weather.getDataFromAPI()
  return None

@app.route('/')
def index():
  # data = get_weather_data()
  r = render_template("index.html")
  return r