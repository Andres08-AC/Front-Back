# Importa la clase BaseModel de Pydantic para la definicion y validacion de esquemas.
from pydantic import BaseModel


# Esquema Pydantic para validar los datos recibidos al crear un usuario.
class UsuarioCreate(BaseModel):
    nombre: str     # Define el campo 'nombre' como una cadena de texto obligatoria.
    apellido: str   # Define el campo 'apellido' como una cadena de texto obligatoria.
    telefono: str   # Define el campo 'telefono' como una cadena de texto obligatoria.
    edad: int       # Define el campo 'edad' como un numero entero obligatorio.


# Esquema Pydantic para estructurar la respuesta devuelta por la API al cliente.
class UsuarioResponse(BaseModel):
    id: int         # Incluye el 'id' entero generado por la base de datos.
    nombre: str     # Incluye el nombre del usuario en la respuesta.
    apellido: str   # Incluye el apellido del usuario en la respuesta.
    telefono: str   # Incluye el telefono del usuario en la respuesta.
    edad: int       # Incluye la edad del usuario en la respuesta.

    # Subclase interna de configuracion para ajustar el comportamiento de Pydantic.
    class Config:
        # Permite mapear modelos ORM de SQLAlchemy directamente a esquemas de Pydantic.
        from_attributes = True