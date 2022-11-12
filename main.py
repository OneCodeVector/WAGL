import wagl
import sys
import  time

Keyboard = wagl.Drivers.Keyboard
Mouse = wagl.Drivers.Mouse()
Window = wagl.Drivers.Graphics.Window(title = "HI")

Mouse_Position = None
Running = True

Keyboard.Get_Key_Events.start()

while Running:
    Window.Load_Frame()

    Old_Mouse_Position = Mouse.position
    Mouse = wagl.Drivers.Mouse()
    New_Mouse_Position = Mouse.position

    if Old_Mouse_Position != New_Mouse_Position:
        Mouse_Position = New_Mouse_Position
        print(Mouse_Position)

    if Keyboard.Key_Pressed != None:
        if str(Keyboard.Key_Pressed) == "Key.esc":
            Window.Destroy()
            Running = False
            sys.exit()

        Keyboard.Key_Pressed = None
    time.sleep(0.01)

Keyboard.Get_Key_Events.join()
