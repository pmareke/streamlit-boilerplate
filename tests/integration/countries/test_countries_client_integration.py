from src.infrastructure.countries.http_countries_client import HttpCountriesClient


class TestCountriesClientIntegration:
    def test_get_all_countries(self) -> None:
        countries_client = HttpCountriesClient()

        countries = countries_client.all(limit=1)

        assert countries[0].name != ""
