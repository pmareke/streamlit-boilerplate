from expects import equal, expect

from src.infrastructure.countries.dummy_countries_client import DummyCountriesClient
from src.use_cases.get_all_countries_query import (
    GetAllCountriesQuery,
    GetAllCountriesQueryHandler,
)


class TestGetAllCountriesQueryHandler:
    def test_get_all(self) -> None:
        query = GetAllCountriesQuery()
        client = DummyCountriesClient()
        handler = GetAllCountriesQueryHandler(client)

        response = handler.execute(query)
        countries = response.message()

        expect(countries[0].name).to(equal("Argentina"))
        expect(countries[0].capital).to(equal("Buenos Aires"))
