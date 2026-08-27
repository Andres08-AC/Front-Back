# Importa componentes clave de FastAPI: la clase principal, inyeccion de dependencias y excepciones HTTP.
from fastapi import FastAPI, Depends, HTTPException
# Importa el middleware de CORS para habilitar solicitudes de origen cruzado.
from fastapi.middleware.cors import CORSMiddleware
# Importa el tipo Session de SQLAlchemy para el anotado de tipos en las funciones.
from sqlalchemy.orm import Session

# Importa la base de modelos, el motor de BD y el generador de sesiones desde database.py.
from database import Base, engine, get_db
# Importa los esquemas Pydantic para entrada y salida de datos desde schemas.py.
from schemas import UsuarioCreate, UsuarioResponse
# Importa el archivo crud.py 
import crud


# Genera todas las tablas definidas en la base de datos si no han sido creadas previamente.
Base.metadata.create_all(bind=engine)


# Instancia la aplicacion principal de FastAPI definiendo titulo y version para Swagger UI.
app = FastAPI(
    title="API Usuarios Universitaria",
    version="1.0.0"
)


# Habilita el middleware CORS para autorizar peticiones desde el cliente web (React).
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Permite origen desde servidor local de desarrollo Vite/React.
        "http://127.0.0.1:5173"    # Permite origen desde la direccion IP equivalente.
    ],
    allow_credentials=True,        # Permite el envio de credenciales y cookies en las peticiones.
    allow_methods=["*"],           # Autoriza todos los metodos HTTP (GET, POST, DELETE, etc.).
    allow_headers=["*"]            # Autoriza todas las cabeceras HTTP.
)


# Define una ruta GET en la raiz del servicio para verificar el estado de la API.
@app.get("/")
def inicio():
    # Retorna un mensaje simple en formato texto/json al acceder a la raiz.
    return "Bienvenido al programa usuarios"


# Ruta GET para obtener la lista completa de usuarios mapeada segun UsuarioResponse.
@app.get(
    "/listadeusuarios",
    response_model=list[UsuarioResponse]
)
def obtener_usuarios(db: Session = Depends(get_db)):
    # Ejecuta la funcion del archivo crud pasando la sesion inyectada para devolver los usuarios.
    return crud.obtener_usuarios(db)


# Ruta POST para crear un nuevo registro de usuario devolviendo codigo HTTP 201 (Created).
@app.post(
    "/agregarusuarios",
    response_model=UsuarioResponse,
    status_code=201
)
def agregar_usuario(
    datos: UsuarioCreate,           # Recibe y valida los datos con el esquema UsuarioCreate.
    db: Session = Depends(get_db)   # Inyecta la sesion activa de la base de datos.
):
    # Llama a la funcion de creacion en el modulo crud y retorna el nuevo usuario guardado.
    return crud.crear_usuario(db, datos)


# Ruta GET dinamica para consultar un usuario en particular mediante su ID.
@app.get(
    "/listadeusuarios/{id}",
    response_model=UsuarioResponse
)
def obtener_usuario(
    id: int,                        # Recibe la variable de ruta 'id' convertida a entero.
    db: Session = Depends(get_db)   # Inyecta la sesion de la base de datos.
):
    # Busca al usuario correspondiente en la base de datos mediante crud.
    usuario = crud.obtener_usuario(db, id)

    # Verifica si el usuario solicitado no existe en la base de datos.
    if usuario is None:
        # Lanza una excepcion HTTP con codigo 404 de recurso no encontrado.
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    # Retorna la informacion del usuario si fue encontrado exitosamente.
    return usuario


# Ruta DELETE dinamica para remover un usuario del sistema segun su ID.
@app.delete("/eliminarusuario/{id}")
def eliminar_usuario(
    id: int,                        # Recibe el parametro de ruta 'id' de tipo entero.
    db: Session = Depends(get_db)   # Inyecta la sesion de base de datos.
):
    # Ejecuta la eliminacion del usuario mediante la funcion del modulo crud.
    usuario = crud.eliminar_usuario(db, id)

    # Verifica si no existia el usuario que se intento borrar.
    if usuario is None:
        # Retorna error 404 en caso de no hallar el registro para eliminar.
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    # Retorna un diccionario con un mensaje de confirmacion tras la eliminacion exitosa.
    return {
        "mensaje": "Usuario eliminado exitosamente"
    }