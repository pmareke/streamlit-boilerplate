from src.delivery.streamlit.components.countries_list import CountriesList
from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.text import Text
from src.domain.countries_client import CountriesClient
from src.infrastructure.countries.dummy_countries_client import DummyCountriesClient


class App:
    def __init__(self, countries_client: CountriesClient = DummyCountriesClient()):
        self.countries_client = countries_client

    def render(self) -> None:
        header = Header()
        header.render("Countries")

        countries_list = CountriesList(self.countries_client)
        countries_list.render()

        text = Text()
        text.render("Made by @pmareke")
