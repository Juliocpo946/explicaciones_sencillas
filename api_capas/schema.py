# schema.py
# Define los esquemas Pydantic que validan los datos que entran y salen de la API.
# Son independientes del modelo ORM: el ORM habla con la BD, los schemas con el cliente.

from pydantic import BaseModel, Field
from typing import Optional


class ProductoCreate(BaseModel):
    # Esquema para crear un producto (el id lo genera la BD, no se recibe)
    nombre: str = Field(..., max_length=100, description="Nombre del producto")
    descripcion: Optional[str] = Field(None, max_length=255)
    precio: float = Field(..., gt=0, description="Precio debe ser mayor a 0")


class ProductoUpdate(BaseModel):
    # Esquema para actualizar; todos los campos son opcionales
    nombre: Optional[str] = Field(None, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)
    precio: Optional[float] = Field(None, gt=0)


class ProductoResponse(BaseModel):
    # Esquema de respuesta: incluye el id generado por la BD
    id: int
    nombre: str
    descripcion: Optional[str]
    precio: float

    class Config:
        # Permite construir el schema desde un objeto ORM directamente
        from_attributes = True
