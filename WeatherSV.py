#This code gathers weather data for Brisbane from WeatherSV
#...and displays it on the RaspberryPi SenseHat

import requests
from requests.exceptions import HTTPError
from sense_hat import SenseHat
import time

sense = SenseHat()

try:
 while True:

    response = requests.get('https://weathersv.app/api/channel/1KYmJu71uCEyETGE2CCJrL8uAGz6w3kVy8')
    response.raise_for_status()
    jsonResponse = response.json()

    tempString = str(jsonResponse["current"]["temperature"])
    humidityString = str(jsonResponse["current"]["humidity"])

    sense.show_message("Brisbane temp is: " + tempString + "C  ", text_colour=[0, 0, 255], scroll_speed=0.05)
    sense.show_message("Current humidity is: " + humidityString + "%  ", text_colour=[0, 255, 0], scroll_speed=0.05)
    sense.show_message(".....Via WeatherSV API.... ", text_colour=[255, 0, 0], scroll_speed=0.05)

    time.sleep(5)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
except KeyboardInterrupt:
    sense.clear()
    print("interrupted!")
