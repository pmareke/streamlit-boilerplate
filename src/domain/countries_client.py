from abc import ABC, abstractmethod

from src.domain.country import Country


class CountriesClient(ABC):
    @abstractmethod
    def all(self) -> list[Country]:
        raise NotImplementedError
