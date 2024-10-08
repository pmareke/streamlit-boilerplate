from expects import be_none, expect

from src.infrastructure.countries.json_countries_client import JSONCountriesClient


class TestJSONCountriesClientIntegration:
    def test_get_all_countries(self) -> None:
        countries_client = JSONCountriesClient()

        countries = countries_client.all(limit=1)

        expect(countries[0].name).not_to(be_none)
