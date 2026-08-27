# Importa la funcion create_engine de SQLAlchemy 
from sqlalchemy import create_engine
# Importa sessionmaker y declarative_base 
from sqlalchemy.orm import sessionmaker, declarative_base
# Importa load_dotenv para cargar variables de entorno desde un archivo .env.
from dotenv import load_dotenv
# Importa el modulo os de Python para acceder a las variables del sistema operativo.
import os

# Carga las variables definidas en el archivo .env en el entorno de la aplicacion.
load_dotenv()

# Obtiene el valor de la variable de entorno DATABASE_URL que contiene la cadena de conexion.
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de la base de datos utilizando la URL obtenida previamente.
engine = create_engine(DATABASE_URL)

# Crea una clase de fabrica para instanciar sesiones de base de datos personalizadas.
SessionLocal = sessionmaker(
    bind=engine,           # Enlaza la sesion con el motor de base de datos configurado.
    autoflush=False,       # Desactiva el envio automatico de cambios a la BD antes de cada consulta.
    autocommit=False       # Desactiva la confirmacion automatica para manejar transacciones manualmente.
)

# Crea la clase base para que los modelos ORM hereden de ella y mapeen las tablas.
Base = declarative_base()

# Define una funcion generadora para gestionar el ciclo de vida de la sesion de BD por peticion.
def get_db():
    # Instancia una nueva sesion de base de datos.
    db = SessionLocal()
    
    try:
        # Entrega la sesion activa al contexto que la solicito (ej. endpoint de FastAPI).
        yield db
    finally:
        # Garantiza que la sesion se cierre siempre al finalizar, liberando la conexion.
        db.close()