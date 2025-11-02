import pymysql

def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",  # cambia si tienes contraseña
        database="db_tracklinker",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS roles (
            rol_id INT AUTO_INCREMENT PRIMARY KEY,
            rol_name VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

