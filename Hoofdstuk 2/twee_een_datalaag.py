import mysql.connector
from mysql.connector import Error

class Datalaag:

    def connect(self):
        """Connectie met de database maken."""
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Str3amIT#",
            database="world"
        )

    def get_steden(self, landcode):
        """Haal de levensverwachting van landen op een bepaald continent op."""

        query = """SELECT Name, Population FROM city WHERE CountryCode = %s """

        try:
            with self.connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, (landcode,))
                    return cursor.fetchall()
                
        except Error as e:
            raise Exception(f"Fout bij het ophalen van gegevens: {e}")