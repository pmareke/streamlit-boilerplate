from abc import ABC, abstractmethod
from typing import Any


class Component(ABC):
    @abstractmethod
    def render(self, *args: Any, **kargs: Any) -> Any:
        raise NotImplementedError
