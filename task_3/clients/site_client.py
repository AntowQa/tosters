import requests
from settings import BASE_URL, HEADERS


class SiteClient:

    def get_start_page(self):
        response = requests.get(
            url=BASE_URL,
            headers=HEADERS
        )
        response.raise_for_status()
        return response.text
