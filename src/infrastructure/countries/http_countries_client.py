import random

import requests

from src.domain.countries_client import CountriesClient
from src.domain.country import Country


class HttpCountriesClient(CountriesClient):
    URL = "https://restcountries.com/v2/all?fields=name,capital,flag"

    def __init__(self) -> None:
        self._req = requests

    def all(self, limit: int = 10) -> list[Country]:
        response = self._req.get(self.URL)
        content = response.json()
        random.shuffle(content)
        countries = []
        for item in content[0:limit]:
            countries.append(self._create_country(item))
        return countries

    def _create_country(self, item: dict) -> Country:
        name = item["name"]
        flag = item["flag"]
        capital = item.get("capital", "N/A")
        return Country(name, capital, flag)
