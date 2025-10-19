from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.config.db import SessionLocal

rol = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@rol.get("/get/roles")
def get_all_roles(db: Session = Depends(get_db)):
    sql = text("SELECT * FROM roles")
    result = db.execute(sql).mappings().all()
    
    # result es una lista de diccionarios, una por cada fila
    return [dict(row) for row in result]

@rol.get("/get/rol/{rol_id}")
def get_rol_by_id(rol_id: int, db: Session = Depends(get_db)):
    sql = text("SELECT * FROM roles WHERE rol_id = :rol_id")
    result = db.execute(sql, {"rol_id": rol_id}).mappings().fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return dict(result)  

@rol.post("/roles/Agregar Rol/")
def create_rol(rol_name: str, db: Session = Depends(get_db)):
    sql = text("INSERT INTO roles (rol_name) VALUES (:rol_name)")
    db.execute(sql, {"rol_name": rol_name})
    db.commit()
    return {"message": "Rol insertado con SQL crudo"}

@rol.put("/roles/raw_update/{rol_id}")
def Update_rol(rol_id: int, rol_name: str, db: Session = Depends(get_db)):
    sql = text("UPDATE roles SET rol_name = :rol_name WHERE rol_id = :rol_id")
    result = db.execute(sql, {"rol_name": rol_name, "rol_id": rol_id})
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"message": f"Rol {rol_id} actualizado"}

@rol.delete("/roles/raw_delete/{rol_id}")
def Delete_rol(rol_id: int, db: Session = Depends(get_db)):
    sql = text("DELETE FROM roles WHERE rol_id = :rol_id")
    result = db.execute(sql, {"rol_id": rol_id})
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"message": f"Rol {rol_id} eliminado"}