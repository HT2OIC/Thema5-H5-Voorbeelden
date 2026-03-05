from twee_een_datalaag import Datalaag

class Domeinlogica:
    def __init__(self, datalaag):
        self.datalaag = datalaag
    def ophalen_steden(self, landcode):
        try:
            if not landcode:
                 raise ValueError("Fout: De landcode mag niet leeg zijn!")
            
            if len(landcode)>3:
                raise ValueError("Fout: Een landcode mag niet langer zijn dan 3 karakters.")
            
            landcode = landcode.upper()
    
            resultaten = self.datalaag.get_steden(landcode)

            # Geen steden gevonden.
            # Lege lijst teruggeven en als gemiddelde 0.
            if not resultaten:
                return [], 0
            
            # Resultaten is een lijst van tuples [(stad1, pop1), (stad2, pop2), ...]
            steden = [stad[0] for stad in resultaten]
            populaties = [stad[1] for stad in resultaten]
    
            gemiddelde = round(sum(populaties)/len(populaties), 2)
            return steden, gemiddelde
        
        except ValueError as e:
            return str(e)
        
        except Exception as e:
            return f"Onverwachte fout bij het ophalen van steden: {e}"
