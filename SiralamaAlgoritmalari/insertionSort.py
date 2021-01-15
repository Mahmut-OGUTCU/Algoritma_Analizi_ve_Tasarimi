import numpy as np
import time

def insertionSort(veriMiktari):
    veriDizini = np.random.randint(0, 100000, veriMiktari)
    copyveriDizini = veriDizini.copy()
    start = time.time()
    islemSayisi = 0
    
    for i in range(1, veriMiktari):
        islemSayisi +=2
        key = veriDizini[i]
        j = i - 1
    
        while 0 <= j and key < veriDizini[j]:
            islemSayisi += 3
            veriDizini[j + 1] = veriDizini[j]
            j -= 1
            veriDizini[j + 1] = key
    
    return veriDizini, islemSayisi, time.time()-start, copyveriDizini