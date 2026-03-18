import argparse
import pygetwindow

from config import WindowConfig, CONFIGS


def getConfig(window: pygetwindow.Win32Window) -> WindowConfig:
  for config in CONFIGS:
    if config.title in window.title:
      return config


# This function is used filtered out the most of invisible windows.
def isRealWindow(window: pygetwindow.Win32Window) -> bool:
  return (
      window.title.strip()
      and window.visible
      and window.width > 0
      and window.height > 0
  )


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--list', action='store_true', help='list current windows')
  args = parser.parse_args()

  for window in pygetwindow.getAllWindows():
    if isRealWindow(window):
      if not args.list:
        config = getConfig(window)
        if config:
          window.moveTo(config.position[0], config.position[1])
          window.resizeTo(config.size[0], config.size[1])
      else:
        print(window)
