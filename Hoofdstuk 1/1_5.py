# Functie toewijzen aan knop
# -------------------------------------------------------
import tkinter as tk

# Gegevens in dictionary
gegevens = {"hoofdstad": "Brussel", "inwoners": 11820000, "levensverwachting": 82.3}

# Functie om dictionary uit te lezen
def lees_data(waarde):
    return gegevens[waarde]

# Functie om labels aan te passen
def schrijf_data():
    label_land["text"] = "Land: België"
    label_hoofdstad["text"] = f"Hoofdstad: {lees_data('hoofdstad')}"
    label_inwoners["text"] = f"Aantal inwoners: {lees_data('inwoners')}"
    label_levensverwachting["text"] = f"Gemiddelde levensverwachting: {lees_data('levensverwachting')}"

# Venster aanmaken
venster = tk.Tk()
venster.title("Europese landen")

# Labels aanmaken
label_land = tk.Label(text = "Land:")
label_hoofdstad = tk.Label(text = "Hoofdstad:")
label_inwoners = tk.Label(text = "Aantal inwoners:")
label_levensverwachting = tk.Label(text = "Gemiddelde levensverwachting:")

# Knop aanmaken met functie
knop_data = tk.Button(text = "Vraag data op", width = 20, command = schrijf_data)

# Labels in venster plaatsen
label_land.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
label_hoofdstad.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)
label_inwoners.grid(row = 2, column = 0, sticky = "w", padx = 5, pady = 5)
label_levensverwachting.grid(row = 3, column = 0, sticky = "w", padx = 5, pady = 5)

# Knop in venster plaatsen
knop_data.grid(row = 4, column = 0, padx = 5, pady = 5)

# Programma uitvoeren
venster.mainloop()