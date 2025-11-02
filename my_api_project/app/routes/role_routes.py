from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers import role_controller

router = APIRouter(prefix="/roles", tags=["Roles"])

class RolRequest(BaseModel):
    rol_name: str

@router.get("/")
def listar_roles():
    return role_controller.listar_roles()

@router.get("/{rol_id}")
def obtener_rol(rol_id: int):
    return role_controller.obtener_rol(rol_id)

@router.post("/")
def crear_rol(rol: RolRequest):
    return role_controller.crear_rol(rol.rol_name)

@router.put("/{rol_id}")
def actualizar_rol(rol_id: int, rol: RolRequest):
    return role_controller.actualizar_rol(rol_id, rol.rol_name)

@router.delete("/{rol_id}")
def eliminar_rol(rol_id: int):
    return role_controller.eliminar_rol(rol_id)

