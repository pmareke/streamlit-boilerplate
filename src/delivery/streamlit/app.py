from src.delivery.streamlit.components.countries_list import CountriesList
from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.text import Text
from src.infrastructure.countries.http_countries_client import HttpCountriesClient

header = Header()
countries_client = HttpCountriesClient()
countries_list = CountriesList(countries_client)
text = Text()

header.render("Countries")
countries_list.render()
text.render("Made by @pmareke")
