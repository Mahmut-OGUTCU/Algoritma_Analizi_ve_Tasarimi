import numpy as np
import time


def partition(veriDizini, ilk, son, islemSayisi):
    i = ilk - 1
    pivot = veriDizini[son]
    
    for j in range(ilk, son):
        islemSayisi +=1
        if veriDizini[j] <= pivot:
            islemSayisi +=2
            i += 1
            veriDizini[i], veriDizini[j] = veriDizini[j], veriDizini[i]
        
    veriDizini[i+1], veriDizini[son] = veriDizini[son], veriDizini[i+1]
    return i+1, islemSayisi

            
def QUİCK_SORT(veriDizini, ilk, son, islemSayisi):
    if ilk < son:
        islemSayisi += 2
        pivot, islemSayisi = partition(veriDizini, ilk, son, islemSayisi)
        QUİCK_SORT(veriDizini, ilk, pivot-1, islemSayisi)
        QUİCK_SORT(veriDizini, pivot+1, son, islemSayisi)
        
def quickSort(veriMiktari):
    veriDizini = np.random.randint(0, 100000, veriMiktari)
    copyveriDizini = veriDizini.copy()
    
    start = time.time()
    islemSayisi = 0
    
    QUİCK_SORT(veriDizini, 0, len(veriDizini) - 1, islemSayisi)
    
    return veriDizini, islemSayisi, time.time()-start, copyveriDizini