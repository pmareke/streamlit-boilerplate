from src.delivery.streamlit.app import App
from src.infrastructure.countries.json_countries_client import JSONCountriesClient
from src.use_cases.get_all_countries_query import GetAllCountriesQueryHandler

countries_client = JSONCountriesClient()
get_all_countries_handler = GetAllCountriesQueryHandler(countries_client)
app = App()

app.render(get_all_countries_handler)
