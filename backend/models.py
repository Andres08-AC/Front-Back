# Importa los tipos de datos Integer y String, y la clase Column de SQLAlchemy.
from sqlalchemy import Column, Integer, String
# Importa la clase Base desde el modulo database.py.
from database import Base


# Define el modelo ORM Usuario que hereda de Base para mapear la tabla.
class Usuario(Base):

    # Define el nombre de la tabla dentro de la base de datos SQL.
    __tablename__ = "usuarios"

    # Define la columna 'id' como clave primaria entera e indexada para busquedas rapidas.
    id = Column(Integer, primary_key=True, index=True)

    # Define la columna 'nombre' como texto de hasta 100 caracteres, campo obligatorio.
    nombre = Column(String(100), nullable=False)

    # Define la columna 'apellido' como texto de hasta 100 caracteres, campo obligatorio.
    apellido = Column(String(100), nullable=False)

    # Define la columna 'telefono' como texto de hasta 20 caracteres, campo obligatorio.
    telefono = Column(String(20), nullable=False)

    # Define la columna 'edad' como numero entero, campo obligatorio.
    edad = Column(Integer, nullable=False)