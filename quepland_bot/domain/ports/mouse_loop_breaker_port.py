from abc import ABC, abstractmethod


class MouseLoopBreakerPort(ABC):
    @abstractmethod
    def break_when_any_key_is_pressed(self) -> None:
        pass
