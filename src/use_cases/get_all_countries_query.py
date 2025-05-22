from src.domain.countries_client import CountriesClient
from src.domain.country import Country
from src.domain.query import Query, QueryHandler, QueryResponse


class GetAllCountriesQuery(Query):
    def __init__(self, limit: int) -> None:
        self.limit = limit
        super().__init__()


class GetAllCountriesQueryResponse(QueryResponse):
    def __init__(self, countries: list[Country]) -> None:
        self.countries = countries

    def message(self) -> list[Country]:
        return self.countries


class GetAllCountriesQueryHandler(QueryHandler):
    def __init__(self, countries_client: CountriesClient) -> None:
        self._countries_client = countries_client

    def execute(self, query: GetAllCountriesQuery) -> GetAllCountriesQueryResponse:
        countries = self._countries_client.all(limit=query.limit)
        return GetAllCountriesQueryResponse(countries)
