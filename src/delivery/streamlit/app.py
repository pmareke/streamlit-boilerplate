from src.delivery.streamlit.components.countries_list import CountriesList
from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.text import Text
from src.domain.component import Component
from src.domain.query import QueryHandler


class App(Component):
    def __init__(self) -> None:
        self.header = Header()
        self.countries_list = CountriesList()
        self.text = Text()

    def render(self, handler: QueryHandler) -> None:
        self.header.render("Countries")
        self.countries_list.render(handler)
        self.text.render("Made by @pmareke")
