# app/models/auth_schema.py

from pydantic import BaseModel

# Esquema para la solicitud de inicio de sesión (espera JSON)
class LoginSchema(BaseModel):
    username: str
    password: str