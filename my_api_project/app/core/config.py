# app/core/config.py

import os

# Clave secreta para firmar los JWT. ¡Cámbiala y protégela!
SECRET_KEY = os.getenv("SECRET_KEY", "tu-clave-secreta-muy-larga-y-segura")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Duración del token en minutos