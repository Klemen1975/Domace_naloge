from e_blagajna import izpisi_ceno

def testiranje_blagajne():
    assert izpisi_ceno("mleko") == 1.40
    print ("e-blagajna deluje pravilno")
testiranje_blagajne()