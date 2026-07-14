const API_URL = "http://localhost:5000";

async function postData(endpoint, data) {

    const respuesta = await fetch(API_URL + endpoint, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    });

    return await respuesta.json();

}