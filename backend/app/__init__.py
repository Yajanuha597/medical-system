from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from datetime import timedelta

from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from app.config.db import db

load_dotenv()

# ==========================
# EXTENSIONES
# ==========================

migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()

# ==========================
# CREAR APLICACION
# ==========================

def create_app():

    app = Flask(__name__)

    # ==========================
    # CONFIGURACION DATABASE
    # ==========================

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ==========================
    # CONFIGURACION JWT
    # ==========================

    app.config["JWT_SECRET_KEY"] = "medical-system-secret-key"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

    # ==========================
    # INICIALIZAR EXTENSIONES
    # ==========================

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # ==========================
    # IMPORTAR MODELOS
    # ==========================

    from app.models.usuario import Usuario
    from app.models.paciente import Paciente
    from app.models.doctor import Doctor
    from app.models.cita import Cita

    # ==========================
    # REGISTRAR RUTAS
    # ==========================

    from app.routes.usuario_routes import usuario_bp
    from app.routes.paciente_routes import paciente_bp
    from app.routes.doctor_routes import doctor_bp
    from app.routes.cita_routes import cita_bp

    app.register_blueprint(usuario_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(cita_bp)

    # ==========================
    # RUTA PRINCIPAL
    # ==========================

    @app.route("/")
    def home():
        return {
            "mensaje": "Bienvenido a Medical System API",
            "version": "1.0.0"
        }

    return app