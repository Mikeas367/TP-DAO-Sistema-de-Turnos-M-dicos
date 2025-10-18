
import { Link } from 'react-router-dom';
import './Sidebar.css'

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
            <li className='nav-item'>
                <Link to="/nuevo-medico" className='nav-link'>
                    Nuevo Medico
                </Link>
            </li>
            <li className='nav-item'>
                <Link to="/medicos" className='nav-link'>
                    Listado de medicos
                </Link>
            </li>
        </ul>
    </div>  
    </>
)
}

export default SideBar;