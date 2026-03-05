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
        
    def store_stad(self, naam, code, district, populatie):
        """Voeg een nieuwe stad toe."""

        query = """
                    INSERT INTO city (Name, CountryCode, District, Population)
                    VALUES (%s, %s , %s , %s)
                    """

        try:
            with self.connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, (naam, code, district, populatie))
                    connection.commit()
                    return True
                
        except Error as e:
            raise Exception(f"Fout bij het ophalen van gegevens: {e}")