import numpy as np
import time

def MERGE(veriDizini, ilk, orta, son, islemSayisi):

    n1 = orta - ilk + 1
    n2 = son - orta
   
    L = [0] * (n1)
    R = [0] * (n2)
   
    for i in range(0 , n1):
        islemSayisi += 1
        L[i] = veriDizini[ilk + i]
 
    for j in range(0 , n2):
        islemSayisi += 1
        R[j] = veriDizini[orta + 1 + j]
   
    i = 0
    j = 0
    k = ilk
 
    while i < n1 and j < n2 :
        islemSayisi += 1
        if L[i] <= R[j]:
            islemSayisi += 1
            veriDizini[k] = L[i]
            i += 1
        else:
            islemSayisi += 1
            veriDizini[k] = R[j]
            j += 1
        k += 1
   
    while i < n1:
        islemSayisi += 1
        veriDizini[k] = L[i]
        i += 1
        k += 1
   
    while j < n2:
        islemSayisi += 1
        veriDizini[k] = R[j]
        j += 1
        k += 1

def MERGE_SORT(veriDizini, ilk, son, islemSayisi):
    if ilk < son:
        islemSayisi += 2
        orta = (ilk + (son - 1)) // 2
        
        MERGE_SORT(veriDizini, ilk, orta, islemSayisi)
        MERGE_SORT(veriDizini, orta + 1, son, islemSayisi)
        MERGE(veriDizini, ilk, orta, son, islemSayisi)

def mergeSort(veriMiktari):
    veriDizini = np.random.randint(0, 100000, veriMiktari)
    copyveriDizini = veriDizini.copy()
    
    start = time.time()
    islemSayisi = 0
    MERGE_SORT(veriDizini, 0, len(veriDizini) - 1, islemSayisi)
    return veriDizini, islemSayisi, time.time()-start, copyveriDizini