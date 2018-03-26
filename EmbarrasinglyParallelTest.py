from joblib import Parallel, delayed
import multiprocessing
import numpy as np
import time

def my_function(i):
    output = np.power(i, 3)
    return output

if __name__ == "__main__":   

   X = np.random.randint(0,255,size=(int(1e5), 1))
   F = np.zeros(X.shape)
   start_time = time.time()
   F = [my_function(element) for element in X]
   outArr = np.asarray(F)
   print("Serial Execution time: {0} seconds".format(time.time()-start_time))
   
   nCPU = multiprocessing.cpu_count()
   p_time = time.time()
   results = Parallel(n_jobs=nCPU)(delayed(my_function)(i) for i in range(X.shape[0]))
   print("Parallel Execution time: {0} seconds".format(time.time()-p_time))
