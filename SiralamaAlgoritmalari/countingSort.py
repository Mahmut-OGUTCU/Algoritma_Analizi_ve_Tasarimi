import numpy as np
import time

def countingSort(veriMiktari):
    veriDizini = np.random.randint(0, 100000, veriMiktari)
    copyveriDizini = veriDizini.copy()
    start = time.time()
    
    islemSayisi = 0
    boyut = len(veriDizini)
    dizi1 = [0] * boyut
    
    dizi2 = [0] * 10
    
    for i in range(0, boyut):
        islemSayisi += 1
        dizi2[veriDizini[i]] += 1
    
    for i in range(1, 10):
        islemSayisi += 1
        dizi2[i] += dizi2[i - 1]
        
    i = boyut - 1
    while i >= 0:
        islemSayisi += 1
        dizi1[dizi2[veriDizini[i]] - 1] = veriDizini[i]
        dizi2[veriDizini[i]] -= 1
        i -= 1
        
    for i in range(0, boyut):
        veriDizini[i] = dizi1[i]        
    
    return veriDizini, islemSayisi, time.time()-start, copyveriDizini