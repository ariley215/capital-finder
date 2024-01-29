from http import BaseHTTPRequesthandler
from urllib import parse
import requests


class Handler(BaseHTTPRequesthandler):
    def do_GET(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse.qsl(url_components.query)
        dictionary = dict(query_string_list)

        if "country" in dictionary:
            url = "https://restcountries.com/v3.1/name/"
            request = request.get(url + dictionary["country"])
            data = request.json
            capital_cities = []

            for country_data in data:
              capital_city = country_data["capitals"][0] #check data to make sure path is correct
              capital_cities.append(capital_city)
              message = str(capital_cities)
            else: 
              message = "What country would you like to know that capital of?"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = ""
        self.wfile.write(message.encode())
