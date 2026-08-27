import { useState } from "react";

function FormularioUsuario({ onUsuarioCreado }) {

    const [nombre, setNombre] = useState("");
    const [apellido, setApellido] = useState("");
    const [telefono, setTelefono] = useState("");
    const [edad, setEdad] = useState("");
    const [cargando, setCargando] = useState(false);
    const [error, setError] = useState("");

    async function guardarUsuario(e) {

        e.preventDefault();
        setError("");

        if (!nombre || !apellido || !telefono || !edad) {
            setError("Todos los campos son obligatorios");
            return;
        }

        try {

            setCargando(true);

            await onUsuarioCreado({
                nombre,
                apellido,
                telefono,
                edad: Number(edad)
            });

            setNombre("");
            setApellido("");
            setTelefono("");
            setEdad("");

        } catch (error) {

            setError(error.message);

        } finally {

            setCargando(false);
        }
    }

    return (
        <form className="formulario" onSubmit={guardarUsuario}>

            <h2>Registrar usuario</h2>

            {error && (
                <div className="alerta error">
                    {error}
                </div>
            )}

            <input
                type="text"
                placeholder="Nombre"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
            />

            <input
                type="text"
                placeholder="Apellido"
                value={apellido}
                onChange={(e) => setApellido(e.target.value)}
            />

            <input
                type="text"
                placeholder="Teléfono"
                value={telefono}
                onChange={(e) => setTelefono(e.target.value)}
            />

            <input
                type="number"
                placeholder="Edad"
                value={edad}
                onChange={(e) => setEdad(e.target.value)}
            />

            <button type="submit" disabled={cargando}>
                {cargando ? "Guardando..." : "Guardar usuario"}
            </button>

        </form>
    );
}

export default FormularioUsuario;
