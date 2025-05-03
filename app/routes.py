from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, crud, config, database

router = APIRouter()

@router.post("/libros", response_model=schemas.LibroCreate)
def create_libro(libro: schemas.LibroCreate, db: Session = Depends(config.SessionLocal)):
    return crud.create_libro(db, libro)

@router.get("/libros", response_model=list[schemas.LibroCreate])
def get_libros(db: Session = Depends(config.SessionLocal)):
    return crud.get_libros(db)

@router.put("/libros/{libro_id}", response_model=schemas.LibroCreate)
def actualizar_libro(libro_id: int, libro: schemas.LibroCreate, db: Session = Depends(database.get_db)):
    actualizado = crud.actualizar_libro(db, libro_id, libro)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return actualizado

@router.delete("/libros/{libro_id}", response_model=schemas.LibroCreate)
def eliminar_libro(libro_id: int, db: Session = Depends(database.get_db)):
    eliminado = crud.eliminar_libro(db, libro_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return eliminado