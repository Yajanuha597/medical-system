from flask import Blueprint, request, jsonify

from app.config.db import db
from app.models.paciente import Paciente

from app.middleware.auth_middleware import token_required


paciente_bp = Blueprint(
    "pacientes",
    __name__,
    url_prefix="/pacientes"
)


# =====================================
# CREAR PACIENTE
# =====================================

@paciente_bp.route("", methods=["POST"])
@token_required
def crear_paciente():

    data = request.json


    nuevo_paciente = Paciente(

        nombre=data["nombre"],

        cedula=data["cedula"],

        edad=data["edad"],

        telefono=data["telefono"],

        direccion=data.get("direccion")

    )


    db.session.add(nuevo_paciente)

    db.session.commit()


    return jsonify({

        "mensaje": "Paciente creado correctamente",

        "paciente": {

            "id": nuevo_paciente.id,

            "nombre": nuevo_paciente.nombre,

            "cedula": nuevo_paciente.cedula,

            "edad": nuevo_paciente.edad,

            "telefono": nuevo_paciente.telefono,

            "direccion": nuevo_paciente.direccion

        }

    }), 201



# =====================================
# LISTAR PACIENTES
# =====================================

@paciente_bp.route("", methods=["GET"])
@token_required
def listar_pacientes():


    pacientes = Paciente.query.all()


    resultado = []


    for paciente in pacientes:

        resultado.append({

            "id": paciente.id,

            "nombre": paciente.nombre,

            "cedula": paciente.cedula,

            "edad": paciente.edad,

            "telefono": paciente.telefono,

            "direccion": paciente.direccion

        })


    return jsonify(resultado)



# =====================================
# BUSCAR PACIENTE POR ID
# =====================================

@paciente_bp.route("/<int:id>", methods=["GET"])
@token_required
def obtener_paciente(id):


    paciente = Paciente.query.get(id)


    if not paciente:

        return jsonify({

            "mensaje": "Paciente no encontrado"

        }),404



    return jsonify({

        "id": paciente.id,

        "nombre": paciente.nombre,

        "cedula": paciente.cedula,

        "edad": paciente.edad,

        "telefono": paciente.telefono,

        "direccion": paciente.direccion

    })



# =====================================
# ACTUALIZAR PACIENTE
# =====================================

@paciente_bp.route("/<int:id>", methods=["PUT"])
@token_required
def actualizar_paciente(id):


    paciente = Paciente.query.get(id)


    if not paciente:

        return jsonify({

            "mensaje": "Paciente no encontrado"

        }),404



    data = request.json


    paciente.nombre = data.get(
        "nombre",
        paciente.nombre
    )

    paciente.edad = data.get(
        "edad",
        paciente.edad
    )

    paciente.telefono = data.get(
        "telefono",
        paciente.telefono
    )

    paciente.direccion = data.get(
        "direccion",
        paciente.direccion
    )


    db.session.commit()


    return jsonify({

        "mensaje": "Paciente actualizado correctamente"

    })



# =====================================
# ELIMINAR PACIENTE
# =====================================

@paciente_bp.route("/<int:id>", methods=["DELETE"])
@token_required
def eliminar_paciente(id):


    paciente = Paciente.query.get(id)


    if not paciente:

        return jsonify({

            "mensaje": "Paciente no encontrado"

        }),404



    db.session.delete(paciente)

    db.session.commit()


    return jsonify({

        "mensaje": "Paciente eliminado correctamente"

    })