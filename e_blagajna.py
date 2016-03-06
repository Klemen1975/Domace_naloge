# -*- coding: utf-8 -*-

#Blago zavedeno v blagajni

blago = {"mleko":1.40,
         "kruh":0.80,
         "sir":0.65,
         "salama":0.95,
         "marmelada":0.75,
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
         "bonboni":1.15,
         "čips":0.45,
         }

#Funkcija

def izpisi_ceno():
    return

if __name__ == "__main__":

    nakup=[]
    cena=float
    repeat = "da"
    index=0
    index=index+1

    while repeat.lower().strip() == 'da':

        izdelek = raw_input("Izberi izdelek:")

        if izdelek in blago.keys():
            cena = blago[izdelek]
            nakup.insert(index, cena)
            print("Cena izdelka je %s" %(cena))

        else:
            print "Navedenega izdelka ni v seznamu"
        repeat=raw_input("Ali boste še nakupovali (da ali ne)? ")

izpisi_ceno()

vrednost_nakupa = sum(nakup)
print("Vrednost vašega nakupa je:%s" %(vrednost_nakupa))









