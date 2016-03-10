# -*- coding: utf-8 -*-
class Oseba:
    ime = ""
    priimek = ""

    def __init__(self, ime, priimek):
        self.ime = ime
        self.priimek = priimek

    def izpisi_osebo (self):
        print (self.ime)
        print (self.priimek)

class Ucitelj(Oseba):
    predmet = ""

    def __init__(self, ime, priimek, predmet):
        self.ime = ime
        self.priimek = priimek
        self.predmet = predmet

    def izpisi_predmet (self):
        print(self.predmet)



ucitelj = Ucitelj(ime = "Klemen", priimek = "Peklaj", predmet = "Fizika")
ucitelj.izpisi_osebo()
ucitelj.izpisi_predmet