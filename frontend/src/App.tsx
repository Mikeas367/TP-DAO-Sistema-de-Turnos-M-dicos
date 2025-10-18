
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import {MedicoForm, MedicoList, SideBar} from "./components"


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
        </Routes>
        </div>
    </Router>
    </>
  )
}

export default App
