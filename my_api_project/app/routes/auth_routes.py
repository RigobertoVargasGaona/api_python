# app/routes/auth_routes.py

from fastapi import APIRouter, HTTPException, Depends
from datetime import timedelta
from app.core.security import create_access_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
# from app.models.auth_schema import LoginSchema # <-- Deshabilitamos la importación del JSON
from fastapi.security import OAuth2PasswordRequestForm # <-- ¡IMPORTAMOS EL FORMULARIO!

router = APIRouter(prefix="/auth", tags=["Auth"])
FAKE_USER = {"username": "admin", "password": "12345"}

@router.post("/login")
# CAMBIAMOS a 'form_data: OAuth2PasswordRequestForm = Depends()'
def login(form_data: OAuth2PasswordRequestForm = Depends()): 
    """Endpoint para iniciar sesión y obtener un token JWT, usando formulario."""
    
    # 1. Validación de credenciales
    # NOTA: Ahora usamos form_data.username y form_data.password
    if form_data.username != FAKE_USER["username"] or form_data.password != FAKE_USER["password"]:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
        
    # 2. Creación del token
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token({"sub": form_data.username}, expires_delta=expires)
    
    # 3. Respuesta exitosa
    return {
        "access_token": token, 
        "token_type": "bearer"
    }

# Asegúrate de eliminar o comentar el modelo LoginSchema en models/auth_schema.py 
# si decides usar solo el formulario, o mantenlo si lo usas en otro lugar.