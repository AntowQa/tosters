import requests
from settings import MTT_URL, HEADERS


class MTTClient:

    def get_start_page(self):
        response = requests.get(
            url=MTT_URL,
            headers=HEADERS
        )
        response.raise_for_status()
        return response.text
