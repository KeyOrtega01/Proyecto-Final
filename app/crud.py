from sqlalchemy.orm import Session
from . import models, schemas

def create_libro(db: Session, libro: schemas.LibroCreate):
    nuevo_libro = models.Libro(**libro.dict())
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

def get_libros(db: Session):
    return db.query(models.Libro).all()

def actualizar_libro(db: Session, libro_id: int, nuevo_libro: schemas.LibroCreate):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if not libro:
        return None

    libro.titulo = nuevo_libro.titulo
    libro.autor = nuevo_libro.autor
    libro.anio_publicacion = nuevo_libro.anio_publicacion

    db.commit()
    db.refresh(libro)
    return libro

def eliminar_libro(db: Session, libro_id: int):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if not libro:
        return None

    db.delete(libro)
    db.commit()
    return libro
