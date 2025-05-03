from pydantic import BaseModel, EmailStr, Field

class LibroCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=255)
    autor: str = Field(..., min_length=3, max_length=255)
    anio_publicacion: int = Field(..., gt=1900, lt=2100)

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str

class LibroUpdate(BaseModel):  # ✅ Usado para actualizar libros (datos opcionales)
    titulo: str = None
    autor: str = None
    anio_publicacion: int = None