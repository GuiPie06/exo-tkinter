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

        bigframe=tk.Frame(self, bg="#f0f0f0", borderwidth=1, relief="solid")
        bigframe.pack(side="top", fill="both", pady=15, padx= 5)

        nomemail = tk.Frame(bigframe, bg="#f0f0f0")
        nomemail.pack(side="left", fill="x", padx = 25, pady=20)
        labelnom = tk.Label(nomemail, text="Nom :", font=("Arial", 11))
        labelnom.pack(side="top", fill="x", pady = 5)
        labalemail = tk.Label(nomemail, text="Email :", font=("Arial", 11))
        labalemail.pack(side="bottom", fill="x", pady = 5)


        entrynomemail = tk.Frame(bigframe, bg="#f0f0f0")
        entrynomemail.pack(side="left", fill="x", ipadx = 125, pady=20)
        entrtynom = tk.Entry(entrynomemail)
        entrtynom.pack(side="top", fill="x", pady = 5)
        entryemail = tk.Entry(entrynomemail)
        entryemail.pack(side="top", fill="x", pady = 5)


        valider = tk.Frame(bigframe, bg="#f0f0f0")
        valider.pack(side="left", fill="x", padx = 25, pady=20)
        boutonvalider = tk.Button(valider, text="Valider", command="on_click", state="normal")
        boutonvalider.pack(side="top")




class Interface3(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pannedwindow")
        self.geometry("900x500")
        self.configure(background="#f0f0f0")

        listeelement = tk.Frame(self, bg="#eaf2ff", borderwidth=1, relief="groove")
        listeelement.pack(side="left", fill="x", padx = 10)

        label = tk.Frame(listeelement, bg="#eaf2ff")
        label.pack(side="top", fill="x", padx = 10, pady=3)
        labelliste= tk.Label(label, bg="#eaf2ff", text="Liste d'éléments", font=("Arial", 9, "bold"))
        labelliste.pack(side="left", fill="x")

        liste = tk.Frame(listeelement, bg="#eaf2ff")
        liste.pack(side="top", fill="x", padx=10, ipady=40)
        listefruit= tk.Listbox(liste, height=10, bg="#ffffff", selectmode="single", font=("Arial", 8, "bold"))
        listefruit.pack(side="top", fill="both", expand=True)
        for item in ("Pomme", "Poire", "Banane", "Ananas", "Mangue"): listefruit.insert("end", item)

        boutons = tk.Frame(listeelement, bg="#eaf2ff")
        boutons.pack(side="top", fill="x", pady = 5, padx = 10)
        boutonlire = tk.Button(boutons, text="Lire sélection", command="on_click", state="normal")
        boutonlire.pack(side="left", padx = 2)
        boutonsupprimer = tk.Button(boutons, text="Supprimer", command="on_click", state="normal")
        boutonsupprimer.pack(side="right", padx = 2)


class Interface4(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Form")
        self.geometry("400x400")
        self.configure(background="#f0f0f0")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frm_ppale = tk.Frame(self)
        frm_ppale.grid(row=0, column=0, sticky="nsew")
        frm_ppale.columnconfigure(1, weight=1)

        tk.Label(frm_ppale, text="Courriel").grid(row=0, column=0, sticky="e")
        email = tk.Entry(frm_ppale)
        email.grid(row=0, column=1, sticky="we")


        tk.Label(frm_ppale, text="Mot de passe").grid(row=1, column=0, sticky="e")
        pwd = tk.Entry(frm_ppale, show="*")
        pwd.grid(row=1, column=1, sticky="we")


        btn = tk.Button(frm_ppale, text="Valider", )
        btn.grid(row=0, column=2, rowspan=2, sticky="e")


if __name__ == "__main__":
    Interface1().mainloop()
    Interface2().mainloop()
    # Interface3().mainloop()
    Interface4().mainloop()