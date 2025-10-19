# Para crear la estructura de carpetas pegar este codigo en la git bush
```
mkdir -p mi_api/app/{models,schemas,routes,controllers} && \
touch mi_api/app/__init__.py \
      mi_api/app/main.py \
      mi_api/app/config.py \
      mi_api/app/database.py \
      mi_api/app/models/user_model.py \
      mi_api/app/schemas/user_schema.py \
      mi_api/app/routes/user_routes.py \
      mi_api/app/controllers/user_controller.py \
      mi_api/requirements.txt \
      mi_api/README.md && \
echo "✅ Estructura base de API REST creada correctamente."

```
# 1. Crear entorno virtual para api en Python
```bash
python -m venv .venv
```
# 2. Activar el entorno virtual
```bash
venv/Scripts/activate
```
# 3. Instala los paquetes del Framework y el servidor
```bash
python -m pip install fastapi uvicorn
```

# 4. Actualizar dependecias

```bash
pip freeze > requirements.txt
```
# 5. Poner a correr el servidor

```bash
uvicorn app.main:app --reload
```