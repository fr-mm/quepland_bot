from unittest import TestCase

from mockito import mock, verify, unstub

from quepland_bot.domain.use_cases import ClickOnCoordinatesSequenceUseCase
from quepland_bot.domain.value_objects import Coordinates


class TestClickOnCoordinatesSequenceUseCase(TestCase):
    def tearDown(self) -> None:
        unstub()

    def test_execute_WHEN_called_THEN_calls_mouse_click_on_with_given_coordinates_collection(self) -> None:
        seconds_between_clicks = 0
        coordinates = mock(Coordinates)
        coordinates_sequence = mock({'next_coordinates': coordinates, 'length': 1})
        mouse = mock({'click_on': lambda x: None})
        click_on_coordinates_sequence_service = ClickOnCoordinatesSequenceUseCase(mouse, seconds_between_clicks)

        click_on_coordinates_sequence_service.execute(coordinates_sequence, loop_forever=False)

        verify(mouse).click_on(coordinates)

