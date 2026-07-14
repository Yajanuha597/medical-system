const API="https://backmedicalsystem.byronrm.com";


function obtenerToken(){

    return localStorage.getItem("token");

}



// ==========================
// CARGAR PACIENTES Y DOCTORES
// ==========================

async function cargarSelects(){


    const pacientes = await fetch(
        API+"/pacientes",
        {
            headers:{
                "Authorization":
                "Bearer "+obtenerToken()
            }
        }
    );


    const listaPacientes =
    await pacientes.json();



    const selectPaciente =
    document.getElementById("paciente_id");



    listaPacientes.forEach(p=>{


        selectPaciente.innerHTML += `

        <option value="${p.id}">
        ${p.nombre}
        </option>

        `;


    });




    const doctores = await fetch(
        API+"/doctores",
        {
            headers:{
                "Authorization":
                "Bearer "+obtenerToken()
            }
        }
    );



    const listaDoctores =
    await doctores.json();



    const selectDoctor =
    document.getElementById("doctor_id");



    listaDoctores.forEach(d=>{


        selectDoctor.innerHTML += `


        <option value="${d.id}">
        ${d.nombre}
        </option>


        `;


    });



}




// ==========================
// LISTAR CITAS
// ==========================

async function cargarCitas(){


const respuesta =
await fetch(

API+"/citas",

{

headers:{

"Authorization":
"Bearer "+obtenerToken()

}

}

);



const citas =
await respuesta.json();



const tabla =
document.getElementById("tablaCitas");



tabla.innerHTML="";



citas.forEach(c=>{


tabla.innerHTML += `


<tr>

<td>${c.id}</td>

<td>${c.paciente}</td>

<td>${c.doctor}</td>

<td>${c.fecha}</td>

<td>${c.hora}</td>

<td>${c.motivo || ""}</td>

<td>${c.estado}</td>


<td>


<button onclick="editarCita(${c.id})">
✏️
</button>


<button onclick="eliminarCita(${c.id})">
🗑️
</button>


</td>


</tr>


`;

});


}





// ==========================
// MOSTRAR FORMULARIO
// ==========================

function mostrarFormulario(){

document.getElementById("formulario")
.style.display="block";

}




function cancelar(){

document.getElementById("formulario")
.style.display="none";


limpiar();


}



function limpiar(){

document.getElementById("idCita").value="";

document.getElementById("fecha").value="";

document.getElementById("hora").value="";

document.getElementById("motivo").value="";


}





// ==========================
// GUARDAR / ACTUALIZAR
// ==========================

async function guardarCita(){



const id =
document.getElementById("idCita").value;



const datos={


paciente_id:
Number(
document.getElementById("paciente_id").value
),


doctor_id:
Number(
document.getElementById("doctor_id").value
),


fecha:
document.getElementById("fecha").value,


hora:
document.getElementById("hora").value,


motivo:
document.getElementById("motivo").value,


estado:
document.getElementById("estado").value


};



let url =
API+"/citas";


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


"Content-Type":
"application/json",


"Authorization":
"Bearer "+obtenerToken()


},


body:
JSON.stringify(datos)


}

);



cancelar();

cargarCitas();


}






// ==========================
// EDITAR
// ==========================

async function editarCita(id){


const respuesta =
await fetch(

API+"/citas/"+id,

{

headers:{

"Authorization":
"Bearer "+obtenerToken()

}

}

);



const c =
await respuesta.json();



document.getElementById("idCita").value=c.id;


document.getElementById("paciente_id").value=c.paciente_id;


document.getElementById("doctor_id").value=c.doctor_id;


document.getElementById("fecha").value=c.fecha;


document.getElementById("hora").value=c.hora;


document.getElementById("motivo").value=c.motivo;


document.getElementById("estado").value=c.estado;



mostrarFormulario();


}





// ==========================
// ELIMINAR
// ==========================

async function eliminarCita(id){


if(confirm("¿Eliminar cita?")){


await fetch(

API+"/citas/"+id,

{

method:"DELETE",


headers:{


"Authorization":
"Bearer "+obtenerToken()


}


}

);



cargarCitas();


}


}





function cerrarSesion(){

localStorage.clear();

window.location.href="login.html";

}





cargarSelects();

cargarCitas();