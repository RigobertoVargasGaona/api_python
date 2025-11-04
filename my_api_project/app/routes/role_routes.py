# app/routes/role_routes.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.controllers import role_controller
from app.core.security import get_current_user # <-- Importar JWT Dependency

router = APIRouter(prefix="/roles", tags=["Roles"])

class RolRequest(BaseModel):
    rol_name: str
    
# Todas las rutas ahora requieren un token JWT válido (Depends(get_current_user))

@router.get("/")
def listar_roles(current_user: str = Depends(get_current_user)): 
    """Lista todos los roles (requiere token JWT)."""
    return role_controller.listar_roles()

@router.get("/{rol_id}")
def obtener_rol(rol_id: int, current_user: str = Depends(get_current_user)):
    """Obtiene un rol por ID (requiere token JWT)."""
    return role_controller.obtener_rol(rol_id)

@router.post("/")
def crear_rol(rol: RolRequest, current_user: str = Depends(get_current_user)):
    """Crea un nuevo rol (requiere token JWT)."""
    return role_controller.crear_rol(rol.rol_name)

@router.put("/{rol_id}")
def actualizar_rol(rol_id: int, rol: RolRequest, current_user: str = Depends(get_current_user)):
    """Actualiza un rol existente (requiere token JWT)."""
    return role_controller.actualizar_rol(rol_id, rol.rol_name)

@router.delete("/{rol_id}")
def eliminar_rol(rol_id: int, current_user: str = Depends(get_current_user)):
    """Elimina un rol (requiere token JWT)."""
    return role_controller.eliminar_rol(rol_id)