from timeit import timeit

setup = """
from array import array
import random
"""

stmt1 = """
array_of_ints = array('i', [random.randint(1, 1000) for _ in range(1_000_000)])
"""

stmt2 = """
list_of_ints = [random.randint(1, 1000) for _ in range(1_000_000)]
"""

stmt3 = """
array_of_longs = array('q', [random.randint(1, 1000) for _ in range(1_000_000)])
"""

stmt4 = """
list_of_longs = [random.randint(1, 1000) for _ in range(1_000_000)]
"""

stmt5 = """
array_of_chars = array('u', ['a' for _ in range(1_000_000)])
"""

stmt6 = """
list_of_chars = ['a' for _ in range(1_000_000)]
"""

print("Czas inicjowania tablicy typu int: ", timeit(stmt1, setup, number=100))
print("Czas inicjowania listy typu int: ", timeit(stmt2, setup, number=100))
print("Czas inicjowania tablicy typu long: ", timeit(stmt3, setup, number=100))
print("Czas inicjowania listy typu long: ", timeit(stmt4, setup, number=100))
print("Czas inicjowania tablicy znaków: ", timeit(stmt5, setup, number=100))
print("Czas inicjowania listy znaków: ", timeit(stmt6, setup, number=100))