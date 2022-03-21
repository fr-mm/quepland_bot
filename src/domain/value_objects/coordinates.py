from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int
