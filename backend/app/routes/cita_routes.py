from flask import Blueprint, request, jsonify

from app.config.db import db
from app.models.cita import Cita
from app.models.paciente import Paciente
from app.models.doctor import Doctor

from app.middleware.auth_middleware import token_required


cita_bp = Blueprint(
    "citas",
    __name__,
    url_prefix="/citas"
)


# =====================================
# CREAR CITA
# =====================================

@cita_bp.route("", methods=["POST"])
@token_required
def crear_cita():

    try:

        data = request.get_json()

        nueva_cita = Cita(

            paciente_id=data["paciente_id"],
            doctor_id=data["doctor_id"],
            fecha=data["fecha"],
            hora=data["hora"],
            motivo=data.get("motivo"),
            estado="Pendiente"

        )

        db.session.add(nueva_cita)
        db.session.commit()

        return jsonify({

            "mensaje": "Cita creada correctamente",

            "cita": {

                "id": nueva_cita.id,

                "paciente_id": nueva_cita.paciente_id,
                "paciente": nueva_cita.paciente.nombre,

                "doctor_id": nueva_cita.doctor_id,
                "doctor": nueva_cita.doctor.nombre,

                "fecha": str(nueva_cita.fecha),
                "hora": nueva_cita.hora,
                "motivo": nueva_cita.motivo,
                "estado": nueva_cita.estado

            }

        }), 201

    except Exception as e:

        db.session.rollback()

        return jsonify({

            "mensaje": "Error al crear la cita",
            "error": str(e)

        }), 500


# =====================================
# LISTAR TODAS LAS CITAS
# =====================================

@cita_bp.route("", methods=["GET"])
@token_required
def listar_citas():

    citas = Cita.query.all()

    resultado = []

    for cita in citas:

        resultado.append({

            "id": cita.id,

            "paciente_id": cita.paciente_id,
            "paciente": cita.paciente.nombre,

            "doctor_id": cita.doctor_id,
            "doctor": cita.doctor.nombre,

            "fecha": str(cita.fecha),
            "hora": cita.hora,
            "motivo": cita.motivo,
            "estado": cita.estado

        })

    return jsonify(resultado)


# =====================================
# BUSCAR CITA POR ID
# =====================================

@cita_bp.route("/<int:id>", methods=["GET"])
@token_required
def obtener_cita(id):

    cita = Cita.query.get(id)

    if cita is None:

        return jsonify({

            "mensaje": "Cita no encontrada"

        }), 404

    return jsonify({

        "id": cita.id,

        "paciente_id": cita.paciente_id,
        "paciente": cita.paciente.nombre,

        "doctor_id": cita.doctor_id,
        "doctor": cita.doctor.nombre,

        "fecha": str(cita.fecha),
        "hora": cita.hora,
        "motivo": cita.motivo,
        "estado": cita.estado

    })


# =====================================
# ACTUALIZAR CITA
# =====================================

@cita_bp.route("/<int:id>", methods=["PUT"])
@token_required
def actualizar_cita(id):

    cita = Cita.query.get(id)

    if cita is None:

        return jsonify({
            "mensaje": "Cita no encontrada"
        }), 404

    data = request.get_json()

    cita.paciente_id = data.get("paciente_id", cita.paciente_id)
    cita.doctor_id = data.get("doctor_id", cita.doctor_id)
    cita.fecha = data.get("fecha", cita.fecha)
    cita.hora = data.get("hora", cita.hora)
    cita.motivo = data.get("motivo", cita.motivo)
    cita.estado = data.get("estado", cita.estado)

    db.session.commit()

    return jsonify({

        "mensaje": "Cita actualizada correctamente",

        "cita": {

            "id": cita.id,

            "paciente_id": cita.paciente_id,
            "paciente": cita.paciente.nombre,

            "doctor_id": cita.doctor_id,
            "doctor": cita.doctor.nombre,

            "fecha": str(cita.fecha),
            "hora": cita.hora,
            "motivo": cita.motivo,
            "estado": cita.estado

        }

    })


# =====================================
# ELIMINAR CITA
# =====================================

@cita_bp.route("/<int:id>", methods=["DELETE"])
@token_required
def eliminar_cita(id):

    cita = Cita.query.get(id)

    if cita is None:

        return jsonify({
            "mensaje": "Cita no encontrada"
        }), 404

    db.session.delete(cita)
    db.session.commit()

    return jsonify({
        "mensaje": "Cita eliminada correctamente"
    })