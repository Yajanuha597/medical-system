const API="http://localhost:5000";


function token(){

return localStorage.getItem("token");

}




async function cargarPacientes(){


const respuesta = await fetch(
API+"/pacientes",
{

headers:{
"Authorization":"Bearer "+token()
}

});


const pacientes = await respuesta.json();



const tabla=document.getElementById("tablaPacientes");


tabla.innerHTML="";



pacientes.forEach(p=>{


tabla.innerHTML += `

<tr>

<td>${p.id}</td>

<td>${p.nombre}</td>

<td>${p.cedula}</td>

<td>${p.edad}</td>

<td>${p.telefono}</td>


<td>

<button onclick="editarPaciente(${p.id})">
✏️
</button>


<button onclick="eliminarPaciente(${p.id})">
🗑️
</button>


</td>


</tr>

`;


});


}




function mostrarFormulario(){

document.getElementById("formulario").style.display="block";

}




function cancelar(){

document.getElementById("formulario").style.display="none";

limpiar();

}




function limpiar(){

document.getElementById("idPaciente").value="";
document.getElementById("nombre").value="";
document.getElementById("cedula").value="";
document.getElementById("edad").value="";
document.getElementById("telefono").value="";
document.getElementById("direccion").value="";

}




async function guardarPaciente(){


const id=document.getElementById("idPaciente").value;



const datos={

nombre:
document.getElementById("nombre").value,

cedula:
document.getElementById("cedula").value,

edad:
Number(document.getElementById("edad").value),

telefono:
document.getElementById("telefono").value,

direccion:
document.getElementById("direccion").value

};



let url=API+"/pacientes";

let metodo="POST";



if(id){

url += "/"+id;

metodo="PUT";

}



await fetch(
url,
{

method:metodo,

headers:{

"Content-Type":"application/json",

"Authorization":"Bearer "+token()

},

body:JSON.stringify(datos)

});



cancelar();

cargarPacientes();


}




async function eliminarPaciente(id){


if(confirm("¿Eliminar paciente?")){


await fetch(

API+"/pacientes/"+id,

{

method:"DELETE",

headers:{

"Authorization":"Bearer "+token()

}

});


cargarPacientes();


}


}




async function editarPaciente(id){


const respuesta=await fetch(

API+"/pacientes/"+id,

{

headers:{

"Authorization":"Bearer "+token()

}

});


const p=await respuesta.json();



document.getElementById("idPaciente").value=p.id;

document.getElementById("nombre").value=p.nombre;

document.getElementById("cedula").value=p.cedula;

document.getElementById("edad").value=p.edad;

document.getElementById("telefono").value=p.telefono;

document.getElementById("direccion").value=p.direccion;



mostrarFormulario();


}




function cerrarSesion(){

localStorage.clear();

window.location.href="login.html";

}




cargarPacientes();