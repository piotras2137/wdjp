# zadanie 1
import random
from random import randint
A = {1/x for x in range(1, 11)}
B = {2**x for x in range(11)}
C = {x for x in B if x % 4 == 0}
print(A)
print(B)
print(C)

# zadanie 2
macierz = [[random.randint(1, 10) for j in range(4)] for i in range(4)]
diagonalna = [macierz[i][i] for i in range(4)]
print(macierz)
print(diagonalna)

# zadanie 3
text = "Ala ma kota."

result = ((word, [ord(c) for c in word]) for word in text.split())

for tuple in result:
    print(tuple)

# zadanie 4
# jest w pliku zadanie4.py

# zadanie 5


def dice_throw(n: int) -> list():
    dice = dict.fromkeys([x for x in range(1, 7)], 0)
    for x in range(n):
        throw = randint(1, 6)
        dice[throw] += 1
    return [(f'oczka: {x}', f'rzutów: {dice[x]}') for x in range(6, 0, -1)]


rzuty = int(input("podaj ilość rzutów kostką"))
print(dice_throw(rzuty))
# zadanie 6


def ciag(* slowa) -> list():
    # jeżeli nie ma argumentów to
    if len(slowa) == 0:
        return list()
    else:
        return sorted([x for x in slowa])


# wywołanie gdy brak argumentów
print(ciag())
print(ciag('jest', 'dobrze', 'pozdrawiam', 'całą', 'legnicę'))

# zadanie 7


def points(** teams: dict()) -> int:
    return sum([teams[x] for x in teams])
