from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    create_access_token
)

from app.config.db import db
from app.models.usuario import Usuario
from app import bcrypt

from app.middleware.auth_middleware import token_required
from app.middleware.role_middleware import role_required


usuario_bp = Blueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios"
)



# ===============================
# REGISTRO
# ===============================

@usuario_bp.route("/registro", methods=["POST"])
@role_required("admin")
def registro():
    data = request.json


    password_hash = bcrypt.generate_password_hash(
        data["password"]
    ).decode("utf-8")


    nuevo_usuario = Usuario(

        nombre=data["nombre"],

        correo=data["correo"],

        password_hash=password_hash,

        rol=data.get(
            "rol",
            "usuario"
        )

    )


    db.session.add(nuevo_usuario)

    db.session.commit()


    return jsonify({

        "mensaje": "Usuario registrado correctamente",

        "usuario": {

            "id": nuevo_usuario.id,

            "nombre": nuevo_usuario.nombre,

            "correo": nuevo_usuario.correo,

            "rol": nuevo_usuario.rol

        }

    })



# ===============================
# LOGIN
# ===============================

@usuario_bp.route("/login", methods=["POST"])
def login():


    data = request.json


    usuario = Usuario.query.filter_by(
        correo=data["correo"]
    ).first()



    if not usuario:

        return jsonify({

            "mensaje": "Usuario no encontrado"

        }),404



    if not bcrypt.check_password_hash(

        usuario.password_hash,

        data["password"]

    ):


        return jsonify({

            "mensaje": "Contraseña incorrecta"

        }),401




    token = create_access_token(

        identity=str(usuario.id),

        additional_claims={

            "rol": usuario.rol,

            "nombre": usuario.nombre,

            "correo": usuario.correo

        }

    )



    return jsonify({

        "mensaje": "Login correcto",

        "token": token,


        "usuario": {

            "id": usuario.id,

            "nombre": usuario.nombre,

            "correo": usuario.correo,

            "rol": usuario.rol

        }

    })





# ===============================
# PERFIL PROTEGIDO JWT
# ===============================


@usuario_bp.route("/perfil", methods=["GET"])
@token_required
def perfil():


    return jsonify({

        "mensaje": "Acceso autorizado con JWT"

    })
