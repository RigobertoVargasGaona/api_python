from app.config.database import get_connection

def obtener_roles():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM roles")
    roles = cursor.fetchall()
    conn.close()
    return roles

def obtener_rol_por_id(rol_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM roles WHERE rol_id = %s", (rol_id,))
    rol = cursor.fetchone()
    conn.close()
    return rol

def crear_rol(rol_name: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO roles (rol_name) VALUES (%s)", (rol_name,))
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return obtener_rol_por_id(nuevo_id)

def actualizar_rol(rol_id: int, rol_name: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE roles SET rol_name = %s WHERE rol_id = %s", (rol_name, rol_id))
    conn.commit()
    conn.close()
    return obtener_rol_por_id(rol_id)

def eliminar_rol(rol_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM roles WHERE rol_id = %s", (rol_id,))
    conn.commit()
    conn.close()
