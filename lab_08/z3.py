from timeit import timeit

setup = """
from collections import deque
kolejka = deque('Ala ma kota'.split())
"""
stmt1="""
for x in range(100_000):
    kolejka.append('?')
"""
stmt2="""
for x in range(100_000):
    kolejka.appendleft('Czy')
"""
print(timeit(stmt1, setup, number=1))
print(timeit(stmt2, setup, number=1))

setup = """
lista = 'Ala ma kota'.split()
"""
stmt1="""
for x in range(100_000):
    lista.append('?')
"""
stmt2="""
for x in range(100_000):
    lista.insert(0,'Czy')
"""
print(timeit(stmt1, setup, number=1))
print(timeit(stmt2, setup, number=1))