# Labels toevoegen
# -------------------------------------------------------
import tkinter as tk

# Venster aanmaken
venster = tk.Tk()
venster.title("Europese landen")

# Labels aanmaken
tk.Label(text="Land:").grid(row = 0, column = 0)
tk.Label(text="Hoofdstad:").grid(row = 1, column = 0)
tk.Label(text="Aantal inwoners:").grid(row = 2, column = 0)
tk.Label(text="Levensverwachting:").grid(row = 3, column = 0)

# Programma uitvoeren
venster.mainloop()