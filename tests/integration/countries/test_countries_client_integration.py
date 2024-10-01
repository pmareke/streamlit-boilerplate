from src.infrastructure.countries.http_countries_client import HttpCountriesClient


class TestCountriesClientIntegration:
    def test_get_all_countries(self) -> None:
        countries_client = HttpCountriesClient()

        countries = countries_client.all()

        assert len(countries) > 0
