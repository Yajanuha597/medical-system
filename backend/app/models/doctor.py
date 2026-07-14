from app.config.db import db


class Doctor(db.Model):

    __tablename__ = "doctores"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    especialidad = db.Column(
        db.String(100),
        nullable=False
    )

    correo = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    telefono = db.Column(
        db.String(20),
        nullable=False
    )

    horario = db.Column(
        db.String(100),
        nullable=False
    )

    estado = db.Column(
        db.String(20),
        default="Activo"
    )

    # Relación con citas
    citas = db.relationship(
        "Cita",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )