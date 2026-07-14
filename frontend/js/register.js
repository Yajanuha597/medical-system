const API = "https://backmedicalsystem.byronrm.com";

document
.getElementById("registerForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const datos = {

        nombre:
        document
        .getElementById("nombre")
        .value,

        correo:
        document
        .getElementById("correo")
        .value,

        password:
        document
        .getElementById("password")
        .value,

        rol:
        document
        .getElementById("rol")
        .value

    };

    try{

        const respuesta = await fetch(

            API + "/usuarios/registro",

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify(datos)

            }

        );

        const resultado = await respuesta.json();

        alert(resultado.mensaje);

        if(respuesta.ok){

            window.location.href = "login.html";

        }

    }catch(error){

        console.error(error);

        alert("No se pudo conectar con el servidor.");

    }

});