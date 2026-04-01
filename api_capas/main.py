# main.py
# Punto de entrada de la aplicación FastAPI.
# Crea la app, registra los routers y crea las tablas al iniciar.

from fastapi import FastAPI
from database import engine, Base
from config import settings
import router as producto_router

# Crea todas las tablas definidas en los modelos si aún no existen
Base.metadata.create_all(bind=engine)

# Instancia principal de la aplicación con metadatos desde .env
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Registra el router de productos; todos sus endpoints quedan disponibles
app.include_router(producto_router.router)


# Ejecutar con: uvicorn main:app --reload
