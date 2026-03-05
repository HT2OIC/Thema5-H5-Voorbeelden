from twee_een_datalaag import Datalaag
from twee_twee_domeinlogica import Domeinlogica
import tkinter as tk

class Presentatielaag:
    def __init__(self, domeinlogica):
        self.domeinlogica = domeinlogica
        # Lege lijst met labels, zodat de labels dynamisch verwijderd kunnen worden.
        self.stad_labels = []

    def toon_foutmelding(self, bericht, kleur = "red"):
        self.fout_label.config (text = bericht, fg = kleur)
    
    def ophalen_steden(self):
        code = self.landcode.get()
        # Labels verwijderen voordat nieuwe worden gemaakt.
        self.verwijderen_labels()
        # Foutmelding leegmaken.
        self.toon_foutmelding("")
        
        # Lijst met steden van een land ophalen.
        resultaat = self.domeinlogica.ophalen_steden(code)
        
        # Nakijken of er een foutmelding was.
        if isinstance(resultaat, str) and "fout" in resultaat.lower():
            self.fout_label.config(text = resultaat, fg="red")
            return
        try:
            steden, gemiddelde = resultaat # Tuple opsplitsen in steden en gemiddelde.
            
            # Als er geen steden gevonden zijn, een foutmelding tonen.
            if not steden:
                self.toon_foutmelding("Geen steden gevonden voor deze landcode.")
                return
            # Alle steden tonen.
            rij = 0  # Start rij voor resultaten
            kolom = 3
            for stad in steden:
                label = tk.Label(text = stad)
                label.grid(row = rij, column = kolom, sticky = "w", padx = 5, pady = 2)
                self.stad_labels.append(label) # Labels toevoegen aan de lijst.
                if rij == 10:
                    rij = 0
                    kolom += 1
                else:
                    rij += 1
            # Gemiddelde populatie tonen
            gemiddelde_label = tk.Label(text = f"Gemiddelde populatie: {gemiddelde}")
            gemiddelde_label.grid(row = rij, column = kolom, sticky = "w", padx = 5, pady = 5)
            self.stad_labels.append(gemiddelde_label)
        except Exception as e:
            self.toon_foutmelding(f"Onverwachte fout: {e}")

    # Labels verwijderen.
    def verwijderen_labels(self):
        for label in self.stad_labels:
            label.destroy()
        self.stad_labels.clear()

    # GUI aanmaken.
    def GUI(self):
        venster = tk.Tk()
        venster.title("Stedenbeheer")
        # Steden oplijsten.
        tk.Label(text = "Van welk land wil je de steden oplijsten?", font = 14).grid(row = 0, sticky = "w")
        tk.Label(text = "Landcode:").grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)
        self.landcode = tk.Entry()
        self.landcode.grid(row = 1, column = 1, padx = 5, pady = 5)
        tk.Button(text = "Ophalen steden", command = self.ophalen_steden).grid(row = 1, column = 2, padx = 5, pady = 5)
        
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
