from flask import Blueprint, request, jsonify

from app.config.db import db
from app.models.doctor import Doctor

from app.middleware.auth_middleware import token_required



doctor_bp = Blueprint(
    "doctores",
    __name__,
    url_prefix="/doctores"
)



# =====================================
# CREAR DOCTOR
# =====================================

@doctor_bp.route("", methods=["POST"])
@token_required
def crear_doctor():

    data = request.json


    nuevo_doctor = Doctor(

        nombre=data["nombre"],

        especialidad=data["especialidad"],

        correo=data["correo"],

        telefono=data["telefono"],

        horario=data["horario"],

        estado=data.get(
            "estado",
            "Activo"
        )

    )


    db.session.add(nuevo_doctor)

    db.session.commit()


    return jsonify({

        "mensaje": "Doctor creado correctamente",

        "doctor": {

            "id": nuevo_doctor.id,

            "nombre": nuevo_doctor.nombre,

            "especialidad": nuevo_doctor.especialidad,

            "correo": nuevo_doctor.correo,

            "telefono": nuevo_doctor.telefono,

            "horario": nuevo_doctor.horario,

            "estado": nuevo_doctor.estado

        }

    }), 201





# =====================================
# LISTAR DOCTORES
# =====================================

@doctor_bp.route("", methods=["GET"])
@token_required
def listar_doctores():


    doctores = Doctor.query.all()


    resultado = []


    for doctor in doctores:

        resultado.append({

            "id": doctor.id,

            "nombre": doctor.nombre,

            "especialidad": doctor.especialidad,

            "correo": doctor.correo,

            "telefono": doctor.telefono,

            "horario": doctor.horario,

            "estado": doctor.estado

        })


    return jsonify(resultado)





# =====================================
# BUSCAR DOCTOR POR ID
# =====================================

@doctor_bp.route("/<int:id>", methods=["GET"])
@token_required
def obtener_doctor(id):


    doctor = Doctor.query.get(id)


    if not doctor:

        return jsonify({

            "mensaje": "Doctor no encontrado"

        }),404



    return jsonify({

        "id": doctor.id,

        "nombre": doctor.nombre,

        "especialidad": doctor.especialidad,

        "correo": doctor.correo,

        "telefono": doctor.telefono,

        "horario": doctor.horario,

        "estado": doctor.estado

    })





# =====================================
# ACTUALIZAR DOCTOR
# =====================================

@doctor_bp.route("/<int:id>", methods=["PUT"])
@token_required
def actualizar_doctor(id):


    doctor = Doctor.query.get(id)


    if not doctor:

        return jsonify({

            "mensaje": "Doctor no encontrado"

        }),404



    data = request.json


    doctor.nombre = data.get(
        "nombre",
        doctor.nombre
    )


    doctor.especialidad = data.get(
        "especialidad",
        doctor.especialidad
    )


    doctor.telefono = data.get(
        "telefono",
        doctor.telefono
    )


    doctor.horario = data.get(
        "horario",
        doctor.horario
    )


    doctor.estado = data.get(
        "estado",
        doctor.estado
    )



    db.session.commit()


    return jsonify({

        "mensaje": "Doctor actualizado correctamente"

    })





# =====================================
# ELIMINAR DOCTOR
# =====================================

@doctor_bp.route("/<int:id>", methods=["DELETE"])
@token_required
def eliminar_doctor(id):


    doctor = Doctor.query.get(id)


    if not doctor:

        return jsonify({

            "mensaje": "Doctor no encontrado"

        }),404



    db.session.delete(doctor)

    db.session.commit()



    return jsonify({

        "mensaje": "Doctor eliminado correctamente"

    })