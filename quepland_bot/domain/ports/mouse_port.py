from abc import ABC, abstractmethod

from quepland_bot.domain.value_objects import Coordinates


class MousePort(ABC):
    @abstractmethod
    def click_on(self, coordinates: Coordinates) -> None:
        pass
