from view import View
from voto.voto import Libretto


class Controller:
    def __init__(self, v: View):
        self._view = v
        self._student = Student()
        self._model = Libretto(student, [])

    def handleAggiungi(self, e):
        strIn = self._view._txtIn.value
        if strIn =="":
            self._view._txtOut.value = "Errore: campo vuoto"
            self._view._page.update()
            return
        else:
            self._view._txtOut.value=strIn
            self._view._page.update()

    def getStudent(self):

