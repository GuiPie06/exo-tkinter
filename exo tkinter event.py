import tkinter as tk
from tkinter import messagebox


class Interface1(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interface Simple")
        self.geometry("400x400")
        self.configure(background="#f0f0f0")

        nb1 = tk.Frame(self)
        nb1.pack(side="top", fill="x", pady= 20)
        label1 = tk.Label(nb1, text="Nombre 1 :")
        label1.pack(side="top", fill="x")
        self.entry1 = tk.Entry(nb1)
        self.entry1.pack(side="top", ipadx = 10)

        nb2 = tk.Frame(self)
        nb2.pack(side="top", fill="x", pady = 20)
        label2 = tk.Label(nb2, text="Nombre 2 :")
        label2.pack(side="top", fill="x")
        self.entry2 = tk.Entry(nb2)
        self.entry2.pack(side="top", ipadx=10)

        bouton = tk.Button(self, text="Calculer", command=self.affichersomme)
        bouton.pack(side="top", ipadx = 10, pady = 10)

    def calculer(self):
        return float(self.entry1.get()) + float(self.entry2.get())

    def affichersomme(self):
        messagebox.showinfo("Résultat", f"la somme est : {self.calculer()}")


if __name__ == "__main__":
    Interface1().mainloop()