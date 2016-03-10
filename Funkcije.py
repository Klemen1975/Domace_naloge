osebe1 = [{"ime":"Klemen"},
         {"ime":"Rok"}]

osebe2 = [{"ime":"Klemen"},
         {"ime":"Rok"},
          {"ime":"Mojca"},
          {"ime":"Peter"}]

def izpisi_osebe(spremenljivka):
    index = 0
    while index < len(spremenljivka):
        oseba=spremenljivka[index]
        print (oseba["ime"])
        index=index+1

izpisi_osebe(osebe1)
izpisi_osebe(osebe2)

stevilka=raw_input("Vnesi stevilo:")
stevilka=int(stevilka)
def zmnozi(prvo_stevilo, drugo_stevilo):
    rezultat=prvo_stevilo*drugo_stevilo
    return (rezultat)
zmnozi (2,stevilka)

print zmnozi(2,stevilka)

zmnozek=zmnozi(2, stevilka)
print zmnozek

n1=raw_input("Vnesi prvo stevilo:")
n2=raw_input("Vnesi drugo stevilo:")
n1=int(n1)
n2=int(n2)
def zmnozi(n1, n2)
    rezultat=n1*n2
    return (rezultat)
print rezultat
