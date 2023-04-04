import csv 
import random 


# zadanie 1
# zadanie 2 
# zadanie 3
# zadanie 4 
# zadanie 5
# zadanie 6
def odwracanietekstuwslowach(text: str):
    x  = text.split(" ")
    ns = []
    for y in x:
        ns.append(y[::-1])
    return " ".join(ns)

print(odwracanietekstuwslowach("Twoja stara piła leży w piwnicy"))
# zadanie 7
imiona = ["Piotrek", "Kacper", "Marcel", "Szymon"]
kolory = ["karo", "pik", "kier", "trefl"]
figury = ["2", "3", "4", "5", "6", "7", "8", "9", "AS", "Król", "Dama", "Walet", "Joker"]
karty = []
for x in figury:
    for y in kolory:
        karty.append(x+" "+y)
wylosowane = []
for imie in imiona:
    reka = imie + ": "
    for i in range(5):
        x = random.choice(karty)
        while(x in wylosowane):
            x = random.choice(karty)
        wylosowane.append(x)
        reka+=x+", "
    print(reka)
# zadanie 8  
# zadnie 9 