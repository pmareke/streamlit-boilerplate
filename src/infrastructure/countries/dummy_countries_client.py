from src.domain.countries_client import CountriesClient
from src.domain.country import Country


class DummyCountriesClient(CountriesClient):
    def all(self, limit: int = 10) -> list[Country]:
        return [
            Country(
                name="Argentina",
                capital="Buenos Aires",
                flag="https://restcountries.com/data/arg.svg",
            ),
        ]
