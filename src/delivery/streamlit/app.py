from src.delivery.streamlit.components.countries_list import CountriesList
from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.text import Text
from src.domain.query import QueryHandler


class App:
    def __init__(self, get_all_countries_handler: QueryHandler) -> None:
        self.get_all_countries_handler = get_all_countries_handler
        self.header = Header()
        self.countries_list = CountriesList(self.get_all_countries_handler)
        self.text = Text()

    def render(self) -> None:
        self.header.render("Countries")

        self.countries_list.render()

        self.text.render("Made by @pmareke")
