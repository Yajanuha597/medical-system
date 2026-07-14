from app.config.db import db


class Cita(db.Model):

    __tablename__ = "citas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey("pacientes.id"),
        nullable=False
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctores.id"),
        nullable=False
    )

    fecha = db.Column(
        db.Date,
        nullable=False
    )

    hora = db.Column(
        db.String(10),
        nullable=False
    )

    motivo = db.Column(
        db.String(200),
        nullable=True
    )

    estado = db.Column(
        db.String(20),
        default="Pendiente"
    )

    # Relación con Paciente
    paciente = db.relationship(
        "Paciente",
        back_populates="citas"
    )

    # Relación con Doctor
    doctor = db.relationship(
        "Doctor",
        back_populates="citas"
    )