from src.delivery.streamlit.app import App
from src.infrastructure.countries.http_countries_client import HttpCountriesClient
from src.use_cases.get_all_countries_query import GetAllCountriesQueryHandler

countries_client = HttpCountriesClient()
get_all_countries_handler = GetAllCountriesQueryHandler(countries_client)
app = App(get_all_countries_handler)

app.render()
