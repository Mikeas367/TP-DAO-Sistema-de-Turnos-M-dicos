import sqlite3

class Database:
    def __init__(self, db_name="medicos.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):

        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS especialidades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL, 
                    descripcion TEXT NOT NULL   
                )
            ''')
        

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                email TEXT UNIQUE,
                especialidad_id INTEGER NOT NULL,
                FOREIGN KEY (especialidad_id) REFERENCES especialidades(id)
            )
        ''')

        
        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor