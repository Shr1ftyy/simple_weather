from weather_au import api

def setup(search=None):
  w = api.WeatherApi(search='parkville+vic', debug=0)
  return w