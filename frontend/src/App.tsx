
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import {MedicoForm, MedicoList, SideBar} from "./components"
import { TurnosForm } from "./components/CalendarioTurnos/TurnosForm";
import { EspecialidadList } from "./components/EspecialidadList/EspecialidadList";
import { EspecialidadForm } from "./components/EspecialidadForm/EspecialidadForm";
import { MedicoTurnos } from "./components/MedicoTurno/MedicoTurnos";
import { NuevoTurnoForm } from "./components/TurnoForm/NuevoTurnoForm";
import { AgendaForm } from "./components/AgendaForm/AgendaForm";
import { AgendaList } from "./components/AgendaList/AgendaList";


function App() {

  return (
    <>
      <Router>
      <SideBar/>
      <div className="content" style={{ marginLeft: "260px", padding: "20px" }}>
        <Routes>
          <Route path="/"element={<h1>Bienvenido</h1>}></Route>
          <Route path="/nuevo-medico"element={<MedicoForm/>}></Route>
          <Route path="/medicos"element={<MedicoList/>}></Route>
          <Route path="/turnos" element={<TurnosForm/>}></Route>
          <Route path="/especialidades" element={<EspecialidadList />} />
          <Route path="/nueva-especialidad" element={<EspecialidadForm />} />
          <Route path="/turnos-medico" element={<MedicoTurnos />}> </Route>
          <Route path="/nuevo-turno" element={<NuevoTurnoForm />}> </Route>
          <Route path="/nueva-agenda" element={<AgendaForm />}> </Route>
          <Route path="/agendas" element={<AgendaList />}> </Route>
        </Routes>
        </div>
    </Router>
    </>
  )
}

export default App
