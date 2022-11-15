try:
    import win32api

except:
    from os import system
    system("pip install pywin32")
    system("python Scripts/pywin32_postinstall.py -install")
    import win32api

from threading import *

def beep(freq, dela):
    win32api.Beep(
        freq,
        dela,
    )

class Sound():
    def __init__(self, **kwargs):
        self.freq = 500
        self.dela = 1000
    def Play_Freq(self, freq, dela):
        Sound_Thread = Thread(target = beep, args = (self.freq, self.dela))
        Sound_Thread.start()
        Sound_Thread.join()
