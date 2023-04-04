# zadanie 2 
def funkcjazadanie2(liczba):
    #funckja sprawdza czy liczba jest integerem i jak jest to zwraca ilosc bitow o wartosci 1 w tej liczbie oraz 1, w przeciwnym wypadku zwraca 0 i 0 
    if liczba.is_integer():
        return int(liczba).bit_count(), 1
    else:
        return 0,0


print(funkcjazadanie2(6.9))
print(funkcjazadanie2(7.0))


# zadanie 1 
int1 = int('100001011001',2)
int2 = int('abcdef',16)
float1 =1.1111
float2 =int1/2.0 
print(int1)
print(int2)
print(float1)
print(float2)

# zadanie 3 
#mnozenie przez 2
x = 21 
x = x<<1
print(x)
#dzielenie przez 2
x = x>>1
print(x)
#czesc wspolna
y = 3
print(x&y)
#wszystkie jedynki
x = 4 
print(x|y)
