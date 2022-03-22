import time
from typing import Callable

from src.domain.entities import CoordinatesSequence
from src.domain.ports import MousePort


class ClickOnCoordinatesSequenceUseCase:
    __mouse: MousePort 
    __seconds_between_clicks: float
    __break_loop: bool

    def __init__(self, mouse: MousePort, seconds_between_clicks: float) -> None:
        self.__mouse = mouse
        self.__seconds_between_clicks = seconds_between_clicks

    def execute(self, coordinates_sequence: CoordinatesSequence, loop_forever: bool = False) -> None:
        self.__break_loop = False
        print(f'Reproducing saved clicks, press any key to stop ')
        if loop_forever:
            self.__loop_forever(coordinates_sequence)
        else:
            self.__process_sequence_once(coordinates_sequence)

    @property
    def loop_break_callback(self) -> Callable:
        return self.__break_loop_callback

    def __break_loop_callback(self) -> None:
        self.__break_loop = True

    def __click_on_next_coordinates(self, coordinates_sequence: CoordinatesSequence) -> None:
        self.__mouse.click_on(coordinates_sequence.next_coordinates)
        time.sleep(self.__seconds_between_clicks)

    def __loop_forever(self, coordinates_sequence: CoordinatesSequence) -> None:
        while not self.__break_loop:
            self.__click_on_next_coordinates(coordinates_sequence)

    def __process_sequence_once(self, coordinates_sequence: CoordinatesSequence) -> None:
        for _ in range(coordinates_sequence.length):
            if self.__break_loop:
                break
            self.__click_on_next_coordinates(coordinates_sequence)
