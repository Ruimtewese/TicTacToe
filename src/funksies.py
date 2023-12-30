'''
==============================================================
File:       funksies.py  
Developer:  Ruimteman
Date:       05/08/2023
Description:
    Al die funksies wat ek nodig het om Tic-Tac-Toe te speel    
==============================================================
'''


def bord(x):
    print("=============")
    print("| %s | %s | %s |" % (x[0], x[1], x[2]))
    print("=============")
    print("| %s | %s | %s |" % (x[3], x[4], x[5]))
    print("=============")
    print("| %s | %s | %s |" % (x[6], x[7], x[8]))
    print("=============")

def nuwe_reeks(reeks, x, wat):
    return reeks[:x-1] + wat + reeks[x:]

def speel(lys, speler):
    while True:
        posisie = input("Speler %s kies 'n posisie: "%(speler))
        
        if posisie in lys:
            nuwe_lys = nuwe_reeks(lys, int(posisie), speler)
            bord(nuwe_lys)
            return nuwe_lys
        else:
            print("Speler %s, probeer weer! "%(speler))

def toets_vir_wen(lys, wenner):
    ry_1_2_3 = lys[0] + lys[1] + lys[2]
    ry_4_5_6 = lys[3] + lys[4] + lys[5]
    ry_7_8_9 = lys[6] + lys[7] + lys[8]    
    kolom_1_4_7 = lys[0] + lys[3] + lys[6]
    kolom_2_5_8 = lys[1] + lys[4] + lys[7]
    kolom_3_6_9 = lys[2] + lys[5] + lys[8]
    diagonaal_1_5_9 = lys[0] + lys[4] + lys[8]
    diagonaal_3_5_7 = lys[2] + lys[4] + lys[6]  


    if ("XXX" in ry_1_2_3 or "XXX" in ry_4_5_6 or "XXX" in ry_7_8_9 or
        "OOO" in ry_1_2_3 or "OOO" in ry_4_5_6 or "OOO" in ry_7_8_9 or
        "XXX" in kolom_1_4_7 or "XXX" in kolom_2_5_8 or "XXX" in kolom_3_6_9 or
        "OOO" in kolom_1_4_7 or "OOO" in kolom_2_5_8 or "OOO" in kolom_3_6_9 or
        "XXX" in diagonaal_1_5_9 or "XXX" in diagonaal_3_5_7 or
        "OOO" in diagonaal_1_5_9 or "OOO" in diagonaal_3_5_7  
        ):
        print("Wenner is %s"%(wenner))
        gewen = 1
        return gewen

