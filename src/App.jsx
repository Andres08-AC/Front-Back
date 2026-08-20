import { useEffect, useState } from "react";

import FormularioUsuario from "./components/FormularioUsuario";
import TablaUsuarios from "./components/TablaUsuarios";

import {
    obtenerUsuarios,
    crearUsuario,
    eliminarUsuario
} from "./services/usuarioService";

import "./App.css";


function App() {

    const [usuarios, setUsuarios] = useState([]);
    const [cargando, setCargando] = useState(true);
    const [mensaje, setMensaje] = useState("");
    const [error, setError] = useState("");


    async function cargarUsuarios() {

        try {

            setCargando(true);

            const datos = await obtenerUsuarios();

            setUsuarios(datos);

        } catch (error) {

            setError(error.message);

        } finally {

            setCargando(false);
        }
    }


    useEffect(() => {
        cargarUsuarios();
    }, []);


    async function manejarCrearUsuario(usuario) {

        await crearUsuario(usuario);

        setMensaje("Usuario registrado correctamente");

        await cargarUsuarios();

        setTimeout(() => {
            setMensaje("");
        }, 3000);
    }


    async function manejarEliminarUsuario(id) {

        const confirmar = window.confirm(
            "¿Está seguro de eliminar este usuario?"
        );

        if (!confirmar) {
            return;
        }

        try {

            await eliminarUsuario(id);

            setMensaje("Usuario eliminado correctamente");

            await cargarUsuarios();

            setTimeout(() => {
                setMensaje("");
            }, 3000);

        } catch (error) {

            setError(error.message);
        }
    }


    return (

        <div className="app">

            <header className="encabezado">

                <div className="logo-sena">
                    SENA
                </div>

                <div>
                    <h1>Gestión de Usuarios</h1>
                    <p>Aplicación Web Full Stack</p>
                </div>

            </header>


            <main className="contenido">

                <section className="bienvenida">

                    <span className="etiqueta">
                        PROYECTO ACADÉMICO
                    </span>

                    <h2>
                        Sistema de gestión de usuarios
                    </h2>

                    <p>
                        Frontend desarrollado con React
                        conectado a una API FastAPI.
                    </p>

                </section>


                {mensaje && (
                    <div className="alerta exito">
                        {mensaje}
                    </div>
                )}


                {error && (
                    <div className="alerta error">
                        {error}
                    </div>
                )}


                <section className="tarjetas">

                    <div className="tarjeta">
                        <strong>{usuarios.length}</strong>
                        <span>Usuarios registrados</span>
                    </div>

                    <div className="tarjeta">
                        <strong>React</strong>
                        <span>Frontend</span>
                    </div>

                    <div className="tarjeta">
                        <strong>FastAPI</strong>
                        <span>Backend</span>
                    </div>

                    <div className="tarjeta">
                        <strong>PostgreSQL</strong>
                        <span>Base de datos</span>
                    </div>

                </section>


                <section className="grid">

                    <FormularioUsuario
                        onUsuarioCreado={manejarCrearUsuario}
                    />

                    <div>

                        {cargando ? (
                            <div className="cargando">
                                Cargando usuarios...
                            </div>
                        ) : (

                            <TablaUsuarios
                                usuarios={usuarios}
                                onEliminar={manejarEliminarUsuario}
                            />

                        )}

                    </div>

                </section>

            </main>


            <footer>
                <p>
                    Proyecto académico Full Stack
                    • React + FastAPI + PostgreSQL
                </p>
            </footer>

        </div>
    );
}

export default App;
