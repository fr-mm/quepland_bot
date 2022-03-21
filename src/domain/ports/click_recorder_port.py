from abc import ABC, abstractmethod

from src.domain.entities import CoordinatesSequence


class ClickRecorderPort(ABC):
    @abstractmethod
    def record_until_any_key_is_pressed(self) -> CoordinatesSequence:
        pass
