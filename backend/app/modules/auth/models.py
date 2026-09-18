from datetime import datetime

from app.extensions.database import db



# ==========================================================
# TABLA: roles
#
# Define los tipos de usuario del sistema
#
# Ejemplo:
# ADMINISTRADOR
# DIRECTORA
# DOCENTE
# ESTUDIANTE
#
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
# TABLA: permisos
#
# Permisos del sistema
#
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
# TABLA: rol_permisos
#
# Relación N:M entre roles y permisos
#
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
        backref="permisos_asignados"
    )


    permiso = db.relationship(
        "Permiso",
        backref="roles_asignados"
    )



# ==========================================================
# TABLA: usuarios
#
# Maneja únicamente autenticación.
#
# Los datos personales están en PERSONAS.
#
# ==========================================================


class Usuario(db.Model):

    __tablename__ = "users"


    id = db.Column(
        db.Integer,
        primary_key=True
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


    rol = db.relationship(
        "Rol",
        backref="usuarios"
    )