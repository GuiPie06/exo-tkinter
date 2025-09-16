import tkinter as tk

class Interface1(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestionnaire de tâches")
        self.geometry("500x650")
        self.configure(background="#f0f0f0")


        titre= tk.Frame(self)
        titre.pack(side="top", fill="x")
        self.label = tk.Label(titre,
                              text='Ma To-do List',
                              font=("Arial", 20, "bold"),
                              bg= "#f0f0f0",
                            )
        self.label.pack(side="top", fill="x", pady = 10)


        ajoutertache = tk.Frame(self, bg="#f0f0f0", relief="groove")
        ajoutertache.pack(side="top", fill="x")
        entry1 = tk.Entry(ajoutertache)
        entry1.pack(side="top", fill="x", padx= 150, pady=10)
        bouton1 = tk.Button(ajoutertache, text="Ajouter la tâche", command='on_click', state="normal")
        bouton1.pack(side="top")

        listetache = tk.Frame(self, bg="#f0f0f0")
        listetache.pack(side="top", fill="x")
        entry2 = tk.Entry(listetache)
        entry2.pack(side="top", fill="both", padx = 120, pady=20, ipady=90, ipadx=12)


        tacheprio= tk.Frame(self, bg="#f0f0f0")
        tacheprio.pack(side="top", fill="x")
        v_news = tk.BooleanVar(value=True)
        case1 = tk.Checkbutton(tacheprio, text="Toutes les tâches sont prioritaires", variable=v_news)
        case1.pack(side="top", pady= 10)


        typetache = tk.Frame(self, bg="#f0f0f0")
        typetache.pack(side="top", pady=10)
        civ = tk.StringVar(value="M")
        tk.Radiobutton(typetache, text="Personnel", variable=civ, value="Personnel").pack(anchor="w")
        tk.Radiobutton(typetache, text="Professionnel", variable=civ, value="Professionnel").pack(anchor="w")

        notetache = tk.Frame(self, bg="#f0f0f0")
        notetache.pack(side="top", fill="x", pady=10)
        titre2 = tk.Label(notetache, text="Notes sur la tâche sélectionnée:", bg="#f0f0f0")
        titre2.pack(side="top", fill="x")
        entry3 = tk.Entry(notetache)
        entry3.pack(side="top", fill="both", pady=20, padx= 50, ipady=90)




class Interface2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formulaire")
        self.geometry("600x150")
        self.configure(background="#f0f0f0")







if __name__ == "__main__":
    Interface1().mainloop()
    Interface2().mainloop()