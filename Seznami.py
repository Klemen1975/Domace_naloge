avtomobili = ["volvo","bmw","audi","skoda"]
stevilke = [1,2,3]
print (avtomobili[0])
print len(avtomobili)
print(avtomobili)
for avto in avtomobili:
    print (avto+" X5")
avtomobili.append("ferrari")
print (avtomobili)
avtomobili[1]="ficko"
print avtomobili
print (avtomobili.index("skoda"))
avtomobili.remove("skoda")
print (avtomobili)
avtomobili.append("skoda")
avtomobili.append("skoda")
print avtomobili
print avtomobili.count("skoda")
stevec=0
for avto in avtomobili:
    if avto == "skoda":
        stevec = stevec +1
print stevec
if "audi" in avtomobili:
    print("audi je notri")

ucenec = {"ime":"Klemen", "priimek":"Peklaj"}
print (ucenec["priimek"])

ucenci=[{"ime":"Klemen","priimek":"Peklaj"},{"ime":"Klem"},{"ime":"Klen"} ]
print (ucenci[0])
ucenec=ucenci[0]
print (ucenec["ime"]+" "+ucenec["priimek"])
for kljuc in ucenec:
    print (kljuc)
    print (ucenec[kljuc])