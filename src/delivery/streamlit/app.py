from src.delivery.streamlit.components.countries_list import CountriesList
from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.text import Text
from src.domain.query import QueryHandler


class App:
    def __init__(self, get_all_countries_handler: QueryHandler) -> None:
        self.get_all_countries_handler = get_all_countries_handler

    def render(self) -> None:
        header = Header()
        header.render("Countries")

        countries_list = CountriesList(self.get_all_countries_handler)
        countries_list.render()

        text = Text()
        text.render("Made by @pmareke")
