# Een invoerveld toevoegen
# -------------------------------------------------------
import tkinter as tk

# Gegevens in dictionary
gegevens = {
    "België": {"hoofdstad": "Brussel", "inwoners": 11820000, "levensverwachting": 82.3},
    "Frankrijk": {"hoofdstad": "Parijs", "inwoners": 67390000, "levensverwachting": 82.5},
    "Duitsland": {"hoofdstad": "Berlijn", "inwoners": 83190000, "levensverwachting": 81.2}
}

# Functie om dictionary uit te lezen
def lees_data(land, waarde):
    land_gegevens = gegevens[land]
    return land_gegevens[waarde]

# Functie om labels aan te passen
def schrijf_data():
    land = invoer.get()
    if land in gegevens:
        label_land["text"] = f"land: {land}"
        label_hoofdstad["text"] = f"Hoofdstad: {lees_data(land, 'hoofdstad')}"
        label_inwoners["text"] = f"Aantal inwoners: {lees_data(land,'inwoners')}"
        label_levensverwachting["text"] = f"Levensverwachting: {lees_data(land,'levensverwachting')}"
    else:
        label_land["text"] = "Land: onbekend"
        label_hoofdstad["text"] = "Hoofdstad: onbekend"
        label_inwoners["text"] = "Aantal inwoners: onbekend"
        label_levensverwachting["text"] = "Levensverwachting: onbekend"

# Venster aanmaken
venster = tk.Tk()
venster.title("Europese landen")

# Invoer aanmaken
invoer = tk.Entry()
invoer.grid(row=0, column = 1, padx = 5, pady = 5)

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