import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_path):
        """Initialize the database manager with the given database path"""
        self.db_path = db_path
    
    def init_db(self):
        """Initialize the SQLite database if it doesn't exist"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Create table if it doesn't exist
        c.execute('''
        CREATE TABLE IF NOT EXISTS water_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            house_number TEXT NOT NULL,
            water_meter REAL NOT NULL,
            date TEXT NOT NULL,
            price REAL NOT NULL
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_reading(self, house_number, water_meter, date, price):
        """Add a new water meter reading to the database"""
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute(
                "INSERT INTO water_readings (house_number, water_meter, date, price) VALUES (?, ?, ?, ?)",
                (house_number, water_meter, date, price)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error adding reading: {e}")
            return False
    
    def get_data(self):
        """Get all water readings as a DataFrame"""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM water_readings", conn)
        conn.close()
        
        if not df.empty and 'date' in df.columns:
            df['Date'] = pd.to_datetime(df['date'])
            df['House Number'] = df['house_number']
            df['Water Meter'] = df['water_meter']
            df['Price'] = df['price']
        
        return df
    
    def clear_data(self):
        """Clear all data from the database"""
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute("DELETE FROM water_readings")
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error clearing data: {e}")
            return False
