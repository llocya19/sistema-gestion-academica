import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
from app import create_app

from app.extensions.database import db

from app.modules.auth.models import Permiso


app = create_app()


permisos = [

    {
        "name": "GESTIONAR_USUARIOS",
        "description":
        "Crear, actualizar y administrar usuarios"
    },

    {
        "name": "GESTIONAR_ROLES",
        "description":
        "Administrar roles del sistema"
    },

    {
        "name": "GESTIONAR_PERMISOS",
        "description":
        "Administrar permisos del sistema"
    },

    {
        "name": "VER_INDICADORES",
        "description":
        "Consultar indicadores académicos"
    },

    {
        "name": "VER_REPORTES",
        "description":
        "Consultar reportes institucionales"
    },

    {
        "name": "GESTIONAR_ESTUDIANTES",
        "description":
        "Administrar estudiantes"
    },

    {
        "name": "GESTIONAR_DOCENTES",
        "description":
        "Administrar docentes"
    },

    {
        "name": "GESTIONAR_MATRICULAS",
        "description":
        "Administrar matrículas académicas"
    },

    {
        "name": "REGISTRAR_SESIONES",
        "description":
        "Registrar sesiones de clase"
    },

    {
        "name": "REGISTRAR_NOTAS",
        "description":
        "Registrar calificaciones"
    },

    {
        "name": "REGISTRAR_ASISTENCIA",
        "description":
        "Registrar asistencia"
    }

]


with app.app_context():


    for permiso_data in permisos:


        existe = Permiso.query.filter_by(
            name=permiso_data["name"]
        ).first()


        if not existe:


            permiso = Permiso(

                name=permiso_data["name"],

                description=permiso_data["description"]

            )


            db.session.add(permiso)



    db.session.commit()


    print(
        "Permisos creados correctamente"
    )