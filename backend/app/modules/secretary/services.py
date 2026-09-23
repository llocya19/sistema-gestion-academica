from app.extensions.database import db

from app.modules.academic.models import (
    Persona,
    Estudiante,
    Docente
)
from app.modules.secretary.imports.excel import (
    leer_excel_estudiantes,
    leer_excel_docentes
)



# ==========================================================
# LISTAR ESTUDIANTES
# ==========================================================

def listar_estudiantes():

    estudiantes = Estudiante.query.all()

    resultado = []


    for estudiante in estudiantes:

        resultado.append({

            "id": estudiante.id,

            "codigo": estudiante.student_code,

            "estado": estudiante.status,

            "persona": {

                "dni": estudiante.persona.dni,

                "nombres": estudiante.persona.nombres,

                "apellidos": estudiante.persona.apellidos

            }

        })


    return resultado



# ==========================================================
# CREAR ESTUDIANTE
# ==========================================================

def crear_estudiante(data):


    # ======================================
    # VALIDAR DNI
    # ======================================

    persona_existente = Persona.query.filter_by(
        dni=data["dni"]
    ).first()


    if persona_existente:

        raise ValueError(
            "El DNI ya está registrado"
        )


    # ======================================
    # VALIDAR CODIGO ESTUDIANTE
    # ======================================

    estudiante_existente = Estudiante.query.filter_by(
        student_code=data["student_code"]
    ).first()


    if estudiante_existente:

        raise ValueError(
            "El código del estudiante ya existe"
        )


    # ======================================
    # CREAR PERSONA
    # ======================================

    persona = Persona(

        dni=data["dni"],

        nombres=data["nombres"],

        apellidos=data["apellidos"],

        telefono=data.get("telefono"),

        direccion=data.get("direccion")

    )


    db.session.add(persona)

    db.session.flush()



    # ======================================
    # CREAR ESTUDIANTE
    # ======================================

    estudiante = Estudiante(

        person_id=persona.id,

        student_code=data["student_code"],

        status=True

    )


    db.session.add(estudiante)

    db.session.commit()


    return estudiante

# ==========================================================
# ACTUALIZAR ESTUDIANTE
# ==========================================================

def actualizar_estudiante(estudiante_id, data):


    estudiante = Estudiante.query.get(
        estudiante_id
    )


    if not estudiante:

        raise ValueError(
            "El estudiante no existe"
        )


    # ======================================
    # ACTUALIZAR DATOS PERSONALES
    # ======================================

    persona = estudiante.persona


    if "nombres" in data:

        persona.nombres = data["nombres"]


    if "apellidos" in data:

        persona.apellidos = data["apellidos"]


    if "telefono" in data:

        persona.telefono = data["telefono"]


    if "direccion" in data:

        persona.direccion = data["direccion"]



    # ======================================
    # ACTUALIZAR CODIGO ESTUDIANTE
    # ======================================

    if "student_code" in data:


        codigo_existente = Estudiante.query.filter(
            Estudiante.student_code == data["student_code"],
            Estudiante.id != estudiante_id
        ).first()


        if codigo_existente:

            raise ValueError(
                "El código del estudiante ya existe"
            )


        estudiante.student_code = data["student_code"]



    db.session.commit()


    return estudiante
# ==========================================================
# CAMBIAR ESTADO ESTUDIANTE
# ==========================================================

def cambiar_estado_estudiante(estudiante_id, estado):


    estudiante = Estudiante.query.get(
        estudiante_id
    )


    if not estudiante:

        raise ValueError(
            "El estudiante no existe"
        )


    estudiante.status = estado


    db.session.commit()


    return estudiante

# ==========================================================
# IMPORTAR ESTUDIANTES DESDE EXCEL
# ==========================================================

def importar_estudiantes_excel(archivo):


    estudiantes_excel = leer_excel_estudiantes(
        archivo
    )


    creados = 0

    errores = []


    for indice, data in enumerate(
        estudiantes_excel,
        start=2
    ):


        try:

            crear_estudiante(
                data
            )


            creados += 1



        except ValueError as error:


            errores.append({

                "fila": indice,

                "error": str(error)

            })



    return {

        "creados": creados,

        "errores": errores

    }

# ==========================================================
# LISTAR DOCENTES
# ==========================================================

def listar_docentes():

    docentes = Docente.query.all()

    resultado = []


    for docente in docentes:

        resultado.append({

            "id": docente.id,

            "codigo": docente.teacher_code,

            "estado": docente.status,

            "persona": {

                "dni": docente.persona.dni,

                "nombres": docente.persona.nombres,

                "apellidos": docente.persona.apellidos

            }

        })


    return resultado
# ==========================================================
# CREAR DOCENTE
# ==========================================================

def crear_docente(data):


    persona_existente = Persona.query.filter_by(
        dni=data["dni"]
    ).first()


    if persona_existente:

        raise ValueError(
            "El DNI ya está registrado"
        )



    docente_existente = Docente.query.filter_by(
        teacher_code=data["teacher_code"]
    ).first()


    if docente_existente:

        raise ValueError(
            "El código del docente ya existe"
        )



    persona = Persona(

        dni=data["dni"],

        nombres=data["nombres"],

        apellidos=data["apellidos"],

        telefono=data.get("telefono"),

        direccion=data.get("direccion")

    )


    db.session.add(persona)

    db.session.flush()



    docente = Docente(

        person_id=persona.id,

        teacher_code=data["teacher_code"],

        status=True

    )


    db.session.add(docente)

    db.session.commit()


    return docente
# ==========================================================
# ACTUALIZAR DOCENTE
# ==========================================================

def actualizar_docente(docente_id, data):


    docente = Docente.query.get(
        docente_id
    )


    if not docente:

        raise ValueError(
            "El docente no existe"
        )


    persona = docente.persona


    if "nombres" in data:

        persona.nombres = data["nombres"]


    if "apellidos" in data:

        persona.apellidos = data["apellidos"]


    if "telefono" in data:

        persona.telefono = data["telefono"]


    if "direccion" in data:

        persona.direccion = data["direccion"]



    if "teacher_code" in data:


        codigo_existente = Docente.query.filter(
            Docente.teacher_code == data["teacher_code"],
            Docente.id != docente_id
        ).first()


        if codigo_existente:

            raise ValueError(
                "El código del docente ya existe"
            )


        docente.teacher_code = data["teacher_code"]



    db.session.commit()


    return docente

# ==========================================================
# CAMBIAR ESTADO DOCENTE
# ==========================================================

def cambiar_estado_docente(docente_id, estado):


    docente = Docente.query.get(
        docente_id
    )


    if not docente:

        raise ValueError(
            "El docente no existe"
        )


    docente.status = estado


    db.session.commit()


    return docente
# ==========================================================
# IMPORTAR DOCENTES DESDE EXCEL
# ==========================================================

def importar_docentes_excel(archivo):


    docentes_excel = leer_excel_docentes(
        archivo
    )


    creados = 0

    errores = []


    for indice, data in enumerate(
        docentes_excel,
        start=2
    ):


        try:

            crear_docente(
                data
            )

            creados += 1



        except ValueError as error:


            errores.append({

                "fila": indice,

                "error": str(error)

            })


    return {

        "creados": creados,

        "errores": errores

    }