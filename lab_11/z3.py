#Zad3
class Zad3:
    a: int
    b: int
    
    def __init__(self,x,y):
        self.a = x
        self.b = y
    
    def result(self):
        return self.a*self.b
    
    def __repr__(self) -> str:
        return f'({self.a}, {self.b})'
    
square = Zad3(3,5)
    
with open('lab_11/picled_inst', 'wb') as file:
    pickle.dump(square, file)

with open('lab_11/picled_inst', 'rb') as file:
    square_un = pickle.load(file)
  
print(square_un.result())

#test
with open('lab_11/picled_class', 'wb') as file:
    pickle.dump(Zad3, file)

with open('lab_11/picled_class', 'rb') as file:
    Zad3_un = pickle.load(file)

square2 = Zad3_un(5,5)
print(square2.result())
#działa :)