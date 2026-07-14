from functools import wraps

from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request


def token_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:

            verify_jwt_in_request()

            return func(*args, **kwargs)


        except Exception as e:

            return jsonify({
                "mensaje": "Token requerido o inválido",
                "error": str(e)
            }), 401


    return wrapper