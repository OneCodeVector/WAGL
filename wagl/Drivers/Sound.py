try:
    import win32api

except:
    from os import system
    system("pip install pywin32")
    system("python Scripts/pywin32_postinstall.py -install")
    import win32api

class Sound():
    def __init__(self, **kwargs):
        self.freq = 500
        self.dela = 3000
    def Play_Freq(self, freq, dela):
        win32api.Beep(
            freq,
            dela,
        )
