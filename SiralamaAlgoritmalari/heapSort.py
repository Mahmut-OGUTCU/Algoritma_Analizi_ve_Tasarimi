import numpy as np
import time

def heapiyf(veriDizini, n, i, islemSayisi):
    enBuyuk = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and veriDizini[i] < veriDizini[l]:
        islemSayisi += 1
        enBuyuk = l
    
    if r < n and veriDizini[enBuyuk] < veriDizini[r]:
        islemSayisi += 1
        enBuyuk = r
        
    if enBuyuk != i:
        islemSayisi += 1
        veriDizini[i], veriDizini[enBuyuk] = veriDizini[enBuyuk], veriDizini[i]
        heapiyf(veriDizini, n, enBuyuk, islemSayisi)

def heapSort(veriMiktari):
    veriDizini = np.random.randint(0, 100000, veriMiktari)
    copyveriDizini = veriDizini.copy()
    
    start = time.time()
    islemSayisi = 0

    n = len(veriDizini)

    for i in range(n//2, -1, -1):
        heapiyf(veriDizini, n, i, islemSayisi)
        
    for i in range(n-1, 0, -1):
        islemSayisi += 1
        veriDizini[i], veriDizini[0] = veriDizini[0], veriDizini[i]
        
        heapiyf(veriDizini, i, 0, islemSayisi)
    
    return veriDizini, islemSayisi, time.time()-start, copyveriDizini