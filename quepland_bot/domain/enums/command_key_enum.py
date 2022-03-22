from enum import Enum

from quepland_bot.domain.enums.keyboard_key_enum import KeyboardKeyEnum


class CommandKeyEnum(Enum):
    START_RECORDING_CLICKS = KeyboardKeyEnum.SPACE
    INTERRUPT_LOOP = KeyboardKeyEnum.ESC
