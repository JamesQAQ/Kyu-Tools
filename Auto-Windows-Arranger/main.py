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
  for window in pygetwindow.getAllWindows():
    if isRealWindow(window):
      config = getConfig(window)
      if config:
        window.moveTo(config.position[0], config.position[1])
        window.resizeTo(config.size[0], config.size[1])
