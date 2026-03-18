from dataclasses import dataclass
from typing import Tuple


@dataclass
class WindowConfig:
  title: str
  position: Tuple  # (left, top)
  size: Tuple  # (width, height)


CONFIGS = [
    WindowConfig(
        title='- Google Chrome',
        position=(-7, 0),
        size=(1294, 840)),
]
