import json
import os
import random

import requests

from src.domain.countries_client import CountriesClient
from src.domain.country import Country


class JSONCountriesClient(CountriesClient):
    def __init__(self) -> None:
        self._req = requests
        self.countries = self._read_countries()

    def all(self, limit: int = 10) -> list[Country]:
        random.shuffle(self.countries)
        return self.countries[:limit]

    def _read_countries(self) -> list[Country]:
        working_directory = os.getcwd()
        path = os.path.join(working_directory, "resources", "countries.json")
        with open(path) as file:
            data = file.read()
            countries = []
            for item in json.loads(data):
                country = self._create_country(item)
                countries.append(country)
        return countries

    def _create_country(self, item: dict) -> Country:
        name = item["name"]["common"]
        flag = item["flags"]["png"]
        capitals = item["capital"]
        capital = capitals[0]
        return Country(name, capital, flag)
