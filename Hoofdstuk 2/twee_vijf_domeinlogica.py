from twee_vier_datalaag import Datalaag

class Domeinlogica:
    def __init__(self, datalaag):
        self.datalaag = datalaag

    # Code om nieuwe stad op te slaan.
    def opslaan_stad(self, naam, code, district, populatie):
        try:
            if not naam or not code:
                 raise ValueError("Fout: Vul alle verplichte velden in!")
            
            if self.datalaag.store_stad(naam, code, district, populatie):
                return "De nieuwe stad is opgeslagen."

        except ValueError as e:
            return str(e)
        
        except Exception as e:
            return f"Onverwachte fout bij het opslaan van de stad: {e}"  
