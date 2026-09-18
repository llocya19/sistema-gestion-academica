from datetime import datetime

from app.extensions.database import db



# ==========================================================
# TABLA: roles
# ==========================================================

class Rol(db.Model):

    __tablename__ = "roles"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )


    description = db.Column(
        db.String(200)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ==========================================================
# TABLA: permissions
# ==========================================================

class Permiso(db.Model):

    __tablename__ = "permissions"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )


    description = db.Column(
        db.String(200)
    )



# ==========================================================
# TABLA: role_permissions
# ==========================================================

class RolPermiso(db.Model):

    __tablename__ = "role_permissions"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False
    )


    permission_id = db.Column(
        db.Integer,
        db.ForeignKey("permissions.id"),
        nullable=False
    )


    rol = db.relationship(
        "Rol",
        backref="permisos"
    )


    permiso = db.relationship(
        "Permiso",
        backref="roles"
    )



# ==========================================================
# TABLA: users
#
# Solo autenticación
#
# Los datos personales están en Persona
#
# ==========================================================

class Usuario(db.Model):

    __tablename__ = "users"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    persona_id = db.Column(
        db.Integer,
        db.ForeignKey("persons.id"),
        nullable=False
    )


    email = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )


    password_hash = db.Column(
        db.String(255),
        nullable=False
    )


    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False
    )


    status = db.Column(
        db.Boolean,
        default=True
    )


    last_login = db.Column(
        db.DateTime
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    updated_at = db.Column(
        db.DateTime,
        onupdate=datetime.utcnow
    )


    persona = db.relationship(
    "Persona",
        back_populates="usuario",
        uselist=False
    )


    rol = db.relationship(
        "Rol",
        backref="usuarios"
    )