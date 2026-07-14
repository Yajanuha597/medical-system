const API="http://localhost:5000";


function token(){

return localStorage.getItem("token");

}



async function cargarDoctores(){


const respuesta=await fetch(

API+"/doctores",

{

headers:{
"Authorization":"Bearer "+token()
}

}

);



const doctores=await respuesta.json();



const tabla=document.getElementById("tablaDoctores");


tabla.innerHTML="";



doctores.forEach(d=>{


tabla.innerHTML += `


<tr>

<td>${d.id}</td>

<td>${d.nombre}</td>

<td>${d.especialidad}</td>

<td>${d.correo}</td>

<td>${d.horario}</td>

<td>${d.estado}</td>


<td>


<button onclick="editarDoctor(${d.id})">
✏️
</button>


<button onclick="eliminarDoctor(${d.id})">
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

document.getElementById("idDoctor").value="";
document.getElementById("nombre").value="";
document.getElementById("especialidad").value="";
document.getElementById("correo").value="";
document.getElementById("telefono").value="";
document.getElementById("horario").value="";
document.getElementById("estado").value="";

}




async function guardarDoctor(){


const id=document.getElementById("idDoctor").value;



const datos={


nombre:
document.getElementById("nombre").value,


especialidad:
document.getElementById("especialidad").value,


correo:
document.getElementById("correo").value,


telefono:
document.getElementById("telefono").value,


horario:
document.getElementById("horario").value,


estado:
document.getElementById("estado").value


};



let url=API+"/doctores";

let metodo="POST";



if(id){

url+="/"+id;

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


}

);



cancelar();

cargarDoctores();


}





async function eliminarDoctor(id){


if(confirm("¿Eliminar doctor?")){


await fetch(

API+"/doctores/"+id,

{

method:"DELETE",

headers:{

"Authorization":"Bearer "+token()

}

}

);



cargarDoctores();


}


}





async function editarDoctor(id){



const respuesta=await fetch(

API+"/doctores/"+id,

{

headers:{

"Authorization":"Bearer "+token()

}

}

);



const d=await respuesta.json();



document.getElementById("idDoctor").value=d.id;

document.getElementById("nombre").value=d.nombre;

document.getElementById("especialidad").value=d.especialidad;

document.getElementById("correo").value=d.correo;

document.getElementById("telefono").value=d.telefono;

document.getElementById("horario").value=d.horario;

document.getElementById("estado").value=d.estado;



mostrarFormulario();


}




function cerrarSesion(){

localStorage.clear();

window.location.href="login.html";

}




cargarDoctores();