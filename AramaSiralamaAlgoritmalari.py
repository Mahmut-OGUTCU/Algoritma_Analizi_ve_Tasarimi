import AramaSiralamaParametre
from tkinter import *

def searchButtonAdd():
    newWindow = Toplevel()
    newWindow.title("Arama Algoritmaları")
    newWindow.geometry("300x300")
    
    binarySearchButton = Button(newWindow, text = "Binary Search", width = 15, height = 3, 
                                command = lambda: AramaSiralamaParametre.searchNewWindow(str("binarysearch")))
    binarySearchButton.grid(padx = 90, pady = 50)
    linearSearchButton = Button(newWindow, text = "Linear Search", width = 15, height = 3, 
                                command = lambda: AramaSiralamaParametre.searchNewWindow(str("linearsearch")))
    linearSearchButton.grid(padx = 90, pady = 2)

def sortButtonAdd():
    newWindow = Toplevel()
    newWindow.title("Sıralama Algoritmaları")
    newWindow.geometry("450x350")
    
    bucketSortButton = Button(newWindow, text = "Bucket Sort", width = 15, height = 3, 
                              command = lambda: AramaSiralamaParametre.sortNewWindow(str("bucketsort")))
    bucketSortButton.grid(row = 1, column = 0, padx = 20, pady = 20)
    
    countingSortButton = Button(newWindow, text = "Counting Sort", width = 15, height = 3, 
                                command = lambda: AramaSiralamaParametre.sortNewWindow(str("countingsort")))
    countingSortButton.grid(row = 1, column = 1, padx = 2, pady = 2)
   
    heapSortButton = Button(newWindow, text = "Heap Sort", width = 15, height = 3, 
                            command = lambda: AramaSiralamaParametre.sortNewWindow(str("heapsort")))
    heapSortButton.grid(row = 1, column = 2, padx = 20, pady = 2)    
   
    insertionSortButton = Button(newWindow, text = "Insertion Sort", width = 15, height = 3, 
                                  command = lambda: AramaSiralamaParametre.sortNewWindow(str("insertionsort")))
    insertionSortButton.grid(row = 2, column = 0, padx = 2, pady = 20)
    
    mergeSortButton = Button(newWindow, text = "Merge Sort", width = 15, height = 3, 
                              command = lambda: AramaSiralamaParametre.sortNewWindow(str("mergesort")))
    mergeSortButton.grid(row = 2, column = 1, padx = 2, pady = 2)
    
    quickSortButton = Button(newWindow, text = "Quick Sort", width = 15, height = 3, 
                              command = lambda: AramaSiralamaParametre.sortNewWindow(str("quicksort")))
    quickSortButton.grid(row = 2, column = 2, padx = 2, pady = 2)
    
    radixSortButton = Button(newWindow, text = "Radix Sort", width = 15, height = 3, 
                              command = lambda: AramaSiralamaParametre.sortNewWindow(str("radixsort")))
    radixSortButton.grid(row = 3, column = 1, padx = 2, pady = 20)