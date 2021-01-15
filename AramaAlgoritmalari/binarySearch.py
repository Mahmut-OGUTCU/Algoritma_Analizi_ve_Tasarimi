import numpy as np
import time

def binarySearch(key, veriMiktari):
    
    data = np.random.randint(0, 100000, veriMiktari)
    data.sort()

    start = time.time()
    ilkDeger = 0
    sonDeger = len(data)
    ortanca = (ilkDeger + sonDeger) // 2
    islemSayisi = 4
    while ilkDeger <= sonDeger:
        
        islemSayisi += 1
        ortanca = (ilkDeger + sonDeger) // 2
        
        if data[ortanca] == key:
            islemSayisi += 1
            return "found", ortanca, islemSayisi, time.time()-start, data
    
        elif data[ortanca] > key:
            islemSayisi += 1
            sonDeger = ortanca - 1
        
        else:
            islemSayisi += 1
            ilkDeger = ortanca + 1
    
    index = -1
    return "notfound", ortanca, islemSayisi, time.time()-start, data