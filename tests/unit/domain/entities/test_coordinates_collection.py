from unittest import TestCase

from quepland_bot.domain.entities import CoordinatesSequence
from quepland_bot.domain.exceptions import CoordinatesCollectionEmptyException
from quepland_bot.domain.value_objects import Coordinates


class TestCoordinatesCollection(TestCase):
    def test_next_coordinates_WHEN_coordinates_exists_THEN_returns_coordinates(self) -> None:
        coordinates = Coordinates(x=1, y=1)
        coordinates_collection = CoordinatesSequence()
        coordinates_collection.add_coordinates(coordinates)

        returned_coordinates = coordinates_collection.next_coordinates

        self.assertEqual(coordinates, returned_coordinates)

    def test_next_coordinates_WHEN_two_coordinates_exists_and_is_called_twice_THEN_returns_coordinates_in_order_they_were_saved(self) -> None:
        coordinates1 = Coordinates(x=1, y=1)
        coordinates2 = Coordinates(x=2, y=2)
        coordinates_collection = CoordinatesSequence()
        coordinates_collection.add_coordinates(coordinates1)
        coordinates_collection.add_coordinates(coordinates2)

        returned_coordinates = (coordinates_collection.next_coordinates, coordinates_collection.next_coordinates)

        expected_coordinates = (coordinates1, coordinates2)
        self.assertEqual(expected_coordinates, returned_coordinates)

    def test_next_coordinates_WHEN_no_coordinates_exists_THEN_raises_coordinates_collection_empty_exception(self) -> None:
        coordinates_collection = CoordinatesSequence()

        with self.assertRaises(CoordinatesCollectionEmptyException):
            coordinates = coordinates_collection.next_coordinates

    def test_next_coordinates_WHEN_last_coordinates_were_the_last_THEN_returns_first_coordinates(self) -> None:
        coordinates1 = Coordinates(x=1, y=1)
        coordinates2 = Coordinates(x=2, y=2)
        coordinates_collection = CoordinatesSequence()
        coordinates_collection.add_coordinates(coordinates1)
        coordinates_collection.add_coordinates(coordinates2)
        first_return_coordinates = coordinates_collection.next_coordinates
        second_returned_coordinates = coordinates_collection.next_coordinates

        third_returned_coordinates = coordinates_collection.next_coordinates

        expected_coordinates = coordinates1
        self.assertEqual(expected_coordinates, third_returned_coordinates)

