document
.getElementById("loginForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const correo =
    document
    .getElementById("correo")
    .value;

    const password =
    document
    .getElementById("password")
    .value;


    try{

        const respuesta =
        await postData(
            "/usuarios/login",
            {
                correo: correo,
                password: password
            }
        );


        if(respuesta.token){

            localStorage.setItem(
                "token",
                respuesta.token
            );

            localStorage.setItem(
                "usuario",
                JSON.stringify(
                    respuesta.usuario
                )
            );

            window.location.href =
            "dashboard.html";

        }else{

            alert(
                respuesta.mensaje
            );

        }

    }catch(error){

        console.error(error);

        alert(
            "No se pudo conectar con el servidor."
        );

    }

});