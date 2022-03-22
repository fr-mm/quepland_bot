from src.application.exceptions import CoordinatesSequenceNotFoundException
from src.domain.entities import CoordinatesSequence
from src.domain.ports import MousePort, ClickRecorderPort, MouseLoopBreakerPort
from src.domain.use_cases import ClickOnCoordinatesSequenceUseCase, RecordClicksUseCase
from src.infrastructure import PyautoguiMouseAdapter, PynputMouseLoopBreakerAdapter
from src.infrastructure.adapters import PynputClickRecorderAdapter


class QueplandBot:
    __default_seconds_between_clicks: float
    __mouse_class: type(MousePort)
    __click_recorder_class: type(ClickRecorderPort)
    __mouse_loop_breaker_class: type(MouseLoopBreakerPort)
    __recorded_coordinates_sequence: CoordinatesSequence

    def __init__(
            self,
            default_seconds_between_clicks=0.1
    ) -> None:
        self.__default_seconds_between_clicks = default_seconds_between_clicks
        self.__mouse_class = PyautoguiMouseAdapter
        self.__click_recorder_class = PynputClickRecorderAdapter
        self.__mouse_loop_breaker_class = PynputMouseLoopBreakerAdapter
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
            seconds_between_clicks=self.__default_seconds_between_clicks
        )
        break_loop_callback = click_on_coordinates_sequence_service.loop_break_callback
        mouse_loop_breaker = self.__mouse_loop_breaker_class(break_loop_callback=break_loop_callback)
        mouse_loop_breaker.break_when_any_key_is_pressed()
        click_on_coordinates_sequence_service.execute(coordinates_sequence=coordinates_sequence, loop_forever=True)

    def __get_valid_coordinates_sequence(self, coordinates_sequence: CoordinatesSequence or None) -> CoordinatesSequence:
        if coordinates_sequence:
            return coordinates_sequence
        elif not self.__recorded_coordinates_sequence.is_empty:
            return self.__recorded_coordinates_sequence
        else:
            raise CoordinatesSequenceNotFoundException('No clicks recorded')
