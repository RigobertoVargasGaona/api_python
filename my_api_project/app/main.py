from fastapi import FastAPI
from app.config.database import init_db
from app.routes import role_routes

app = FastAPI(title="API de Roles - MVC con SQL crudo")

# Inicializamos la base de datos al iniciar
init_db()

# Registramos las rutas
app.include_router(role_routes.router)
