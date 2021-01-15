### Arama modülleri
from AramaAlgoritmalari import binarySearch
from AramaAlgoritmalari import linearSearch

### Sıralama modülleri
from SiralamaAlgoritmalari import bucketSort
from SiralamaAlgoritmalari import countingSort
from SiralamaAlgoritmalari import heapSort
from SiralamaAlgoritmalari import insertionSort
from SiralamaAlgoritmalari import mergeSort
from SiralamaAlgoritmalari import quickSort
from SiralamaAlgoritmalari import radixSort

from tkinter import messagebox

def doSearch(aramaTipi, arananSayi, veriMiktari):            
    
    if aramaTipi == "binarysearch":
        SearchFound(binarySearch.binarySearch(arananSayi, veriMiktari))
    elif aramaTipi == "linearsearch":
        SearchFound(linearSearch.linearSearch(arananSayi, veriMiktari))

def doSort(siralamaTipi, veriMiktari):
    
    if siralamaTipi == "bucketsort":
        isSort(bucketSort.bucketSort(veriMiktari), siralamaTipi)
    elif siralamaTipi == "countingsort":
        isSort(countingSort.countingSort(veriMiktari), siralamaTipi)
    elif siralamaTipi == "heapsort":
        isSort(heapSort.heapSort(veriMiktari))
    elif siralamaTipi == "insertionsort":
        isSort(insertionSort.insertionSort(veriMiktari), siralamaTipi)
    elif siralamaTipi == "mergesort":
        isSort(mergeSort.mergeSort(veriMiktari), siralamaTipi)
    elif siralamaTipi == "quicksort":
        isSort(quickSort.quickSort(veriMiktari), siralamaTipi)
    elif siralamaTipi == "radixsort":
        isSort(radixSort.radixSort(veriMiktari), siralamaTipi)

def SearchFound(data):
    if data[0] == "found":
        messagebox.showinfo("Arama Sonuçları", "Aranan sayı BULUNDU\nbulunan index "+str(data[1]))
        
    else:
        messagebox.showinfo("Arama Sonuçları", "Aranan sayı BULUNAMADI")
    
    messagebox.showinfo("Arama Sonuçları", "yapılan islem sayısı "+str(data[2])+"\ngeçen süre "+str(data[3]))
    
    if len(data[4]) <= 1000:
        messagebox.showinfo("Arama Sonuçları", message = str(data[4]))
    
    else:
        messagebox.showerror("Arama Sonuçları", message = "1.000'den fazla değer yazdırılamıyor\n"+str(data[4]))
    
    messagebox.showinfo("Arama Sonuçları", "0 - 100000 arasında"+len(data[0])+"tane random sayı oluşturulup .sort() methodu ile sıralandıktan sonra arama yapmılmıştır.")

def isSort(data, siralamaTipi):
    if len(data[0]) <= 1000:
        messagebox.showinfo("Sıralama Sonuçları", message = "Sıralanmış veri dizisi\n"+str(data[0]))
    
    else:
        messagebox.showerror("Sıralama Sonuçları", message = "1.000'den fazla değer yazdırılamıyor\nSıralanmış veri dizisi\n"+str(data[0]))
    
    messagebox.showinfo("Arama Sonuçları", "yapılan islem sayısı "+str(data[1])+"\ngeçen süre "+str(data[2]))
    
    messagebox.showinfo("Sıralama Sonuçları", message = "Sıralanmamış veri dizisi\n"+str(data[3]))
    
    if siralamaTipi != "bucketsort":    
        messagebox.showinfo("Sıralama Sonuçları", "0 - 100000 arasında"+len(data[0])+"tane random sayı oluşturulmuştur.")
    else:
        messagebox.showinfo("Sıralama Sonuçları", "0 - 1 arasında"+len(data[0])+"tane random sayı oluşturulmuştur.")