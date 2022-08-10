import requests


class MyRequests:
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookie: dict = None):
        return MyRequests._send(url, data, headers, cookie, "GET")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response
