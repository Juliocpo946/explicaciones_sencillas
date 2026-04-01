# service.py
# Capa de lógica de negocio: orquesta llamadas al repository y aplica reglas.
# Es quien decide qué error HTTP lanzar cuando algo falla.

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import repository
from schema import ProductoCreate, ProductoUpdate
from model import Producto


def obtener_todos(db: Session) -> list[Producto]:
    # Delega la consulta al repository sin lógica adicional
    return repository.get_all(db)


def obtener_por_id(db: Session, producto_id: int) -> Producto:
    # Lanza 404 si el producto no existe; el router no necesita saber cómo
    producto = repository.get_by_id(db, producto_id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {producto_id} no encontrado",
        )
    return producto


def crear(db: Session, data: ProductoCreate) -> Producto:
    # Crea el producto; la validación de campos la hizo Pydantic en el schema
    return repository.create(db, data)


def actualizar(db: Session, producto_id: int, data: ProductoUpdate) -> Producto:
    # Verifica existencia antes de intentar actualizar
    producto = obtener_por_id(db, producto_id)
    return repository.update(db, producto, data)


def eliminar(db: Session, producto_id: int) -> None:
    # Verifica existencia antes de intentar eliminar
    producto = obtener_por_id(db, producto_id)
    repository.delete(db, producto)
