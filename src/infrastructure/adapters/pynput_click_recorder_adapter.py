from pynput import mouse, keyboard

from src.domain.entities import CoordinatesSequence
from src.domain.ports import ClickRecorderPort
from src.domain.value_objects import Coordinates


class PynputClickRecorderAdapter(ClickRecorderPort):
    __start_recording_trigger_key: keyboard.Key
    __mouse_listener: mouse.Listener
    __keyboard_listener: keyboard.Listener
    __coordinates_sequence: CoordinatesSequence

    def __init__(self) -> None:
        self.__start_recording_trigger_key = keyboard.Key.space

    def record_until_any_key_is_pressed(self) -> CoordinatesSequence:
        self.__coordinates_sequence = CoordinatesSequence()
        self.__create_listeners()
        self.__record_until_key_press()
        return self.__coordinates_sequence

    def wait_until_start_recording_trigger_key_is_pressed(self, key: keyboard.Key) -> None:
        self.__keyboard_listener = keyboard.Listener(
            on_press=lambda key_pressed: self.__keyboard_listener.stop()
        )
        with self.__keyboard_listener as listener:
            listener.join()

    def __create_listeners(self) -> None:
        self.wait_until_start_recording_trigger_key_is_pressed(self.__start_recording_trigger_key)
        self.__mouse_listener = mouse.Listener(
            on_click=self.__save_click_coordinates_to_sequence
        )
        self.__keyboard_listener = keyboard.Listener(
            on_press=self.__stop_listeners
        )

    def __record_until_key_press(self) -> None:
        self.__mouse_listener.start()
        with self.__keyboard_listener as keyboard_listener:
            keyboard_listener.join()

    def __stop_listeners(self, key: keyboard.Key) -> None:
        self.__mouse_listener.stop()
        self.__keyboard_listener.stop()

    def __save_click_coordinates_to_sequence(self, position_x: int, position_y: int, button: mouse.Button, pressed: bool) -> None:
        if pressed:
            self.__coordinates_sequence.add_coordinates(Coordinates(x=position_x, y=position_y))
