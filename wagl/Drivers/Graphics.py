try:
    from win32 import win32gui
    import win32ui
    import win32con

except:
    from os import system
    system("pip install pywin32")
    system("python Scripts/pywin32_postinstall.py -install")
    from win32 import win32gui
    import win32ui
    import win32con

from time import sleep

class Window:
    def __init__(self, **kwargs):
        #data
        self.title = None
        self.geometry = (900, 900)
        
        #window
        self.wc = win32gui.WNDCLASS()
        self.wc.lpszClassName = 'test_win32gui_1'
        self.wc.style = win32con.CS_GLOBALCLASS | win32con.CS_VREDRAW | win32con.CS_HREDRAW
        self.wc.hbrBackground = win32con.COLOR_WINDOW + 1
        self.class_atom = win32gui.RegisterClass(self.wc)
        self.win_obj = win32gui.CreateWindow(
            self.wc.lpszClassName,
            self.title,
            win32con.WS_CAPTION | win32con.WS_VISIBLE,
            100, 100, *self.geometry, 0, 0, 0, None
        )

    def Load_Frame(self):
        win32gui.InvalidateRect(self.win_obj,None,False)
        win32gui.PumpWaitingMessages()
        
    def Destroy(self):
        win32gui.PostMessage(self.wc, win32con.WM_CLOSE,0,0)
