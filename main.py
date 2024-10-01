from src.delivery.streamlit.app import App
from src.infrastructure.countries.http_countries_client import HttpCountriesClient

client = HttpCountriesClient()
app = App(client)

app.render()
