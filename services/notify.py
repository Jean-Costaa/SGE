import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    
    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/3bfd437c-658c-40c9-b415-4cb4b23ddbc5',
            data=data,
        )
