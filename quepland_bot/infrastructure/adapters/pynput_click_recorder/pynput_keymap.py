from typing import Dict

from pynput import keyboard

from quepland_bot.domain.enums import KeyboardKeyEnum


class PynputKeymap:
    __keymap: Dict[keyboard.Key, KeyboardKeyEnum]

    def __init__(self) -> None:
        self.__keymap = {
            keyboard.Key.space: KeyboardKeyEnum.SPACE,
            keyboard.Key.esc: KeyboardKeyEnum.ESC
        }

    def get_by_pynput_key(self, key: keyboard.Key) -> KeyboardKeyEnum:
        return self.__keymap[key]
