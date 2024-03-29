from typing import Any, List, Union
# zadanie 1. 
def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: (isinstance(x, int) or isinstance(x, float)) and not isinstance(x, bool), vals))

print(extract_numbers([21, 37, "xd", True, "4.20", 6.9]))

# zadanie 2
x = input("podaj wyrazy oddzielone spacją ")
lista = x.split(" ")
print(list(sorted(lista, key=lambda x: len(x))))

# zadanie 3 
def sort_mixed_list(lst: List[Union[int, str]], reversed: bool = True) -> List[Union[int, str]]:
    sorted_lst = sorted(lst, key=lambda x: (isinstance(x, str), x), reverse=reversed)
    return sorted_lst

lst1 = [12, "abc", "acb", 14, "cbd"]
sorted_lst1 = sort_mixed_list(lst1)
print(sorted_lst1)

# zadanie 5
def foo(vals: dict[str, list[int]], func) -> dict[str, list[int]]: 
    return dict(sorted(vals.items(), key=lambda x: func(x[1]), reverse=True))
    
print(foo({'Jan': [2,1,3,7], 'Zbigniew': [6, 9, 6], 'Kamil': [4, 10, 10]}, sum))