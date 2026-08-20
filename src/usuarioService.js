const API_URL = "http://127.0.0.1:8000";

export async function obtenerUsuarios() {
    const respuesta = await fetch(`${API_URL}/listadeusuarios`);

    if (!respuesta.ok) {
        throw new Error("No se pudieron obtener los usuarios");
    }

    return await respuesta.json();
}

export async function crearUsuario(usuario) {
    const respuesta = await fetch(
        `${API_URL}/agregarusuarios`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(usuario)
        }
    );

    if (!respuesta.ok) {
        const error = await respuesta.json();
        throw new Error(error.detail || "No se pudo crear el usuario");
    }

    return await respuesta.json();
}

export async function eliminarUsuario(id) {
    const respuesta = await fetch(
        `${API_URL}/eliminarusuario/${id}`,
        {
            method: "DELETE"
        }
    );

    if (!respuesta.ok) {
        const error = await respuesta.json();
        throw new Error(error.detail || "No se pudo eliminar el usuario");
    }

    return await respuesta.json();
}
