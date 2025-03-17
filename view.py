import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._controller = None
        self._page = page


    def loadInterface(self):
        pass

    def setController(self, c):
        self._controller = c

