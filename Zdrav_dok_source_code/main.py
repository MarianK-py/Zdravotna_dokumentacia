from Text_finder import *
import tkinter as tk
from os.path import exists

class ErrorWindow(tk.Toplevel):
    def __init__(self, parent, errMessage):
        super().__init__(parent)

        self.geometry('300x120')
        self.title('Error Window')

        l = tk.Label(self, text=errMessage, font="arial 12", anchor="center")
        l.place(x=150, y=25, height=40, anchor="center")

        b = tk.Button(self, text='OK', anchor="center", command=self.destroy)
        b.place(x=150, y=75, width=100, height=40, anchor="center")

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("550x350")
        self.title("Main window")

        rad1y = 100
        rad2y = 160
        rad3y = 220
        rad4y = 300

        l0 = tk.Label(self, text="Spracovávanie dát COVID-19 pacientov", font="arial 18", anchor="center")
        l0.place(x=275, y=50, height=40, anchor="center")

        l1 = tk.Label(self, text="Čítaný súbor:", font="arial 14", anchor="center")
        l1.place(x=20, y=rad1y, height=40)

        self.e1 = tk.Entry(self, justify="center", font="arial 12")
        self.e1.place(x=220, y=rad1y, height=40, width=300)

        l2 = tk.Label(self, text="Zapisovaný súbor:", font="arial 14", anchor="center")
        l2.place(x=20, y=rad2y, height=40)

        self.e2 = tk.Entry(self, justify="center", font="arial 12")
        self.e2.place(x=220, y=rad2y, height=40, width=300)

        l31 = tk.Label(self, text="Číslo prvého hárku:", font="arial 12", anchor="center")
        l31.place(x=20, y=rad3y, height=40)

        self.e31 = tk.Entry(self, justify="center", font="arial 12")
        self.e31.place(x=170, y=rad3y, height=40, width=60)

        l32 = tk.Label(self, text="Číslo posledného hárku:", font="arial 12", anchor="center")
        l32.place(x=250, y=rad3y, height=40)

        self.e32 = tk.Entry(self, justify="center", font="arial 12")
        self.e32.place(x=430, y=rad3y, height=40, width=60)

        b1 = tk.Button(self, text="START", font="arial 12", anchor="center", command=self.skontroluj_hodnoty)
        b1.place(x=275, y=rad4y, width=100, height=40, anchor="center")




    def skontroluj_hodnoty(self):
        citany = self.e1.get()
        if (len(citany) == 0):
            window = ErrorWindow(self, "Chýba čítaný súbor")
            window.grab_set()
            print("Chýba čítaný súbor")
            return
        else:
            if (citany[-5:] != ".xlsx"):
                citany += ".xlsx"

        zapis = self.e2.get()
        if (len(zapis) == 0):
            window = ErrorWindow(self, "Chýba zapisovací súbor")
            window.grab_set()
            print("Chýba zapisovací súbor")
            return
        else:
            if (zapis[-5:] != ".xlsx"):
                zapis += ".xlsx"

        prvy = self.e31.get()
        if (prvy.isnumeric() == False):
            window = ErrorWindow(self, "Zlé číslo prvého hárku")
            window.grab_set()
            print("Zlé číslo prvého hárku")
            return
        else:
            prvy = int(prvy)

        posledny = self.e32.get()
        if (posledny.isnumeric() == False):
            window = ErrorWindow(self, "Zlé číslo posledneho hárku")
            window.grab_set()
            print("Zlé číslo posledneho hárku")
            return
        else:
            posledny = int(posledny)

        if (prvy > posledny):
            window = ErrorWindow(self, "Zlé čísla hárkov")
            window.grab_set()
            print("Zlé čísla hárkov")
            return

        if (exists(citany) == False):
            window = ErrorWindow(self, "Problém pri načítaní čítacieho súboru")
            window.grab_set()
            print("Problém pri načítaní čítacieho súboru")
            return

        if (exists(zapis) == False):
            window = ErrorWindow(self, "Problém pri načítaní zapisovacieho súboru")
            window.grab_set()
            print("Problém pri načítaní zapisovacieho súboru")
            return

        pridavanie_udajov(citany, zapis, prvy, posledny)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
