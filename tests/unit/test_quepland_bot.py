from unittest import TestCase

from mockito import unstub, when, verify

from quepland_bot.quepland_bot import QueplandBot
from quepland_bot.domain.entities import CoordinatesSequence
from quepland_bot.domain.use_cases import ClickOnCoordinatesSequenceUseCase
from quepland_bot.domain.value_objects import Coordinates


class TestQueplandBot(TestCase):
    seconds_between_clicks: float

    def setUp(self) -> None:
        self.seconds_between_clicks = 0

    def tearDown(self) -> None:
        unstub()

    def test_run_WHEN_populated_coordinates_sequence_given_THEN_execute_click_on_coordinates_sequence_service_with_given_coordinates_sequence(self) -> None:
        default_loop_forever = True
        coordinates_sequence = CoordinatesSequence()
        coordinates_sequence.add_coordinates(Coordinates(x=1, y=1))
        when(ClickOnCoordinatesSequenceUseCase).execute(...)
        quepland_bot = QueplandBot()

        quepland_bot.run(coordinates_sequence)

        verify(ClickOnCoordinatesSequenceUseCase).execute(
            coordinates_sequence=coordinates_sequence,
            loop_forever=default_loop_forever
        )
