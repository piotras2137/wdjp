from array import array
from datetime import datetime

import random 

print("=======Array=======")
print("=======Write=======")
start = datetime.now()
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
with open('lab_08/floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)
end = datetime.now()
print(end-start)
print("=======Read=======")
start = datetime.now()
list_of_floats = [random.random() for _ in range(1_000_000)]
with open('lab_08/floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
end = datetime.now()
print(end-start)
print("=======List=======")
print("=======Write=======")
start = datetime.now()
tab_of_floats_loaded = array('f')
file_arr = open('lab_08/floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()
end = datetime.now()
print(end-start)
print("=======Read=======")
start = datetime.now()
with open('lab_08/floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()
list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
end = datetime.now()
print(end-start)
print("==================")
