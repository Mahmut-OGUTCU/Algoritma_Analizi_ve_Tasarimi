import AramaSiralamaAlgoritmalari
from tkinter import *

pencere = Tk()
pencere.title("Arama ve Siralama Algoritmalari")
pencere.geometry("350x300")

def SearchorSort():
    searchButton = Button(pencere, text = "Arama Algoritmaları", width = 17, height = 3, command = AramaSiralamaAlgoritmalari.searchButtonAdd)
    searchButton.grid(padx = 115, pady = 50)
    sortButton = Button(pencere, text = "Sıralama Algoritmaları", width = 17, height = 3, command = AramaSiralamaAlgoritmalari.sortButtonAdd)
    sortButton.grid(padx = 115, pady = 2)

def main():
    SearchorSort()
    pencere.mainloop()

main()