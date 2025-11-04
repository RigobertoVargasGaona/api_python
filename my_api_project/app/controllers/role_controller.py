# app/controllers/role_controller.py

from fastapi import HTTPException
from app.models import role_model

def listar_roles():
    return role_model.obtener_roles()

def obtener_rol(rol_id: int):
    rol = role_model.obtener_rol_por_id(rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

def crear_rol(rol_name: str):
    return role_model.crear_rol(rol_name)

def actualizar_rol(rol_id: int, rol_name: str):
    rol_existente = role_model.obtener_rol_por_id(rol_id)
    if not rol_existente:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return role_model.actualizar_rol(rol_id, rol_name)

def eliminar_rol(rol_id: int):
    rol_existente = role_model.obtener_rol_por_id(rol_id)
    if not rol_existente:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    role_model.eliminar_rol(rol_id)
    return {"mensaje": "Rol eliminado correctamente"}