from typing import List

from src.value_objects import Coordinates


class CoordinatesCollection:
    __coordinates: List[Coordinates]
    __counter: int

    def __init__(self) -> None:
        self.__coordinates = []
        self.reset_to_first_coordinates()

    def add_coordinates(self, coordinates: Coordinates) -> None:
        self.__coordinates.append(coordinates)

    @property
    def next_coordinates(self) -> Coordinates:
        coordinates = self.__coordinates[self.__counter]
        self.__counter += 1
        return coordinates

    def reset_to_first_coordinates(self) -> None:
        self.__counter = 0
