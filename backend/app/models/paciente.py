from app.config.db import db


class Paciente(db.Model):

    __tablename__ = "pacientes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    cedula = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    edad = db.Column(
        db.Integer,
        nullable=False
    )

    telefono = db.Column(
        db.String(20),
        nullable=False
    )

    direccion = db.Column(
        db.String(200),
        nullable=True
    )

    # Relación con citas
    citas = db.relationship(
        "Cita",
        back_populates="paciente",
        cascade="all, delete-orphan"
    )