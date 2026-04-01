# repository.py
# Capa de acceso a datos: todas las operaciones SQL están aquí.
# No conoce la lógica de negocio ni los detalles HTTP; solo habla con la BD.

from sqlalchemy.orm import Session
from model import Producto
from schema import ProductoCreate, ProductoUpdate


def get_all(db: Session) -> list[Producto]:
    # Retorna todos los productos almacenados
    return db.query(Producto).all()


def get_by_id(db: Session, producto_id: int) -> Producto | None:
    # Busca un producto por su clave primaria; retorna None si no existe
    return db.query(Producto).filter(Producto.id == producto_id).first()


def create(db: Session, data: ProductoCreate) -> Producto:
    # Crea un nuevo registro en la tabla productos
    nuevo = Producto(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)   # actualiza el objeto con el id generado por la BD
    return nuevo


def update(db: Session, producto: Producto, data: ProductoUpdate) -> Producto:
    # Actualiza solo los campos que vienen con valor en el cuerpo de la petición
    cambios = data.model_dump(exclude_none=True)
    for campo, valor in cambios.items():
        setattr(producto, campo, valor)
    db.commit()
    db.refresh(producto)
    return producto


def delete(db: Session, producto: Producto) -> None:
    # Elimina el registro de la BD
    db.delete(producto)
    db.commit()
