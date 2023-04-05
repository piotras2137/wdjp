import csv
import random


# zadanie 1
def zamowienia():
    return 0
# zadanie 2


def scalpliki(lista: list, nowy: str):
    with open(nowy, "w") as wynik:
        for fn in lista:
            with open(fn, "r") as y:
                x = y.readlines()
                for line in x:
                    if line[-1] != "\n":
                        wynik.append(line+"\n")
                    else:
                        wynik.append(line)


# zadanie 3
def nnajwartosci(lista: list, n: int, najwieksze= True):
    for i in lista:
        if str(i).isnumeric() != True:
            lista.remove(i)
    lista.sort()
    print(lista)
    if najwieksze:
        return lista[-n:]
    else:
        return lista[:n]

print(nnajwartosci(["x",2,1,3,7,8,4,-1,6,2],3))
print(nnajwartosci(["y",2,1,3,7,8,4,-1],3,False))
# zadanie4
def zad4(lista: list):
    slownik = {"int":[], "str":[], "float":[]}
    for item in lista:
        if str(type(item)) == "<class 'int'>":
            slownik["int"].append(item)
        elif str(type(item)) == "<class 'float'>":
            slownik["float"].append(item)
        elif str(type(item)) == "<class 'str'>":
            slownik["str"].append(item)
    return slownik


mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
slownik = zad4(mieszana)
print(slownik)
# zadanie 5


def podzializapis(nazwiska: list):
    am = []
    nz = []
    for nazwisko in nazwiska:
        if nazwisko[0] <= "M":
            am.append(nazwisko)
        else:
            nz.append(nazwisko)

    with open("A-M_nazwiska.txt", "w") as plik:
        for x in am:
            plik.write(x+"\n")
    with open("N-Z_nazwiska.txt", "w") as plik:
        for x in nz:
            plik.write(x+"\n")


podzializapis(["Martyniuk", "Walczak", "Mrozowski", "Sliwa", "Adamiak"])

# zadanie 6


def odwracanietekstuwslowach(text: str):
    x = text.split(" ")
    ns = []
    for y in x:
        ns.append(y[::-1])
    return " ".join(ns)


print(odwracanietekstuwslowach("Twoja stara piła leży w piwnicy"))
# zadanie 7
imiona = ["Piotrek", "Kacper", "Marcel", "Szymon"]
kolory = ["karo", "pik", "kier", "trefl"]
figury = ["2", "3", "4", "5", "6", "7", "8",
          "9", "AS", "Król", "Dama", "Walet", "Joker"]
karty = []
for x in figury:
    for y in kolory:
        karty.append(x+" "+y)
wylosowane = []
for imie in imiona:
    reka = imie + ": "
    for i in range(5):
        x = random.choice(karty)
        while (x in wylosowane):
            x = random.choice(karty)
        wylosowane.append(x)
        reka += x+", "
    print(reka)
# zadanie 8


def nazwiskanaemail(nazwapliku, domena):
    plik2 = open("email"+nazwapliku, 'w')
    with open(nazwapliku, 'r') as plik:
        x = plik.readlines()
        for line in x:
            email = line.strip("\n").replace(" ", ".")+"@"+domena
            plik2.write(line.strip('\n')+", " + email + "\n")
    plik2.close()


nazwiskanaemail("nazwiska.txt", "infbud.pl")
# zadnie 9


def kolofortuny():
    plik = open("kolofortuny.txt", 'r')
    hasla = [line.strip("\n") for line in plik.readlines()]
    wybrane = random.choice(hasla)
    odgadniete = []
    while (1):
        printstr = ""
        for letter in wybrane:
            if (letter in odgadniete or letter == " "):
                printstr += letter
            else:
                printstr += "_"
        print(printstr)
        print("podaj litere")
        x = input()
        if (x not in wybrane):
            print("zle, takiej litery nie ma w hasle")
        elif (x == " "):
            print("nie musisz podawać spacji")
        else:
            odgadniete.append(x)

        if (len(odgadniete) == len(wybrane.strip(" "))):
            print("brawo, zgadles haslo")
            break


kolofortuny()
