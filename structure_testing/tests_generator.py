
import random
import numpy as np
import os

def test_generator(file_name,structure_type,min_value=-10000,max_value=10000):
    sizes = [20,100,1000,5000,10000,30000,50000]
    file_path = f"structure_testing/{file_name}.npy"
    if not os.path.exists(file_path):
        arrays=[]
        if structure_type ==5:
            sizes.append(100000000)
            structure_type = 2
        for size in sizes:
            if structure_type == 1:
               array = np.sort(np.random.randint(min_value,max_value,size))
               arrays.append(array)
            elif structure_type == 2:
                array = np.sort(np.random.randint(min_value,max_value,size))
                array = array[::-1] 
                arrays.append(array)
            elif structure_type == 3:
                mid = size // 2
                arr = np.random.randint(min_value,max_value,size)
                sorted_half = np.sort(arr[:mid])
                array = np.concatenate((sorted_half , arr[mid:])) 
                arrays.append(array)
            elif structure_type == 4:
                partition = int(size * 0.95)
                arr = np.random.randint(min_value,max_value,size)
                sorted_part = np.sort(arr[:partition])
                array = np.concatenate((sorted_part ,arr[partition:]))  
                arrays.append(array)
            elif structure_type == 5:
                array = np.sort(np.random.randint(min_value,max_value,size))
                array = array[::-1] 
                arrays.append(array)
            
        arrays = np.asarray(arrays,dtype=list)
        np.save(file_path,arrays,allow_pickle=True)
        
# test 1 is for 7 sorted arrays with the biggest size is 50000   
# test 2 is for 7 reversed sorted arrays with the biggest size is 50000
# test 3 is for 7 half sorted arrays with the biggest size is 50000
# test 4 is for 7 95% sorted arrays with the biggest size is 50000
# test 5 is for 8 reversed sorted arrays with the biggest size is 100000000

test_generator('test1',1)
test_generator('test2',2)
test_generator('test3',3)
test_generator('test4',4)
test_generator('test5',5)