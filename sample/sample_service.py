import requests


class SampleService:

    def __init__(self, host):
        self.host = host

    def get_todo(self, id):
        url = "{}/todos/{}".format(self.host, id)
        resp = requests.get(url)

        if resp.status_code != 200:
            raise ValueError(
                "SampleService::get_todo returned status {}".format(
                    resp.status_code))

        return resp.json()
