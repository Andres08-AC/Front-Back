# Importa la clase Session de SQLAlchemy para manejar la sesion de la base de datos (tipado).
from sqlalchemy.orm import Session
# Importa el modelo ORM 'Usuario' que representa la tabla de usuarios en la base de datos.
from models import Usuario
# Importa el esquema Pydantic 'UsuarioCreate' para validar los datos recibidos al crear un usuario.
from schemas import UsuarioCreate


# Funcion para consultar y obtener todos los registros de usuarios.
def obtener_usuarios(db: Session):
    # Realiza la consulta sobre el modelo Usuario y retorna una lista con todos los registros de la tabla.
    return db.query(Usuario).all()


# Funcion para buscar y retornar un usuario especifico por su identificador unico (ID).
def obtener_usuario(db: Session, usuario_id: int):
    # Retorna el resultado de la consulta encadenada.
    return (
        # Prepara la consulta apuntando a la tabla/modelo Usuario.
        db.query(Usuario)
        # Aplica un filtro WHERE buscando la coincidencia exacta entre el ID de la base de datos y el recibido.
        .filter(Usuario.id == usuario_id)
        # Devuelve el primer resultado encontrado o 'None' si no existen coincidencias.
        .first()
    )


# Funcion para registrar un nuevo usuario en la base de datos.
def crear_usuario(db: Session, datos: UsuarioCreate):
    # Instancia el objeto ORM Usuario asignando los atributos del esquema Pydantic a cada columna.
    nuevo_usuario = Usuario(
        nombre=datos.nombre,      # Asigna el campo 'nombre' recibido a la columna 'nombre'.
        apellido=datos.apellido,  # Asigna el campo 'apellido' recibido a la columna 'apellido'.
        telefono=datos.telefono,  # Asigna el campo 'telefono' recibido a la columna 'telefono'.
        edad=datos.edad           # Asigna el campo 'edad' recibido a la columna 'edad'.
    )
    
    # Añade el objeto 'nuevo_usuario' a la sesion de la base de datos (aun no guardado definitivamente).
    db.add(nuevo_usuario)
    # Confirma la transaccion guardando permanentemente los cambios en la base de datos.
    db.commit()
    # Recarga el objeto desde la BD para obtener atributos generados automaticamente (como el ID autoincremental).
    db.refresh(nuevo_usuario)
    
    # Retorna la instancia del usuario recien creado con sus datos actualizados.
    return nuevo_usuario


# Funcion para borrar un usuario existente en la base de datos mediante su ID.
def eliminar_usuario(db: Session, usuario_id: int):
    # Reutiliza la función 'obtener_usuario' para buscar el registro que se desea eliminar.
    usuario = obtener_usuario(db, usuario_id)
    
    # Verifica si el usuario no fue encontrado en la base de datos.
    if usuario is None:
        # Si no existe, finaliza la ejecucion retornando 'None'.
        return None
        
    # Marca el objeto 'usuario' localizado para ser borrado dentro de la sesion actual.
    db.delete(usuario)
    # Confirma la transaccion impactando y eliminando definitivamente el registro de la base de datos.
    db.commit()
    
    # Retorna el objeto del usuario que fue eliminado (util para confirmaciones en la API).
    return usuario