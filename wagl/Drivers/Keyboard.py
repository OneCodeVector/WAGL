try:
    from pynput import keyboard
except:
    from os import  system
    system("pip install pynput")
    from pynput import keyboard

Key_Pressed = None

def on_press(key):
    global Key_Pressed
    Key_Pressed = key

Get_Key_Events = keyboard.Listener(on_press=on_press)

