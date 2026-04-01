# config.py
# Lee las variables del archivo .env y las expone como un objeto tipado.
# Cualquier módulo que necesite configuración importa `settings` desde aquí.

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str
    APP_VERSION: str

    class Config:
        # Indica el archivo desde donde se cargan las variables
        env_file = ".env"


# Instancia única reutilizable en toda la aplicación
settings = Settings()
