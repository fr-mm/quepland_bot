from typing import Callable
from pynput import keyboard

from src.domain.ports import MouseLoopBreakerPort


class PynputMouseLoopBreakerAdapter(MouseLoopBreakerPort):
    __break_loop_callback: Callable
    __keyboard_listener: keyboard.Listener

    def __init__(self, break_loop_callback: Callable) -> None:
        self.__break_loop_callback = break_loop_callback

    def break_when_any_key_is_pressed(self) -> None:
        self.__keyboard_listener = keyboard.Listener(
            on_press=lambda key: self.__break_loop()
        )
        self.__keyboard_listener.start()

    def __break_loop(self) -> None:
        self.__keyboard_listener.stop()
        self.__break_loop_callback()
        print(f'Loop interrupted')
