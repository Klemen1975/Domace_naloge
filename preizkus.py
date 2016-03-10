# -*- coding: utf-8 -*-

#Blago zavedeno v blagajni

blago = {"mleko":1.40,
         "kruh":0.80,
         "jabolka":0.65,
         "hruške":0.50,
         "kava":1.10,
         "whisky":3.50,
         "pivo":2.20,
         "vino":2.85,
         "vodka":3.70,
         "tekila":3.10,
         "rum":2.90,
         "čokolada":1.90,
         "piškoti":1.20,
         "marmelada":0.75,
         "sir":0.65,
         }

#Funkcija

def izpisi_ceno():
    return

if __name__ == "__main__":

    repeat = "da"

    while repeat.lower().strip() == 'da':

        izdelek = raw_input("Izberi izdelek:")

        if izdelek in blago.keys():
            cena = blago[izdelek]
            print("Cena izdelka je %s" %(cena))
        else:
            print "Navedenega izdelka ni v seznamu"

        repeat=raw_input("Ali boste se nakupovali (da ali ne)? ")

izpisi_ceno()