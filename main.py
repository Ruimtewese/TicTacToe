'''
=============================================================
File:       main.py  
Developer:  Ruimteman
Date:       05/08/2023
Description:
    Tic-Tac-Toe game   
==============================================================
'''

from src.funksies import bord
from src.funksies import speel
from src.funksies import toets_vir_wen


while True:

    lys = "123456789" 
    bord(lys)
    counter = 0

    while True:
        #speler X se beurt
        speler = "X"
        lys = speel(lys, speler)
        if toets_vir_wen(lys, speler) == 1 : break
        counter += 1
        if counter == 9:
            print("Dit is gelykop!")
            break

        #speler O se beurt
        speler = "O"
        lys = speel(lys, speler)
        if toets_vir_wen(lys, speler) == 1 : break
        counter += 1
        if counter == 9:
            print("Dit is gelykop!")
            break


    speel_verder = input("Wil jy nog speel?(J/N)").lower()    
    if speel_verder == "n": exit()
        


        
            


