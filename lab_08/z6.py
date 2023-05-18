from collections import deque, namedtuple, Counter

def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())


print(create_kolo_fortuny(4,5,6,7,4,6,2,7,4,5,6,6,5,3,5,5,3,4,5,1))