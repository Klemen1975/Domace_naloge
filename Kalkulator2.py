
def sestevanje(x, y):
    return x + y
def odstevanje(x, y):
    return x - y
def mnozenje(x, y):
    return x * y
def deljenje(x, y):
    return x / y


repeat = "yes"

while repeat.lower().strip() == 'yes':
    print("Izberi operacijo:")
    print("1.sestevanje")
    print("2.odstevanje")
    print("3.mnozenje")
    print("4.deljenje")

    izbira = raw_input("Izberi operacijo (1/2/3/4):")

    x=int(raw_input("Vnesi prvo stevilo:"))
    y=int(raw_input("Vnesi drugo stevilo:"))

    if izbira == '1':
        print "Rezultat:", sestevanje(x, y)

    elif izbira == '2':
        print "Rezultat:",odstevanje(x, y)

    elif izbira == '3':
        print "Rezultat:",mnozenje(x, y)

    elif izbira == '4':
        print "Rezultat:",deljenje(x, y)

    else:
        print("Napaka")

    repeat=raw_input("Ali bos se kalkuliral (yes or no)? ")
