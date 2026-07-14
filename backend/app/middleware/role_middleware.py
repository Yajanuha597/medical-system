from functools import wraps

from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def role_required(role):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            try:

                verify_jwt_in_request()

                claims = get_jwt()

                user_role = claims.get("rol")

                if user_role != role:
                    return jsonify({
                        "mensaje": "No tiene permisos para acceder a este recurso"
                    }), 403

                return func(*args, **kwargs)

            except Exception as e:

                return jsonify({
                    "mensaje": "Token inválido",
                    "error": str(e)
                }), 401

        return wrapper

    return decorator
