# zadanie 1
import string
numbers = list(range(1, 11))

pierwsza = numbers[:5]
druga = numbers[5:]

print(pierwsza)
print(druga)

# zadanie 2

polaczona = druga + pierwsza

# Dodawanie wartości "0" na początku listy
polaczona.insert(0, 0)

# Tworzenie kopii listy
posortowana = polaczona.copy()

# Sortowanie listy malejąco
posortowana.sort(reverse=True)

# Wyświetlanie list
print(polaczona)
print(posortowana)

# zadanie 3

# Wczytanie tekstu ze standardowego wejścia
text = input()

# Tworzenie zbioru unikalnych znaków
unique_chars = set(text.lower())

# Sortowanie znaków alfabetycznie
posortowaneznaki = sorted(unique_chars)

# Wyświetlanie ciągu unikalnych znaków
print(''.join(posortowaneznaki))

# zadanie 4
# Tworzenie słownika z nazwami polskich miesięcy
miesiace = {
    1: 'styczeń',
    2: 'luty',
    3: 'marzec',
    4: 'kwiecień',
    5: 'maj',
    6: 'czerwiec',
    7: 'lipiec',
    8: 'sierpień',
    9: 'wrzesień',
    10: 'październik',
    11: 'listopad',
    12: 'grudzień'
}

# Wyświetlanie słownika
print(miesiace)

# zadanie 5
# Tworzenie słownika z nazwami angielskimi miesięcy
miesiaceang = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

# Łączenie słowników
miesiaceplang = {
    'pl': miesiace,
    'en': miesiaceang
}

# Wyświetlanie słownika
print(miesiaceplang)

# zadanie 6
name = 'Marianna'
dictionary = dict.fromkeys(name, 1)
print(dictionary)

# zadanie 7

text = input('Wprowadź dowolny tekst: ')
text_lower = text.lower()

lowercase_letters = string.ascii_lowercase
digits = string.digits

lowercase_count = sum(1 for char in text_lower if char in lowercase_letters)
digits_count = sum(1 for char in text_lower if char in digits)

print(f'W tekście jest {lowercase_count} ({lowercase_count/len(text_lower)*100:.2f}%) małych liter i {digits_count} ({digits_count/len(text_lower)*100:.2f}%) cyfr.')
