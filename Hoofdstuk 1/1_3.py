# Tekstlabels uitlijnen
# -------------------------------------------------------
import tkinter as tk

# Venster aanmaken
venster = tk.Tk()
venster.title("Europese landen")

# Labels aanmaken met uitlijning
tk.Label(text="Land:").grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
tk.Label(text="Hoofdstad:").grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)
tk.Label(text="Aantal inwoners:").grid(row=2, column = 0, sticky = "w", padx = 5, pady = 5)
tk.Label(text="Levensverwachting:").grid(row=3, column = 0, sticky = "w", padx = 5, pady = 5)

# Programma uitvoeren
venster.mainloop()