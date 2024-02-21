from string import *
from random import *
import random



#Kivi-paber-käärid
mängijad=input("Sisestage mängija nimi: ")
kuip=int(input("Mitu vootu soovite mängida: "))
for mängija in mängijad:
    valik=input(f"{mängija} vali oma käik näiteks (kivi, paber,käärid" ).lower()
    robori_valik= random.choice(["kivi","paber","käärid"])
    print(f"{mängija} valinud {valik}, robot valinud {roboti_valik} " )
    if valik == roboti_valik:
        print("võitajat pole")
    elif (valik == "kivi" and roboti_valik == "käärid") or \
         (valik == "paber" and roboti_valik == "kivi") or \
         (valik == "kivi" and roboti_valik == "paber"):
        print(f"{mängija} vooru võitis")
        tulemused[mängija] += 1
