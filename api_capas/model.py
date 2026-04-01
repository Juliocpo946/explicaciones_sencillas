# model.py
# Define la tabla `productos` en la base de datos mediante SQLAlchemy ORM.
# Cada instancia de Producto representa una fila en esa tabla.

from sqlalchemy import Column, Integer, String, Float
from database import Base


class Producto(Base):
    __tablename__ = "productos"

    # Clave primaria autoincremental
    id = Column(Integer, primary_key=True, index=True)

    # Nombre del producto; no puede ser nulo
    nombre = Column(String(100), nullable=False)

    # Descripción opcional del producto
    descripcion = Column(String(255), nullable=True)

    # Precio con decimales; no puede ser nulo
    precio = Column(Float, nullable=False)
