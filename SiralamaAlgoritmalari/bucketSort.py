import numpy as np
import time



def bucketSort(veriMiktari):
    veriDizini = np.random.random(veriMiktari)
    copyveriDizini = veriDizini.copy()
    start = time.time()
    
    islemSayisi = 0
    dizi = []
    
    slotNo = 10
    
    for i in range(slotNo):
        islemSayisi += 1
        dizi.append([])
        
    for j in veriDizini:
        islemSayisi += 2
        indexB = int(slotNo * j)
        dizi[indexB].append(j)
        
    for i in range(slotNo):
        islemSayisi += 2
        dizi[i], islemSayisi =  insertionSort(dizi[i], islemSayisi)
        
    k = 0
    for i in range(slotNo):
        for j in range(len(dizi[i])):
            islemSayisi += 2
            veriDizini[k] = dizi[i][j]
            k += 1
            
    return veriDizini, islemSayisi, time.time()-start, copyveriDizini
    

def insertionSort(dizi, islemSayisi):
    for i in range(1, len(dizi)):
        islemSayisi += 3
        yukari = dizi[i]
        j = i - 1
        
        while j >= 0 and dizi[j] > yukari:
            islemSayisi += 2
            dizi[j + 1] = dizi[j]
            j -= 1
        
        dizi[j + 1] = yukari
        
    return dizi, islemSayisi