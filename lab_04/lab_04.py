# zadanie 1
from bs4 import BeautifulSoup
import requests
import this
import sys

dec = int(input("Podaj liczbę całkowitą: "))
print("Liczba w postaci binarnej: ", bin(dec))
print("Liczba w postaci ósemkowej: ", oct(dec))
print("Liczba w postaci szesnastkowej: ", hex(dec))

# zadanie 2
value = input("Podaj wartość: ")
try:
    int(value)
    print("Podana wartość jest rzutowalna na typ int")
except ValueError:
    print("Podana wartość nie jest rzutowalna na typ int")
try:
    float(value)
    print("Podana wartość jest rzutowalna na typ float")
except ValueError:
    print("Podana wartość nie jest rzutowalna na typ float")

# zadanie 3
value = int(input("Podaj wartość: "))
result = []
multiplier = 1
while value > 0:
    digit = value % 10
    value //= 10
    result.append(str(digit) + " * " + str(multiplier))
    multiplier *= 10
sys.stdout.write("Podaną liczbę można zapisać jako: " +
                 " + ".join(reversed(result)))

# zadanie 4
encoder = this.d
sentence = input("Podaj zdanie do zakodowania: ")
encoded_sentence = ""
for c in sentence:
    if c.lower() in encoder:
        encoded_sentence += encoder[c.lower()]
    else:
        encoded_sentence += c
print(encoded_sentence)

# zadanie 5
sentence = input("Podaj zdanie: ")
words = sentence.split()
sorted_words = sorted(words, key=len)
print("Posortowane wyrazy: ", sorted_words)

# zadanie 6
url = "http://prawolaffera.pl/uniwersalny-kod-przemowien/"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
table = soup.find_all("table")[0]
rows = table.find_all("tr")[1:]
sentences = [row.find_all("td")[1].text.strip() for row in rows]
n = int(input("Podaj ilość zdań do wygenerowania: "))
for i in range(n):
    print(sentences[i % len(sentences)])
