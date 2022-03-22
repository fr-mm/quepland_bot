from typing import List

from quepland_bot.domain.exceptions import CoordinatesCollectionEmptyException
from quepland_bot.domain.value_objects import Coordinates


class CoordinatesSequence:
    __coordinates: List[Coordinates]
    __counter: int

    def __init__(self) -> None:
        self.__coordinates = []
        self.reset_to_first_coordinates()

    @property
    def is_empty(self) -> bool:
        return len(self.__coordinates) == 0

    @property
    def length(self) -> int:
        return len(self.__coordinates)

    def add_coordinates(self, coordinates: Coordinates) -> None:
        self.__coordinates.append(coordinates)

    @property
    def next_coordinates(self) -> Coordinates:
        try:
            coordinates = self.__coordinates[self.__counter]
            self.__increment_counter()
            return coordinates

        except IndexError:
            raise CoordinatesCollectionEmptyException()

    def reset_to_first_coordinates(self) -> None:
        self.__counter = 0

    def __increment_counter(self) -> None:
        if self.__counter < len(self.__coordinates) - 1:
            self.__counter += 1
        else:
            self.reset_to_first_coordinates()
