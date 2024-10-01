from abc import ABC, abstractmethod

from src.domain.country import Country


class CountriesClient(ABC):
    @abstractmethod
    def all(self, limit: int = 10) -> list[Country]:
        raise NotImplementedError
