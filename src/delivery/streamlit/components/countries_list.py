from src.delivery.streamlit.components.button import Button
from src.delivery.streamlit.components.image import Image
from src.delivery.streamlit.components.text import Text
from src.domain.component import Component
from src.domain.query import QueryHandler
from src.infrastructure.countries.dummy_countries_client import DummyCountriesClient
from src.use_cases.get_all_countries_query import (
    GetAllCountriesQuery,
    GetAllCountriesQueryHandler,
)


class CountriesList(Component):
    def __init__(self) -> None:
        self.button = Button()

    def render(self, handler: QueryHandler) -> None:
        if self.button.render("Load Countries"):
            query = GetAllCountriesQuery(limit=3)
            response = handler.execute(query)
            for country in response.message():
                text = Text()
                image = Image()

                text.render(f"Country: {country.name}, Capital: {country.capital}")
                image.render(url=country.flag, width=100)


if __name__ == "__main__":
    countries_client = DummyCountriesClient()
    get_all_countries_handler = GetAllCountriesQueryHandler(countries_client)
    countries_list = CountriesList()
    countries_list.render(get_all_countries_handler)
