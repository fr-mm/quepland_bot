from pynput import mouse, keyboard

from quepland_bot.domain.entities import CoordinatesSequence
from quepland_bot.domain.enums import CommandKeyEnum
from quepland_bot.domain.ports import ClickRecorderPort
from quepland_bot.domain.value_objects import Coordinates
from quepland_bot.infrastructure.adapters.pynput_click_recorder.pynput_keymap import PynputKeymap


class PynputClickRecorderAdapter(ClickRecorderPort):
    __pynput_keymap: PynputKeymap
    __mouse_listener: mouse.Listener
    __keyboard_listener: keyboard.Listener
    __coordinates_sequence: CoordinatesSequence

    def __init__(self) -> None:
        self.__pynput_keymap = PynputKeymap()
        self.__start_recording_trigger_key = keyboard.Key.space

    def record_until_any_key_is_pressed(self) -> CoordinatesSequence:
        self.__coordinates_sequence = CoordinatesSequence()
        self.__create_listeners()
        self.__record_until_key_press()
        return self.__coordinates_sequence

    def wait_until_start_recording_trigger_key_is_pressed(self) -> None:
        self.__keyboard_listener = keyboard.Listener(
            on_press=lambda key_pressed: self.__stop_waiting_if_key_pressed_is_correct(key_pressed)
        )
        with self.__keyboard_listener as listener:
            listener.join()

    def __stop_waiting_if_key_pressed_is_correct(self, key: keyboard.Key) -> None:
        try:
            pressed_key = CommandKeyEnum.START_RECORDING_CLICKS.value
            command_key = self.__pynput_keymap.get_by_pynput_key(key)
            if pressed_key == command_key:
                self.__keyboard_listener.stop()

        except KeyError:
            pass

    def __create_listeners(self) -> None:
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
