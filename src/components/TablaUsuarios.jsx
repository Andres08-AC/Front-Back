function TablaUsuarios({ usuarios, onEliminar }) {

    return (
        <div className="tabla-contenedor">

            <h2>Usuarios registrados</h2>

            {usuarios.length === 0 ? (
                <p className="vacio">
                    No hay usuarios registrados.
                </p>
            ) : (

                <table>

                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Apellido</th>
                            <th>Teléfono</th>
                            <th>Edad</th>
                            <th>Acción</th>
                        </tr>
                    </thead>

                    <tbody>

                        {usuarios.map((usuario) => (

                            <tr key={usuario.id}>

                                <td>{usuario.id}</td>
                                <td>{usuario.nombre}</td>
                                <td>{usuario.apellido}</td>
                                <td>{usuario.telefono}</td>
                                <td>{usuario.edad}</td>

                                <td>
                                    <button
                                        className="btn-eliminar"
                                        onClick={() => onEliminar(usuario.id)}
                                    >
                                        Eliminar
                                    </button>
                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            )}

        </div>
    );
}

export default TablaUsuarios;
