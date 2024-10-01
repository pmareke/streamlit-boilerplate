from src.delivery.streamlit.components.button import Button
from src.delivery.streamlit.components.image import Image
from src.delivery.streamlit.components.text import Text
from src.domain.countries_client import CountriesClient
from src.infrastructure.countries.dummy_countries_client import DummyCountriesClient


class CountriesList:
    def __init__(self, countries_client: CountriesClient) -> None:
        self.countries_client = countries_client
        self.button = Button()

    def render(self) -> None:
        if self.button.render("Load Countries"):
            countries = self.countries_client.all(limit=3)
            for country in countries:
                text = Text()
                image = Image()

                text.render(f"Country: {country.name}, Capital: {country.capital}")
                image.render(url=country.flag, width=100)


if __name__ == "__main__":
    countries_client = DummyCountriesClient()
    countries_list = CountriesList(countries_client)
    countries_list.render()
