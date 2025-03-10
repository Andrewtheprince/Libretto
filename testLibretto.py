from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student("Harry", "Potter", 11, "castani",
                "castani", "Grifondoro", "civetta",
                "Expecto Patronum")
mylib = Libretto(Harry, [])

v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 21, "2022-02-12", False)
mylib.append(v1)
mylib.append(v2)

mylib.append(Voto("Pozioni", 21, "2022-06-14", False))
mylib.append(Voto("Trasfigurazione", 21, "2022-06-14", False))

mylib.calcolaMedia()

votiFiltrati = mylib.getVotiByPunti(21, False)
print(votiFiltrati)

votoTrasfigurazione = mylib.getVotoByName("Trasfigurazione")

if votoTrasfigurazione is None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione.materia)