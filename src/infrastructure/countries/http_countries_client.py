import requests

from src.domain.countries_client import CountriesClient
from src.domain.country import Country


class HttpCountriesClient(CountriesClient):
    def __init__(self) -> None:
        self._req = requests

    def all(self) -> list[Country]:
        url = "https://restcountries.com/v2/all?fields=name,capital,flag"
        response = self._req.get(url)
        content = response.json()
        countries = []
        for item in content:
            name = item["name"]
            flag = item["flag"]
            capital = item.get("capital", "N/A")
            country = Country(name, capital, flag)
            countries.append(country)
        return countries
