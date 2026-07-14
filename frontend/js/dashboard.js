const usuario = JSON.parse(
localStorage.getItem("usuario")
);


if(usuario){

document.getElementById("usuario").innerHTML =
`
Nombre: ${usuario.nombre}<br>
Correo: ${usuario.correo}<br>
Rol: ${usuario.rol}
`;

}



function cerrarSesion(){

localStorage.clear();

window.location.href="login.html";

}