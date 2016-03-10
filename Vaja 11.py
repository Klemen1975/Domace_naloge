osebe1 = [{"ime":"Klemen"},
         {"ime":"Rok"}]
index = 0
while index < len(osebe1):
    oseba=osebe1[index]
    print (oseba["ime"])
    index=index+1


osebe2 = [{"ime":"Klemen"},
         {"ime":"Rok"},
          {"ime":"Mojca"},
          {"ime":"Peter"}]

osebe = [{"ime":"Matjaz"},
         {"ime":"Matej"},
         {"ime":"Miha"},
         {"ime":"Marko"}]



def izpisi_osebe():
    index = 0
    while index < len(osebe):
        oseba=osebe[index]
        print (oseba["ime"])
        index=index+1

izpisi_osebe()

from random import randint
print (randint(1,100))
