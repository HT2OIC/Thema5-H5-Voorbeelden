# Knop toevoegen
# -------------------------------------------------------
import tkinter as tk

# Venster aanmaken
venster = tk.Tk()
venster.title("Europese landen")

# Labels aanmaken
label_land = tk.Label(text = "Land:")
label_hoofdstad = tk.Label(text = "Hoofdstad:")
label_inwoners = tk.Label(text = "Aantal inwoners:")
label_levensverwachting = tk.Label(text = "Gemiddelde levensverwachting:")

# Knop aanmaken
knop_data = tk.Button(text = "Vraag data op", width = 20)

# Labels in venster plaatsen
label_land.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
label_hoofdstad.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)
label_inwoners.grid(row = 2, column = 0, sticky = "w", padx = 5, pady = 5)
label_levensverwachting.grid(row = 3, column = 0, sticky = "w", padx = 5, pady = 5)

# Knop in venster plaatsen
knop_data.grid(row = 4, column = 0, padx = 5, pady = 5)

# Programma uitvoeren
venster.mainloop()