import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._student = None
        self._titolo = None
        self._txtOut = None
        self._btnIn = None
        self._txtIn = None
        self._controller = None
        self._page = page


    def loadInterface(self):
        
        self._titolo = ft.Text("Libretto Voti", color="red", size=24)
        self._student = ft.Text(value=self._controller.getStudent(), color="brown", )
        self._txtIn = ft.TextField(label ="Inserisci nome")
        self._btnIn = ft.ElevatedButton("Aggiungi", on_click=self._controller.handleAggiungi)
        row = ft.Row(controls = [self._txtIn, self._btnIn])
        self._txtOut = ft.Text("")
        self._page.add(self._titolo, row, self._txtOut)
        

    def setController(self, c):
        self._controller = c

