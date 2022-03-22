from src.application.exceptions import CoordinatesSequenceNotFoundException
from src.domain.entities import CoordinatesSequence
from src.domain.ports import MousePort, ClickRecorderPort
from src.domain.use_cases import ClickOnCoordinatesSequenceUseCase, RecordClicksUseCase
from src.infrastructure import PyautoguiMouseAdapter
from src.infrastructure.adapters import PynputClickRecorderAdapter


class QueplandBot:
    __mouse_class: type(MousePort)
    __click_recorder_class: type(ClickRecorderPort)
    __recorded_coordinates_sequence: CoordinatesSequence
    __seconds_between_clicks: float

    def __init__(self) -> None:
        self.__seconds_between_clicks = 0.2
        self.__mouse_class = PyautoguiMouseAdapter
        self.__click_recorder_class = PynputClickRecorderAdapter
        self.__recorded_coordinates_sequence = CoordinatesSequence()

    def record_clicks(self) -> CoordinatesSequence:
        click_recorder = self.__click_recorder_class()
        record_clicks_service = RecordClicksUseCase(click_recorder)
        self.__recorded_coordinates_sequence = record_clicks_service.execute()
        return self.__recorded_coordinates_sequence

    def run(self, recorded_clicks: CoordinatesSequence = None):
        coordinates_sequence = self.__get_valid_coordinates_sequence(recorded_clicks)
        mouse = PyautoguiMouseAdapter()
        click_on_coordinates_sequence_service = ClickOnCoordinatesSequenceUseCase(
            mouse=mouse,
            seconds_between_clicks=self.__seconds_between_clicks
        )
        click_on_coordinates_sequence_service.execute(coordinates_sequence=coordinates_sequence, loop_forever=False)

    def __get_valid_coordinates_sequence(self, coordinates_sequence: CoordinatesSequence or None) -> CoordinatesSequence:
        if coordinates_sequence:
            return coordinates_sequence
        elif not self.__recorded_coordinates_sequence.is_empty:
            return self.__recorded_coordinates_sequence
        else:
            raise CoordinatesSequenceNotFoundException('No clicks recorded')
