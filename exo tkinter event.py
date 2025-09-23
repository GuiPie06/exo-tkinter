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





class Interface2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x400")
        self.configure(background="#f0f0f0")


        fenetrelecture = tk.Frame(self, borderwidth=5, relief="groove")
        fenetrelecture.pack(side="top", fill="x", pady = 5 , padx = 10)
        entrylecture = tk.Entry(fenetrelecture, font=("Arial", 12, "bold"))
        entrylecture.pack(side="top", fill="x", pady = 10, padx = 10, ipady = 15 )

        range1= tk.Frame(self, borderwidth=2, relief="groove")
        range1.pack(side="top", fill="x")
        boutonC = tk.Button(range1, text="C", ) #command=self.******
        boutonC.pack(side="left", fill="x")
        boutonslash = tk.Button(range1, text="/", )  #command=self.******
        boutonslash.pack(side="left", fill="x")
        boutonasterix = tk.Button(range1, text="*", ) #command=self.******
        boutonasterix.pack(side="left", fill="x")







if __name__ == "__main__":
    # Interface1().mainloop()
    Interface2().mainloop()