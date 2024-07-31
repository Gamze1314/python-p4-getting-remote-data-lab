import requests
import json
import ipdb

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #sends a get request to url, returns the body of the response.
        # https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        #uses get_response_body to send a request, return Python list or dictionary of data converted from the response.
        # https: // learn-co-curriculum.github.io/json-site-example/endpoints/people.json
        response_body = self.get_response_body()
        return json.loads(response_body)


x = GetRequester(
    "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
print(x)
# ipdb.set_trace()
