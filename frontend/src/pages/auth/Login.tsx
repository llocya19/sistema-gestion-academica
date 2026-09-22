import {useState} from "react";
import {login} from "../../services/authService";

import "./Login.css";

import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";


function Login(){

const { iniciarSesion } = useAuth();
const navigate = useNavigate();

const [email,setEmail]=useState("");
const [password,setPassword]=useState("");




const handleSubmit = async(e:any)=>{

e.preventDefault();


try{


const response = await login({

email,
password

});


iniciarSesion(
  response.access_token,
  response.usuario
);

navigate("/home");



}catch(error){

console.log(error);


}


}



return(


<div className="login-container">


<div className="login-card">


<h1 className="login-title">

Sistema de Gestión Académica

</h1>



<form onSubmit={handleSubmit}>


<input

className="login-input"

placeholder="email"

value={email}

onChange={
e=>setEmail(e.target.value)
}

/>



<input

className="login-input"

type="password"

placeholder="Contraseña"

value={password}

onChange={
e=>setPassword(e.target.value)
}

/>



<button className="login-button">

Ingresar

</button>



</form>


</div>


</div>


)


}


export default Login;