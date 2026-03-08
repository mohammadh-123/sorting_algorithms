
import random
import numpy as np
import os

def test_generator(file_name,num_of_arrays,min_size,max_size,min_value=-10000,max_value=10000):
    file_path = f"size_testing/{file_name}.npy"
    if not os.path.exists(file_path):  
        arrays = []      
        for i in range(num_of_arrays):
            size = random.randint(min_size,max_size)
            array = np.random.randint(min_value,max_value,size)
            arrays.append(array)
        if num_of_arrays == 1:
            arrays = arrays[0]
        else:
            arrays = np.asarray(arrays,dtype=list)
        print(arrays)
        np.save(file_path,arrays,allow_pickle=True)
        
# test 1 is for 100000 arrays with sizes between 2 to 150   
# test 2 is for 100 arrays with sizes between 10000 to 30000
# test 3 is for 10 arrays with sizes between 1000000 to 10000000
# test 4 is for 1 arrays with size 100000000
test_generator('test1',100000,2,150)
test_generator('test2',100,10000,30000)
test_generator('test3',10,1000000,10000000)
test_generator('test4',1,100000000,100000000)


