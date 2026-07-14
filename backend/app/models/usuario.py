from app.config.db import db


class Usuario(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    correo = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
    db.String(255),
    nullable=False
)
    

    rol = db.Column(
        db.String(50),
        default="paciente"
    )


    def __repr__(self):
        return f"<Usuario {self.nombre}>"