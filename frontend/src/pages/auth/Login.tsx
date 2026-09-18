import {useState} from "react";
import {login} from "../../services/authService";

import "./Login.css";


function Login(){


const [username,setUsername]=useState("");
const [password,setPassword]=useState("");



const handleSubmit = async(e:any)=>{

e.preventDefault();


try{


const response = await login({

username,
password

});


console.log(response);


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

placeholder="Usuario"

value={username}

onChange={
e=>setUsername(e.target.value)
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