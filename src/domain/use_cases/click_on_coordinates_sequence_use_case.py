import time

from src.domain.entities import CoordinatesSequence
from src.domain.ports import MousePort


class ClickOnCoordinatesSequenceUseCase:
    __mouse: MousePort
    __seconds_between_clicks: float

    def __init__(self, mouse: MousePort, seconds_between_clicks: float) -> None:
        self.__mouse = mouse
        self.__seconds_between_clicks = seconds_between_clicks

    def execute(self, coordinates_sequence: CoordinatesSequence, loop_forever: bool = False) -> None:
        print(f'Reproducing saved clicks ')
        if loop_forever:
            self.__loop_forever(coordinates_sequence)
        else:
            self.__process_sequence_once(coordinates_sequence)

    def __click_on_next_coordinates(self, coordinates_sequence: CoordinatesSequence) -> None:
        self.__mouse.click_on(coordinates_sequence.next_coordinates)
        time.sleep(self.__seconds_between_clicks)

    def __loop_forever(self, coordinates_sequence: CoordinatesSequence) -> None:
        while True:
            self.__click_on_next_coordinates(coordinates_sequence)

    def __process_sequence_once(self, coordinates_sequence: CoordinatesSequence) -> None:
        for _ in range(coordinates_sequence.length):
            self.__click_on_next_coordinates(coordinates_sequence)
