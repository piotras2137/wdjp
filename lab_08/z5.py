from array import array
import random

tab_of_ints = sorted(array('I', [random.randint(0,1000000) for _ in range(1000)]))
print(tab_of_ints[len(tab_of_ints):len(tab_of_ints)-int(len(tab_of_ints)/10)-1:-1])