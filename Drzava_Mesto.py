# -*- coding: utf-8 -*-

#Seznam Držav z glavnimi mesti

Drzava_mesto = {"Slovenija":"Ljubljana",
         "Hrvaška":"Zagreb",
         "Srbija":"Beograd",
         "Avstrija":"Dunaj",
         "Madžarska":"Budimpešta",
         "Italija":"Rim",
         "Francija":"Pariz",
         "Španija":"Madrid",
         "Portugalska":"Lizbona",
         "Švica":"Bern",
         "Nemčija":"Berlin",
         "Nizozemska":"Amsterdam",
         "Danska":"Kopenhagen",
         "Švedska":"Stockholm",
         "Norveška":"Oslo",
         "Finska":"Helsinki",
         "Rusija":"Moskva",
         "Poljska":"Varšava",
         }

#Funkcija

def izpisi_mesto():
    return 'mesto'

drzava = raw_input("Vpiši državo:")

if drzava in Drzava_mesto.keys():
    mesto = Drzava_mesto[drzava]
    print("Glavno mesto je: %s" %(mesto))

else:
    print "Navedene države ni v seznamu"

izpisi_mesto()

def kontrola():
    return

drzava_kont= raw_input("Vpiši državo:")
mesto_kont = raw_input("Vpiši glavno mesto:")

mesto = Drzava_mesto[drzava_kont]
drzava_kont = Drzava_mesto.keys()

if mesto_kont == mesto:
    print ("Vaš odgovor je pravilen!")

else:
    print ("Vaš odgovor ni pravilen")

kontrola()