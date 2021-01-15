import numpy as np
import time

def linearSearch(key, veriMiktari):
    

    data = np.random.randint(0, 100000, veriMiktari)
    data.sort()
    
    start = time.time()
    
    for i in range(0, len(data)):
        if key == data[i]:
            return "found", i, i, time.time()-start, data
        elif i == len(data)-1:
            return "notfound", i, i, time.time()-start, data