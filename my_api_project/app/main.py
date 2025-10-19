# app/main.py

from fastapi import FastAPI
from app.config.db import Base, engine
from app.routes import roles

# Crea las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Montar las rutas del módulo roles
app.include_router(roles.rol)
