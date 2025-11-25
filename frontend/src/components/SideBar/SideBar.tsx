import { Link } from 'react-router-dom';
import './Sidebar.css';

import "bootstrap/dist/css/bootstrap.min.css";
import 'bootstrap/dist/js/bootstrap.bundle.min';

export const SideBar = () =>  {
    return(
    <>
    <div className="sidebar">
        <h1 className="sidebar-title">Menú</h1>

        <ul className="nav flex-colum">

            <li className='nav-item'>
                <Link to="/" className='nav-link'>
                    Inicio
                </Link>
            </li>

            {/* Médicos */}
            <li className='nav-item'>
                <Link to="/nuevo-medico" className='nav-link'>
                    Nuevo Médico
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/medicos" className='nav-link'>
                    Listado de Médicos
                </Link>
            </li>

            {/* Especialidades */}
            <li className='nav-item'>
                <Link to="/especialidades" className='nav-link'>
                    Listado de Especialidades
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/nueva-especialidad" className='nav-link'>
                    Nueva Especialidad
                </Link>
            </li>

            {/* Turnos */}
            <li className='nav-item'>
                <Link to="/turnos" className='nav-link'>
                    Turnos
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/turnos-medico" className='nav-link'>
                    Turnos por Médico
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/nuevo-turno" className='nav-link'>
                    Nuevo Turno
                </Link>
            </li>

            {/* Agendas */}
            <li className='nav-item'>
                <Link to="/nueva-agenda" className='nav-link'>
                    Nueva Agenda
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/agendas" className='nav-link'>
                    Listado de Agendas
                </Link>
            </li>

            {/* Pacientes */}
            <li className='nav-item'>
                <Link to="/pacientes" className='nav-link'>
                    Listado de Pacientes
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/nuevo-paciente" className='nav-link'>
                    Nuevo Paciente
                </Link>
            </li>

            {/* Reportes */}
            <li className='nav-item'>
                <Link to="/reportes" className='nav-link'>
                    Reportes
                </Link>
            </li>

            {/* Recetas */}
            <li className='nav-item'>
                <Link to="/recetas" className='nav-link'>
                    Recetas
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/recetas/nueva" className='nav-link'>
                    Nueva Receta
                </Link>
            </li>

        </ul>
    </div>
    </>
    );
}

export default SideBar;
