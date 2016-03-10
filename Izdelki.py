class Izdelek:
    ime = ""
    cena = ""
    teza =""

    def __init__(self, ime, cena, teza):
        self.ime=ime
        self.cena=cena
        self.teza=teza


izdelek1 = Izdelek(ime="mleko", cena=1, teza="1 kg")
izdelek2 = Izdelek(ime="sir", cena=2, teza="1.5 kg")
izdelek3 = Izdelek(ime="kruh", cena=3, teza="0.5 kg")

znesek = 0
seznam = [izdelek1, izdelek2, izdelek3]

for Izdelek in seznam:
    znesek=znesek+Izdelek.cena

print znesek




