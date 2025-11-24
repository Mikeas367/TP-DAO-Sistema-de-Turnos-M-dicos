import sqlite3

class Database:
    def __init__(self, db_name="medicos.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Tabla de Especialidades
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS especialidades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL, 
                    descripcion TEXT NOT NULL   
                )
            ''')
        
        # Tabla de Medicos
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
        
        # Tabla de Pacientes
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                email TEXT UNIQUE
            )
        ''')

        # Tabla de Estados
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS estados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT
            )
        ''')

        # Tabla de Turnos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS turnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER,
                medico_id INTEGER NOT NULL,
                estado_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
                FOREIGN KEY (medico_id) REFERENCES medicos(id),
                FOREIGN KEY (estado_id) REFERENCES estados(id)
            )
        ''')

        # Tabla Historial clinico
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS historiales (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            medico_id INTEGER NOT NULL,
                            fecha TEXT NOT NULL,
                            paciente_id INTEGER NOT NULL,
                            diagnostico TEXT NOT NULL,
                            tratamiento TEXT NOT NULL,
                            FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
                            FOREIGN KEY (medico_id) REFERENCES medicos(id)
                            )
            ''')
        
        # Tabla Agenda
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS agendas_medico (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    medico_id INTEGER NOT NULL,
                    FOREIGN KEY (medico_id) REFERENCES medicos(id)
                    )   
            ''')
        
        # Tabla Dia Laboral 
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS agenda_dias_trabajo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    agenda_id INTEGER NOT NULL,
                    dia_semana INTEGER NOT NULL,       -- 0 a 6
                    hora_inicio TEXT NOT NULL,         -- "08:00"
                    hora_fin TEXT NOT NULL,            -- "12:00"
                    duracion_turno_min INTEGER NOT NULL,

                    FOREIGN KEY (agenda_id) REFERENCES agendas_medico(id)
                    )
            ''')
        
        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor