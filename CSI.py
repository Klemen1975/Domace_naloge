# -*- coding: utf-8 -*-

ziga = ["TGCAGGAACTTC", "AAAACCTCA", "TTAGCTATCGC", "AAGTAGTGAC", "ACCACAA"]

matej = ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"]

miha = ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]

dna = open("dna.txt","r").read()

if dna.find(ziga[0])>=0:
    print "Ziga DNA found"
else:
    print "Ziga DNA not found"
if dna.find(ziga[1])>=0:
    print "Ziga DNA found"
if dna.find(ziga[2])>=0:
    print "Ziga DNA found"
else:
    print "Ziga DNA not found"
if dna.find(ziga[3])>=0:
    print "Ziga DNA found"
else:
    print "Ziga DNA not found"
if dna.find(ziga[4])>=0:
    print "Ziga DNA found"
else:
    print "Ziga DNA not found"

if dna.find(matej[0])>=0:
    print "Matej DNA found"
else:
    print "Matej DNA not found"
if dna.find(matej[1])>=0:
    print "Matej DNA found"
if dna.find(matej[2])>=0:
    print "Matej DNA found"
else:
    print "Matej DNA not found"
if dna.find(matej[3])>=0:
    print "Matej DNA found"
else:
    print "Matej DNA not found"
if dna.find(matej[4])>=0:
    print "Matej DNA found"
else:
    print "Matej DNA not found"

if dna.find(miha[0])>=0:
    print "Miha DNA found"
else:
    print "Miha DNA not found"
if dna.find(miha[1])>=0:
    print "Miha DNA found"
if dna.find(miha[2])>=0:
    print "Miha DNA found"
else:
    print "Miha DNA not found"
if dna.find(miha[3])>=0:
    print "Miha DNA found"
else:
    print "Miha DNA not found"
if dna.find(miha[4])>=0:
    print "Miha DNA found"
else:
    print "Miha DNA not found"