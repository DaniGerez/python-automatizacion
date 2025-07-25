import sqlite3

def conectar():
    """
    Establece y retorna la conexión con la base de datos.
    """
    return sqlite3.connect('inventario.db')

def crear_tabla():
    """
    Crea la tabla 'productos' si no existe.
    """
    con = conectar()
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    con.commit()
    con.close()
