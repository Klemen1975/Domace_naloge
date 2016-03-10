# -*- coding: utf-8 -*-

class kontakti:
    first_name=""
    last_name=""
    email=""
    phone=""
    address=""

    def __init__(self, first_name, last_name, email, phone, adress):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone=phone
        self.address=adress

    def polno_ime(self):
        print ("%s %s" %(self.first_name, self.last_name))

    def vnos_kontakta():
        return

        vnos=raw_input("Želite dodati nov kontakt(ja ali ne):")

        if vnos ==  "ja":
            print "Vensite zahtevane podatke:"

            repeat = "da"
            seznam=[]

            while repeat.lower().strip() == 'da':

                first_name = raw_input("Vpiši ime:")
                last_name = raw_input("Vpiši priimek:")
                email = raw_input("Vpiši email:")
                phone = raw_input("Vpiši številko:")
                address = raw_input("Vpiši naslov:")

                kontakt = (first_name+""+last_name+""+email+""+phone+""+address)

                seznam.append(kontakt)

                repeat=raw_input("Ali boste dodali še en kontakt: (da ali ne)? ")
    vnos_kontakta()




