import tkinter as tk
from tkinter import messagebox


class Interface2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x400")
        self.configure(background="#f0f0f0")


        fenetrelecture = tk.Frame(self, borderwidth=5, relief="groove")
        fenetrelecture.pack(side="top", fill="x", pady = 5 , padx = 10)
        self.entrylecture = tk.Entry(fenetrelecture, font=("Arial", 12, "bold"))
        self.entrylecture.pack(side="top", fill="x", pady = 10, padx = 10, ipady = 15 )

        operateurs = tk.Frame(self, relief="groove")
        operateurs.pack(side="top", fill="both", expand=True)

        range1= tk.Frame(operateurs, borderwidth=2, relief="groove")
        range1.pack(side="top", fill="both", expand=True)
        boutonc = tk.Button(range1, text="C", command=self.operateurC)
        boutonc.pack(side="left", fill="both", expand=True)
        boutonslash = tk.Button(range1, text="/", command=lambda: self.ecrire("/"))  #https://stackoverflow.com/questions/70406400/understanding-python-lambda-behavior-with-tkinter-button
        boutonslash.pack(side="left", fill="both", expand=True)
        boutonasterix = tk.Button(range1, text="*", command=lambda: self.ecrire("*") )
        boutonasterix.pack(side="left", fill="both", expand=True)

        range2= tk.Frame(operateurs, borderwidth=2, relief="groove")
        range2.pack(side="top", fill="both", expand=True, )
        bouton7 = tk.Button(range2, text="7",command=lambda: self.ecrire("7") )
        bouton7.pack(side="left", fill="both", expand=True)
        bouton8 = tk.Button(range2, text="8", command=lambda: self.ecrire("8"))
        bouton8.pack(side="left", fill="both", expand=True)
        bouton9 = tk.Button(range2, text="9", command=lambda: self.ecrire("9"))
        bouton9.pack(side="left", fill="both", expand=True)
        boutonmoins = tk.Button(range2, text="-", command=lambda: self.ecrire("-"))
        boutonmoins.pack(side="left", fill="both", expand=True)

        range3= tk.Frame(operateurs, borderwidth=2, relief="groove")
        range3.pack(side="top", fill="both", expand=True)
        bouton4 = tk.Button(range3, text="4", command=lambda: self.ecrire("4"))
        bouton4.pack(side="left", fill="both", expand=True)
        bouton5 = tk.Button(range3, text="5", command=lambda: self.ecrire("5"))
        bouton5.pack(side="left", fill="both", expand=True)
        bouton6 = tk.Button(range3, text="6", command=lambda: self.ecrire("6"))
        bouton6.pack(side="left", fill="both", expand=True)
        boutonplus = tk.Button(range3, text="+", command=lambda: self.ecrire("+"))
        boutonplus.pack(side="left", fill="both", expand=True)

        range4= tk.Frame(operateurs, borderwidth=2, relief="groove")
        range4.pack(side="top", fill="both", expand=True)
        bouton1 = tk.Button(range4, text="1", command=lambda: self.ecrire("1"))
        bouton1.pack(side="left", fill="both", expand=True)
        bouton2 = tk.Button(range4, text="2", command=lambda: self.ecrire("2"))
        bouton2.pack(side="left", fill="both", expand=True)
        bouton3 = tk.Button(range4, text="3", command=lambda: self.ecrire("3"))
        bouton3.pack(side="left", fill="both", expand=True)
        boutonegal = tk.Button(range4, text="=", command=self.calculer)  # command=self.****** calculer
        boutonegal.pack(side="left", fill="both", expand=True)

        range5 = tk.Frame(operateurs, borderwidth=2, relief="groove")
        range5.pack(side="top", fill="both", expand=True)
        bouton0 = tk.Button(range5, text="0", command=lambda: self.ecrire("0"))
        bouton0.pack(side="left", fill="both", expand=True)
        boutonpoint = tk.Button(range5, text=".", command=lambda: self.ecrire("."))
        boutonpoint.pack(side="left", fill="both", expand=True)



    def operateurC(self) -> None:
        self.entrylecture.delete(0, tk.END)

    def ecrire(self, text)  :
        self.entrylecture.insert("end", text)

    def calculer(self):
        try:
            ligne = self.entrylecture.get()
            resultat = eval(ligne) #https://stackoverflow.com/questions/32642178/what-is-the-tkinter-eval-function
            self.entrylecture.delete(0, "end")
            self.entrylecture.insert("end", str(resultat))
        except:
            self.entrylecture.delete(0, "end")
            self.entrylecture.insert("end", "ERREUR")

if __name__ == "__main__":
    Interface2().mainloop()