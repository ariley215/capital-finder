from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        if "country" in dictionary:
            url = "https://restcountries.com/v3.1/name/"
            response = requests.get(url + dictionary["country"])
            data = response.json()
            country = data[0]
            capital_city = country["capital"][0]
            message = f"The capital of {country['name']['common']} is {capital_city}"
        elif "capital" in dictionary:
            response = requests.get(
                f'https://restcountries.com/v3.1/capital/{dictionary["capital"]}?fields=name,capital'
            )
            capitals_response = response.json()
            capital = capitals_response[0]["capital"][0]
            capital_country = capitals_response[0]["name"]["common"]
            message = f"{capital} is the capital of {capital_country}"

        else:
            message = "What country would you like to know that capital of?"
            response = {"statusCode": 400, "body": "Invalid query parameters"}

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))
        return
