import AramaSiralamaSonuc
from tkinter import *

def searchNewWindow(aramaTipi = ""):
    newWindow = Toplevel()
    newWindow.title("Arama Parametreleri")
    newWindow.geometry("300x300")
    
    Label(newWindow, text = "Aranan Sayı").grid(row = 0, sticky = W)
    keyTextbox = Entry(newWindow)
    keyTextbox.grid(row = 0, column = 1, sticky = E)
    
    Label(newWindow, text = "Sayı Adedi").grid(row = 1, sticky = W)
    miktarTextbox = Entry(newWindow)
    miktarTextbox.grid(row = 1, column = 1, sticky = E)
    
    aramayiBaslatButton = Button(newWindow, text = "Aramayı Başlat",
                                  command = lambda: AramaSiralamaSonuc.doSearch(aramaTipi, int(keyTextbox.get()), int(miktarTextbox.get())))
    aramayiBaslatButton.grid(row = 2, column = 1, sticky = E)
    
def sortNewWindow(aramaTipi = ""):
    newWindow = Toplevel()
    newWindow.title("Arama Parametreleri")
    newWindow.geometry("300x300")
    
    Label(newWindow, text = "Sayı Adedi").grid(row = 0, sticky = W)
    miktarTextbox = Entry(newWindow)
    miktarTextbox.grid(row = 0, column = 1, sticky = E)
    
    aramayiBaslatButton = Button(newWindow, text = "Aramayı Başlat",
                                  command = lambda: AramaSiralamaSonuc.doSort(aramaTipi, int(miktarTextbox.get())))
    aramayiBaslatButton.grid(row = 3, column = 1, sticky = E)