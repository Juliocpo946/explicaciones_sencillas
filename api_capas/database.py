# database.py
# Configura el motor de base de datos y la sesión de SQLAlchemy.
# También expone la clase base para que los modelos puedan heredar de ella.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings


# Motor de conexión; check_same_thread=False es necesario solo para SQLite
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Fábrica de sesiones: cada petición HTTP abrirá y cerrará una sesión propia
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    # Clase base de la que heredan todos los modelos ORM
    pass


def get_db():
    # Generador que provee una sesión de BD por petición y la cierra al terminar.
    # Se usa como dependencia inyectada en los routers con Depends(get_db).
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
