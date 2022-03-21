import pyautogui

from src.domain.ports import MousePort
from src.domain.value_objects import Coordinates


class PyautoguiMouseAdapter(MousePort):
    def click_on(self, coordinates: Coordinates) -> None:
        pyautogui.click(x=coordinates.x, y=coordinates.y)
