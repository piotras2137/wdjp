from collections import deque, namedtuple, Counter
import random
import time

def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())



def spinit(fortune: deque, wygrana: int):
    fortune.rotate(random.randint(0, len(fortune)))

    print(f"Aktualny stan koła: {fortune}")
    if fortune[0] != wygrana:
        time.sleep(1)
        spinit(fortune, wygrana)
       
fortune = create_kolo_fortuny(9,2,3,4,5,6,7,8,1)
wygrana = fortune[0] #albo random.choice(fortune)

fortune.rotate(1)
spinit(fortune, wygrana)
print("Wygrałeś")