
import random
import numpy as np
import os
import string

def get_random_word(length = 5):
    chars = string.ascii_letters
    word = [random.choice(chars) for _ in range(length) ]
    return ''.join(word)

def test_generator(file_name,structure_type,min_value=-10000,max_value=10000,string_length=5):
    sizes = [20,100,1000,5000,10000,20000,30000]
    file_path = f"data_type_testing/{file_name}.npy"
    if not os.path.exists(file_path):
        arrays=[]
        for size in sizes:
            if structure_type == 1:
               array = np.random.randint(min_value,max_value,size)
               arrays.append(array)
            elif structure_type == 2:
                array = np.random.random(size) * 10000
                arrays.append(array)
            elif structure_type == 3:
                words = [get_random_word(string_length) for _ in range(size)]
                array = np.asarray(words,dtype = list)
                arrays.append(array)       
        arrays = np.asarray(arrays,dtype=list)
        print(arrays)
        np.save(file_path,arrays,allow_pickle=True)
        
# test 1 is for 7 integer arrays with the biggest size is 30000   
# test 2 is for 7 big integer arrays with the biggest size is 30000
# test 3 is for 7 float arrays with the biggest size is 30000
# test 4 is for 7 string arrays with the biggest size is 30000

test_generator('test1',1,-1000,1000)
test_generator('test2',1,-1000000,1000000)
test_generator('test3',2)
test_generator('test4',3,string_length=10)