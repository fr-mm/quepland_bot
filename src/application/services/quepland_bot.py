from src.domain.entities import CoordinatesSequence
from src.domain.use_cases import ClickOnCoordinatesSequenceUseCase
from src.domain.value_objects import Coordinates
from src.infrastructure import PyautoguiMouse


class QueplandBot:
    __click_on_coordinates_sequence_use_case: ClickOnCoordinatesSequenceUseCase

    def __init__(self) -> None:
        mouse = PyautoguiMouse()
        self.__click_on_coordinates_sequence_use_case = ClickOnCoordinatesSequenceUseCase(
            mouse=mouse,
            seconds_between_clicks=0.2
        )

    def run(self):
        coordinates_sequence = CoordinatesSequence()
        coordinates_sequence.add_coordinates(Coordinates(800, 400))
        coordinates_sequence.add_coordinates(Coordinates(1000, 400))
        coordinates_sequence.add_coordinates(Coordinates(900, 500))

        self.__click_on_coordinates_sequence_use_case.execute(coordinates_sequence)
