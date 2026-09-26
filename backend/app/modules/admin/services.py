from werkzeug.security import generate_password_hash

from app.extensions.database import db

from app.modules.auth.models import (
    Usuario,
    Rol,
    Permiso,
    RolPermiso
)

from app.modules.academic.models import Persona



# ==========================================================
# LISTAR USUARIOS
# ==========================================================

def listar_usuarios():

    usuarios = Usuario.query.all()

    resultado = []


    for usuario in usuarios:

        resultado.append({

            "id": usuario.id,

            "email": usuario.email,

            "estado": usuario.status,

            "rol": usuario.rol.name,

            "persona": {

                "dni": usuario.persona.dni,

                "nombres": usuario.persona.nombres,

                "apellidos": usuario.persona.apellidos

            }

        })


    return resultado





# ==========================================================
# CREAR USUARIO
# ==========================================================

def crear_usuario(data):


    # ======================================
    # VALIDAR DATOS OBLIGATORIOS
    # ======================================

    campos_obligatorios = [

        "email",
        "password",
        "dni",
        "nombres",
        "apellidos",
        "role_id"

    ]


    for campo in campos_obligatorios:


        if campo not in data or not str(data[campo]).strip():


            raise ValueError(

                f"El campo {campo} es obligatorio"

            )



    # ======================================
    # LIMPIAR DATOS
    # ======================================

    email = data["email"].strip().lower()

    dni = data["dni"].strip()

    nombres = data["nombres"].strip()

    apellidos = data["apellidos"].strip()

    password = data["password"].strip()



    # ======================================
    # VALIDAR PASSWORD
    # ======================================

    if len(password) < 8:

        raise ValueError(

            "La contraseña debe tener mínimo 8 caracteres"

        )



    # ======================================
    # VALIDAR DNI
    # ======================================

    if not dni.isdigit():

        raise ValueError(

            "El DNI solo debe contener números"

        )


    if len(dni) != 8:

        raise ValueError(

            "El DNI debe tener 8 dígitos"

        )



    # ======================================
    # VALIDAR EMAIL DUPLICADO
    # ======================================

    usuario_existente = Usuario.query.filter_by(

        email=email

    ).first()


    if usuario_existente:

        raise ValueError(

            "El correo ya está registrado"

        )



    # ======================================
    # VALIDAR DNI DUPLICADO
    # ======================================

    persona_existente = Persona.query.filter_by(

        dni=dni

    ).first()


    if persona_existente:

        raise ValueError(

            "El DNI ya está registrado"

        )



    # ======================================
    # VALIDAR ROL
    # ======================================

    rol = Rol.query.get(

        data["role_id"]

    )


    if not rol:

        raise ValueError(

            "El rol seleccionado no existe"

        )



    # ======================================
    # CREAR PERSONA
    # ======================================

    persona = Persona(

        dni=dni,

        nombres=nombres,

        apellidos=apellidos,

        telefono=data.get("telefono"),

        direccion=data.get("direccion")

    )


    db.session.add(persona)

    db.session.flush()



    # ======================================
    # CREAR USUARIO
    # ======================================

    usuario = Usuario(

        persona_id=persona.id,

        email=email,

        password_hash=generate_password_hash(

            password

        ),

        role_id=rol.id,

        status=True

    )


    db.session.add(usuario)

    db.session.commit()



    return usuario





# ==========================================================
# ACTUALIZAR USUARIO
# ==========================================================

def actualizar_usuario(usuario_id, data):


    usuario = Usuario.query.get(usuario_id)


    if not usuario:

        raise ValueError(

            "El usuario no existe"

        )



    # Validar correo si cambia

    if "email" in data:


        correo = Usuario.query.filter(

            Usuario.email == data["email"],

            Usuario.id != usuario_id

        ).first()



        if correo:

            raise ValueError(

                "El correo ya está registrado"

            )


        usuario.email = data["email"]




    # Actualizar persona

    persona = usuario.persona



    if "nombres" in data:

        persona.nombres = data["nombres"]



    if "apellidos" in data:

        persona.apellidos = data["apellidos"]



    if "telefono" in data:

        persona.telefono = data["telefono"]



    if "direccion" in data:

        persona.direccion = data["direccion"]




    # Actualizar rol

    if "role_id" in data:


        rol = Rol.query.get(

            data["role_id"]

        )


        if not rol:

            raise ValueError(

                "El rol seleccionado no existe"

            )


        usuario.role_id = rol.id




    db.session.commit()


    return usuario





# ==========================================================
# CAMBIAR ESTADO USUARIO
# ==========================================================

def cambiar_estado_usuario(usuario_id, estado):


    usuario = Usuario.query.get(usuario_id)



    if not usuario:

        raise ValueError(

            "El usuario no existe"

        )



    if not isinstance(estado, bool):

        raise ValueError(

            "El estado debe ser verdadero o falso"

        )



    usuario.status = estado


    db.session.commit()


    return usuario





# ==========================================================
# LISTAR ROLES
# ==========================================================

def listar_roles():


    roles = Rol.query.all()


    resultado = []


    for rol in roles:


        resultado.append({

            "id": rol.id,

            "nombre": rol.name,

            "descripcion": rol.description

        })


    return resultado





# ==========================================================
# LISTAR PERMISOS
# ==========================================================

def listar_permisos():


    permisos = Permiso.query.all()


    resultado = []


    for permiso in permisos:


        resultado.append({

            "id": permiso.id,

            "nombre": permiso.name,

            "descripcion": permiso.description

        })


    return resultado





# ==========================================================
# ASIGNAR PERMISOS A ROL
# ==========================================================

def asignar_permisos_rol(role_id, permisos_ids):


    rol = Rol.query.get(role_id)



    if not rol:

        raise ValueError(

            "El rol no existe"

        )



    RolPermiso.query.filter_by(

        role_id=role_id

    ).delete()



    for permiso_id in permisos_ids:


        permiso = Permiso.query.get(

            permiso_id

        )


        if not permiso:

            raise ValueError(

                f"El permiso {permiso_id} no existe"

            )



        relacion = RolPermiso(

            role_id=role_id,

            permission_id=permiso_id

        )


        db.session.add(relacion)




    db.session.commit()



    return rol





# ==========================================================
# OBTENER PERMISOS DE UN ROL
# ==========================================================

def obtener_permisos_rol(role_id):


    rol = Rol.query.get(role_id)



    if not rol:

        raise ValueError(

            "El rol no existe"

        )



    permisos = []



    for relacion in rol.permisos:


        permisos.append({

            "id":
            relacion.permiso.id,


            "nombre":
            relacion.permiso.name,


            "descripcion":
            relacion.permiso.description

        })



    return {


        "id": rol.id,

        "nombre": rol.name,

        "permisos": permisos

    }