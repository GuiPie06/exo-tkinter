from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

class ExoTtkTableau(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formulaire")
        self.geometry("800x500")
        self.configure(background="#f0f0f0")

        self.init_Widgets()


    def init_Widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)



        header_content = tk.Frame(self)
        header_content.grid(row=0, column=0, sticky="ew")
        header_content.columnconfigure(0, weight=1)
        header_content.columnconfigure(1, weight=1)
        header_content.columnconfigure(2, weight=1)

        #labels
        self.lbl_nom = tk.Label(header_content, text="Nom")
        self.lbl_nom.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        self.lbl_email = tk.Label(header_content, text="Email")
        self.lbl_email.grid(row=0, column=1, sticky="w", padx=20, pady=5)
        self.lbl_age = tk.Label(header_content, text="Âge")
        self.lbl_age.grid(row=0, column=2, sticky="w", padx=20, pady=5)

        #inputs
        self.entry_nom = tk.Entry(header_content)
        self.entry_nom.grid(row=1, column=0, sticky="ew", padx=(20,5), pady=5)
        self.entry_email = tk.Entry(header_content)
        self.entry_email.grid(row=1, column=1, sticky="ew", padx=20, pady=5)
        self.entry_age = tk.Entry(header_content)
        self.entry_age.grid(row=1, column=2, sticky="ew", padx=20, pady=5)

        #boutons
        self.btn_ajouter = tk.Button(header_content, text="Ajouter")
        self.btn_ajouter.grid(row=1, column=3, sticky="e", padx=5, pady=5)
        self.btn_supprimer = tk.Button(header_content, text="Supprimer sélection")
        self.btn_supprimer.grid(row=1, column=4, sticky="e", padx=5, pady=5)



        main_content = tk.Frame(self)
        main_content.grid(row=1, column=0, sticky="snew")
        main_content.columnconfigure(0, weight=1)
        main_content.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(main_content, columns=("nom", "email", "age"), show="headings")
        self.tree.heading("nom", text="Nom")
        self.tree.heading("email", text="Email")
        self.tree.heading("age", text="Âge")

        self.tree.column("nom", width=200)
        self.tree.column("email", width=400)
        self.tree.column("age", width=80)

        self.tree.grid(column=0, row=0, sticky="nsew", padx=15, pady=15)



        footer_content = tk.Frame(self)
        footer_content.grid(row=2, column=0, sticky="snew")
        footer_content.columnconfigure(1, weight=1)
        footer_content.columnconfigure(2, weight=1)

        self.btn_importerjson = tk.Button(footer_content, text="Importer JSON")
        self.btn_importerjson.grid(row=0, column=0, sticky="w", padx=(20,5), pady=5)
        self.btn_importercsv = tk.Button(footer_content, text="Importer CSV")
        self.btn_importercsv.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.btn_exporterjson = tk.Button(footer_content, text="Exporter JSON")
        self.btn_exporterjson.grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.btn_exportercsv = tk.Button(footer_content, text="Exporter CSV")
        self.btn_exportercsv.grid(row=0, column=3, sticky="e", padx=(5,20), pady=5)



if __name__ == '__main__':
    ExoTtkTableau().mainloop()