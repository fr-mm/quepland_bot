import pyautogui

from quepland_bot.domain.ports import MousePort
from quepland_bot.domain.value_objects import Coordinates


class PyautoguiMouseAdapter(MousePort):
    def click_on(self, coordinates: Coordinates) -> None:
        pyautogui.click(x=coordinates.x, y=coordinates.y)
