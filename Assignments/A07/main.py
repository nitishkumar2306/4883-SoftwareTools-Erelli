import gui
import get_weather

url = gui.buildWeatherURL()
get_weather.mainfunction(url)