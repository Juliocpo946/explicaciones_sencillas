# router.py
# Define los endpoints HTTP para la entidad Producto.
# Solo maneja la capa HTTP: recibe peticiones, llama al service y retorna respuestas.

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import service
from schema import ProductoCreate, ProductoUpdate, ProductoResponse
from database import get_db

# Prefijo común para todas las rutas de este router
router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=list[ProductoResponse])
def listar(db: Session = Depends(get_db)):
    # GET /productos — retorna todos los productos
    return service.obtener_todos(db)


@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener(producto_id: int, db: Session = Depends(get_db)):
    # GET /productos/{id} — retorna un producto por su id
    return service.obtener_por_id(db, producto_id)


@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear(data: ProductoCreate, db: Session = Depends(get_db)):
    # POST /productos — crea un nuevo producto con los datos del cuerpo
    return service.crear(db, data)


@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    # PUT /productos/{id} — actualiza los campos enviados en el cuerpo
    return service.actualizar(db, producto_id, data)


@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(producto_id: int, db: Session = Depends(get_db)):
    # DELETE /productos/{id} — elimina el producto; retorna 204 sin cuerpo
    service.eliminar(db, producto_id)
