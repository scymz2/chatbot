# -*- coding: utf-8 -*-
import re
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement


class WeatherLogicAdapter(LogicAdapter):
    """
    A logic adapter that returns information regarding the weather and
    the forecast for a specific location. Currently, only basic information
    is returned, but additional features are planned in the future.
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['weather', 'temperature', 'humidity', 'light', 'wind', 'rain']
        question = re.sub(r'[^\w\s]', '', statement.text)
        if any(x in question.split() for x in words):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        """
        Returns the forecast for a location (using latitude and longitude).
        """
        import requests

        url = "http://api.openweathermap.org/data/2.5/weather?q=Ningbo,china&APPID=885aa9eb815b6b6b1b24ce7ade4b78d9"

        res = requests.get(url)
        data = res.json()

        if res.status_code == 404:
            response = Statement(text='Network Error!')
            response.confidence = 0
            return response
        else:
            condition = data["main"]
            temp = condition["temp"]
            humidity = condition["humidity"]
            pressure = condition["pressure"]

            info = data["weather"]
            des = info[0]
            descrip = des["description"]

            response = Statement(text="The current weather in Ningbo: " + str(descrip) + ", Temperature: " + str(int(
                temp - 272.15)) + "℃, Humidity: " + str(humidity) + "%, Pressure: " + str(pressure/1000) + "kpa")
            response.confidence = 2
            return response

