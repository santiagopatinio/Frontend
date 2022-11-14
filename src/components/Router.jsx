import { HashRouter, Routes, Route } from "react-router-dom"
import LoginPage from "../pages/Login"
import HomePage from "../pages/HomePage"
import Info from "../pages/InfoInstitucional"
import Navbar from "../pages/Navbar"
import Cursoshomepage from "../pages/Cursoshomepage"
import Carrerahomepage from "../pages/Carrerahomepage"


import AdminPage from "../pages/admin/Admin"
import SecretarioPage from "../pages/secretario/Secretario"

import AlumnoPage from "../pages/alumno/Alumno"
    import CursoAlumnoPage from "../pages/alumno/CursoControl"  
    
import ProfesorPage from "../pages/profesor/Profesor"
    import CursoProfesorPage from "../pages/profesor/CursoControl"
    import AlumnoControlPage from "../pages/profesor/AlumnoControl"
import { Switch } from "@mui/material"


export default function Router() {
    return (
        <HashRouter>
            <Routes>
                <Route exact path='/' element={ <Navbar /> }>
                        <Route index element={ <HomePage /> } />
                        <Route exact path="/login" element= { <LoginPage /> } />
                        <Route exact path="/inscripcion" element= { <HomePage /> } />
                        <Route exact path="/informacion" element= { <Info /> } />    
                        <Route exact path="/cursos" element= { <Cursoshomepage /> } />  
                        <Route exact path="/carrera" element= { <Carrerahomepage /> } />                            
                </Route>
                    <Route exact path="/alumno" element= { <AlumnoPage/> } />
                        <Route exact path="/alumno/curso" element= { <CursoAlumnoPage /> } />
                    <Route exact path="/profesor" element= { <ProfesorPage /> } />
                        <Route exact path="/profesor/curso" element= { <CursoProfesorPage /> } />
                        <Route exact path="/profesor/curso/alumno" element= { <AlumnoControlPage /> } />
                    <Route exact path="/secretario" element= { <SecretarioPage /> } />
                        <Route exact path="/secretario/alumno/:id" element= { <SecretarioPage origen ={2}/> } />
                    <Route exact path="/admin" element= { <AdminPage /> } />
            </Routes>
        </HashRouter>
    )
}