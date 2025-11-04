# app/main.py

from fastapi import FastAPI
from app.config.database import init_db
from app.routes import role_routes
from app.routes import auth_routes 

app = FastAPI(title="MY_API_PROJECT - JWT Integrado")

# Inicializamos la base de datos al iniciar
# Asumo que la importación de init_db es correcta
init_db()

# Registramos las rutas
app.include_router(auth_routes.router) 
app.include_router(role_routes.router)

@app.get("/")
def read_root():
    return {"message": "API está funcionando correctamente. Visita /docs para la documentación."}