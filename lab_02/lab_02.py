# zadanie 1
print('podaj dane')
data = input()
print('podaj separator źródłowy')
zro = input()
print('podaj separator docelowy')
doc = input()

result = doc.join(data.split(zro))
# prostrze
#result = data.replace(zro, doc)
print(result)

# zadanie 2
akapit = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

litera1 = 'Piotr'[2]
litera2 = 'Martyniuk'[3]
ll1 = akapit.count(litera1)
ll2 = akapit.count(litera2)
print('W tekście jest', ll1, ' liter"',
      litera1, '" oraz ', ll2, ' liter "', litera2, '"')
