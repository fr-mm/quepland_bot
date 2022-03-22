from quepland_bot.domain.entities import CoordinatesSequence
from quepland_bot.domain.enums import CommandKeyEnum
from quepland_bot.domain.ports import ClickRecorderPort


class RecordClicksUseCase:
    __click_recorder: ClickRecorderPort

    def __init__(self, click_recorder: ClickRecorderPort) -> None:
        self.__click_recorder = click_recorder

    def execute(self) -> CoordinatesSequence:
        print(f'Press {CommandKeyEnum.START_RECORDING_CLICKS.value.value} to start recording')
        self.__click_recorder.wait_until_start_recording_trigger_key_is_pressed()
        print('Recording clicks, press any key to stop')
        coordinates_sequence = self.__click_recorder.record_until_any_key_is_pressed()
        print(f'Recorded {coordinates_sequence.length} clicks')
        return coordinates_sequence
