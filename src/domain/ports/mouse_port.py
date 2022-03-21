from abc import ABC, abstractmethod

from src.domain.value_objects import Coordinates


class MousePort(ABC):
    @abstractmethod
    def click_on(self, coordinates: Coordinates) -> None:
        pass
