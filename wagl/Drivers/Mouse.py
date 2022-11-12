try:
    from win32 import win32gui
except:
    from os import system

    system("pip install pywin32")
    system("python Scripts/pywin32_postinstall.py -install")
    from win32 import win32gui


class Mouse:
    def __init__(self):
        self.position = win32gui.GetCursorPos()
