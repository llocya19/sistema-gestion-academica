from flask_jwt_extended import JWTManager
from flask import jsonify


jwt = JWTManager()



@jwt.expired_token_loader
def token_expirado(jwt_header, jwt_payload):

    return jsonify({

        "mensaje":
        "La sesión ha expirado, vuelva a iniciar sesión"

    }),401



@jwt.invalid_token_loader
def token_invalido(error):

    return jsonify({

        "mensaje":
        "Token inválido"

    }),401



@jwt.unauthorized_loader
def falta_token(error):

    return jsonify({

        "mensaje":
        "Debe iniciar sesión"

    }),401
@jwt.needs_fresh_token_loader
def token_no_fresco(jwt_header, jwt_payload):

    return jsonify({

        "mensaje":
        "Debe volver a autenticarse"

    }),401
@jwt.revoked_token_loader
def token_revocado(jwt_header, jwt_payload):

    return jsonify({

        "mensaje":
        "Token revocado"

    }),401