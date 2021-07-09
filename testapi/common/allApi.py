import requests


class Api:

    def get(self, url, params):
        response = requests.get(url=url, params=params)
        return response.text

    def post_data(self, url, data):
        response = requests.get(url=url, data=data)
        return response.text

    def post_json(self, url, json):
        response = requests.get(url=url, json=json)
        return response.text

if __name__ == '__main__':
    a=Api()
    print(a.get('https://reqres.in/api/users?','page=2'))