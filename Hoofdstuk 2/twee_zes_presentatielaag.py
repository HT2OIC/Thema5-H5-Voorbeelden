from twee_vier_datalaag import Datalaag
from twee_vijf_domeinlogica import Domeinlogica
import tkinter as tk

class Presentatielaag:
    def __init__(self, domeinlogica):
        self.domeinlogica = domeinlogica

    def toon_foutmelding(self, bericht, kleur = "red"):
        self.fout_label.config (text = bericht, fg = kleur)

    def nieuwe_stad(self):
        # Waardes inlezen.
        naam = self.naam.get()
        code = self.code.get()
        district = self.district.get()
        populatie = self.populatie.get()
        
        # Foutmelding leegmaken.
        self.toon_foutmelding("")
        try:
            # Nakijken of de populatie een getal is.
            populatie = int(populatie) if populatie else 0
        except ValueError:
            self.toon_foutmelding("De populatie moet een geheel getal zijn.")
            return
        
        # Data opslaan in db.
        resultaat = self.domeinlogica.opslaan_stad(naam, code, district, populatie)
        # Nakijken of resultaat een foutmelding is.
        kleur = "red" if "fout" in resultaat.lower() else "green"
        self.toon_foutmelding(resultaat, kleur)

    
    # GUI aanmaken.
    def GUI(self):
        venster = tk.Tk()
        venster.title("Stedenbeheer")

        # Stad toevoegen.
        tk.Label(text = "Voeg een nieuwe stad toe.", font = 14).grid(row = 2, sticky = "w")
        tk.Label(text = "Naam stad*:").grid(row = 3, column = 0, sticky = "w", padx = 5, pady = 5)
        self.naam = tk.Entry()
        self.naam.grid(row = 3, column = 1)
        tk.Label(text = "Landcode*:").grid(row = 4, column = 0, sticky = "w", padx = 5, pady = 5)
        self.code = tk.Entry()
        self.code.grid(row = 4, column = 1)
        tk.Label(text = "Provincie:").grid(row = 5, column = 0, sticky = "w", padx = 5, pady = 5)
        self.district = tk.Entry()
        self.district.grid(row = 5, column = 1)
        tk.Label(text = "Populatie:").grid(row = 6, column = 0, sticky = "w", padx = 5, pady = 5)
        self.populatie = tk.Entry()
        self.populatie.grid(row = 6, column = 1)   
        tk.Button(text = "Toevoegen stad", command = self.nieuwe_stad).grid(row = 6, column = 2, padx = 5, pady = 5)
        
        # Label voor foutmeldingen.
        self.fout_label = tk.Label(text = "", fg="red")
        self.fout_label.grid(row = 7, column = 0, columnspan = 4, sticky = "w", padx = 5, pady = 5)
        venster.mainloop()

# Lagen initialiseren
if __name__ == "__main__":
    datalaag = Datalaag()
    domeinlogica = Domeinlogica(datalaag)
    Presentatie_laag = Presentatielaag(domeinlogica)
    Presentatie_laag.GUI() 
