try:
    import mouse
except:
    from os import system
    system("pip install mouse")
    import mouse


class Mouse:
    def __init__(self):
        self.position = mouse.get_position()
