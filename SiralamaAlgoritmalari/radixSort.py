import numpy as np
import time

def countingSort(veriDizini, say, islemSayisi):
    
    n = len(veriDizini)
    
    output = [0] * (n)
    
    count = [0] * 10
    
    for i in range(0, n):
        islemSayisi += 2
        index = (veriDizini[i] / say)
        count[int((index) % 10)] += 1

    for i in range(1, 10):
        islemSayisi += 1
        count[i] += count[i - 1]
        
    i = n - 1
    while i>=0:
        islemSayisi += 4
        index = (veriDizini[i] / say)
        output[count[int((index) % 10)] - 1] = veriDizini[i]
        count[int((index) % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(veriDizini)): 
        islemSayisi += 1
        veriDizini[i] = output[i]
 

def radixSort(veriMiktari):
    veriDizini = np.random.randint(0, 100000, veriMiktari)
    copyveriDizini = veriDizini.copy()
    
    start = time.time()
    islemSayisi = 0
    
    maks = max(veriDizini)

    say = 1
    while maks / say > 0:
        islemSayisi += 2
        countingSort(veriDizini, say, islemSayisi)
        say *= 10
        
    return veriDizini, islemSayisi, time.time()-start, copyveriDizini