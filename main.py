"""
  Integrantes:
    - VERA, Ezequiel
    - ROSELL, Ezequiel Jesus
    - CAPPA, Giuliano Martin
    - ROBLEDO, Camila Antonella
"""

import io
import os
import pickle
import platform
from datetime import date, datetime
from getpass import getpass
from random import randint
from typing import cast

# Entidades


class Administrador:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.password = ""


class Estudiante:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.email = ""
        self.sexo = ""
        self.password = ""
        self.fecha_nac = ""
        self.biografia = ""
        self.hobbies = ""
        self.genero = ""
        self.ciudad = ""
        self.pais = ""
        self.estado = True


class Moderador:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.password = ""
        self.estado = True


class Reporte:
    def __init__(self):
        self.id_reportante = 0
        self.id_reportado = 0
        self.razon = ""
        self.estado = True


class Likes:
    def __init__(self):
        self.remitente = 0
        self.destinatario = 0


"""
GENERO: Arreglo de 0 a 1 de string
PROPS_ESTUDIANTE: Arreglo de 0 a 6 de string
"""
GENERO = ["F", "M"]
PROPS_ESTUDIANTE = [
    "Nombre",
    "Nacimiento",
    "Biografía",
    "Hobbies",
    "Género",
    "Ciudad",
    "País",
]


def crear_ruta_archivo(ruta: str, ar_nombre: str) -> str:
    return os.path.join(ruta, ar_nombre)


RUTA_ARCHIVOS = os.path.join(".", "archivos")

ar_fi_estudiantes = crear_ruta_archivo(RUTA_ARCHIVOS, "estudiantes.dat")
ar_fi_likesEstudiantes = crear_ruta_archivo(RUTA_ARCHIVOS, "likes_estudiantes.dat")
ar_fi_moderadores = crear_ruta_archivo(RUTA_ARCHIVOS, "moderadores.dat")
ar_fi_administradores = crear_ruta_archivo(RUTA_ARCHIVOS, "administradores.dat")
ar_fi_reportes = crear_ruta_archivo(RUTA_ARCHIVOS, "reportes.dat")

ar_lo_estudiantes: io.BufferedRandom
ar_lo_likesEstudiantes: io.BufferedRandom
ar_lo_moderadores: io.BufferedRandom
ar_lo_administradores: io.BufferedRandom
ar_lo_reportes: io.BufferedRandom


def inicializar_ar_estudiantes():
    global ar_lo_estudiantes, ar_fi_estudiantes

    ar_lo_estudiantes = open(ar_fi_estudiantes, "w+b")
    inicializar_estudiantes()


def inicializar_ar_likes():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    ar_lo_likesEstudiantes = open(ar_fi_likesEstudiantes, "w+b")
    inicializar_likes()


def inicializar_ar_moderadores():
    global ar_lo_moderadores, ar_fi_moderadores

    ar_lo_moderadores = open(ar_fi_moderadores, "w+b")
    inicializar_moderadores()


def inicializar_ar_reportes():
    global ar_lo_reportes, ar_fi_reportes

    ar_lo_reportes = open(ar_fi_reportes, "w+b")
    inicializar_reportes()


def inicializar_ar_administradores():
    global ar_lo_administradores, ar_fi_administradores

    ar_lo_administradores = open(ar_fi_administradores, "w+b")
    inicializar_administradores()

    ar_lo_administradores.close()
    ar_lo_administradores = open(ar_fi_administradores, "rb")


def crear_archivos():
    os.mkdir(RUTA_ARCHIVOS)

    inicializar_ar_estudiantes()
    inicializar_ar_likes()
    inicializar_ar_moderadores()
    inicializar_ar_reportes()
    inicializar_ar_administradores()


def comprobar_existencia_archivos():
    global ar_lo_estudiantes, ar_lo_likesEstudiantes, ar_lo_moderadores, ar_lo_administradores, ar_lo_reportes, ar_fi_estudiantes, ar_fi_likesEstudiantes, ar_fi_moderadores, ar_fi_administradores, ar_fi_administradores, ar_fi_reportes

    if not os.path.exists(ar_fi_estudiantes):
        inicializar_ar_estudiantes()
    else:
        ar_lo_estudiantes = open(ar_fi_estudiantes, "r+b")

    if not os.path.exists(ar_fi_likesEstudiantes):
        inicializar_ar_likes()
    else:
        ar_lo_likesEstudiantes = open(ar_fi_likesEstudiantes, "r+b")

    if not os.path.exists(ar_fi_moderadores):
        inicializar_ar_moderadores()
    else:
        ar_lo_moderadores = open(ar_fi_moderadores, "r+b")

    if not os.path.exists(ar_fi_administradores):
        inicializar_ar_administradores()
    else:
        ar_lo_administradores = open(ar_fi_administradores, "rb")

    if not os.path.exists(ar_fi_reportes):
        inicializar_ar_reportes()
    else:
        ar_lo_reportes = open(ar_fi_reportes, "r+b")


### Archivos ###


def inicializar_archivos():
    if os.path.exists(RUTA_ARCHIVOS):
        comprobar_existencia_archivos()
    else:
        crear_archivos()


def finalizar_archivos():
    ar_lo_administradores.close()
    ar_lo_estudiantes.close()
    ar_lo_likesEstudiantes.close()
    ar_lo_moderadores.close()
    ar_lo_reportes.close()


### Útiles ###


def formatear_cadena(cad: str, largo: int) -> str:
    return cad.ljust(largo)


"""
comando, so: string
"""


def limpiar_consola():
    # Detecta el sistema operativo(SO).
    # Para ejecutar el comando de limpieza de terminal de acuerdo al SO.
    so = platform.system()

    if so == "Windows":
        comando = "cls"
    else:
        comando = "clear"

    os.system(comando)


def en_construccion():
    limpiar_consola()
    print("En construcción.")
    input("Presiona Enter para continuar... ")


"""
opc: string
"""


def validar_continuacion(opc: str) -> str:
    while opc != "S" and opc != "N":
        opc = input("Opción incorrecta S o N: ").upper()

    limpiar_consola()

    return opc


"""
fecha: Arreglo de 0 a 2 de string
"""


def ingresar_fecha() -> list[str]:
    fecha = [""] * 3

    fecha[0] = input("Ingresa el día de nacimiento: ")
    fecha[1] = input("Ingresa el mes de nacimiento: ")
    fecha[2] = input("Ingresa el año de nacimento: ")

    return fecha


"""
max_dia_febrero, dia, mes, anio: int
es_valido: bool
"""


def validar_valores_fecha(dia: int, mes: int, anio: int) -> bool:
    es_valido = True

    if mes < 1 or mes > 12:
        es_valido = False
    elif (
        mes == 1
        or mes == 3
        or mes == 5
        or mes == 7
        or mes == 8
        or mes == 10
        or mes == 12
    ) and (dia < 1 or dia > 31):
        es_valido = False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30):
        es_valido = False
    elif mes == 2:
        max_dia_febrero = 28

        if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
            max_dia_febrero = max_dia_febrero + 1

        if dia < 1 or dia > max_dia_febrero:
            es_valido = False
    elif anio > 2006 or anio < 1959:
        es_valido = False

    return es_valido


"""
fecha: Arreglo de 0 a 2 de string
"""


def validar_fecha(fecha: list[str]):
    while not (
        fecha[0].isdigit() and fecha[1].isdigit() and fecha[2].isdigit()
    ) or not validar_valores_fecha(int(fecha[0]), int(fecha[1]), int(fecha[2])):
        print("Los datos ingresados no son válidos")
        print("\n")
        fecha = ingresar_fecha()


"""
edades: Arreglo de 0 a 5 de int
ind: int
"""


def mostrar_edades(edades: list[int]):
    for ind in range(6):
        print(f"- {edades[ind]} años")


"""
edad, edad_1, edad_2: int
"""


def mostrar_valores_faltantes(edad_1: int, edad_2: int):
    print("\nSe detectó un hueco.")
    print(f"Los valores faltantes entre {edad_1} y {edad_2} años son:\n")

    for edad in range(edad_1 + 1, edad_2):
        print("-", edad)

    print("\n")


"""
edades: Arreglo de 0 a 5 de int
cant_huecos, edad_1, edad_2, ind: int
"""


def detectar_huecos_entre_edades(edades: list[int]):
    cant_huecos = 0

    for ind in range(5):
        edad_1 = edades[ind]
        edad_2 = edades[ind + 1]

        if edad_2 - edad_1 != 1:
            cant_huecos = cant_huecos + 1
            mostrar_valores_faltantes(edad_1, edad_2)

    if cant_huecos != 0:
        print(
            f"Se encontraron {cant_huecos} huecos entre las edades de los 6 estudiantes."
        )
    else:
        print("No se encontrarón huecos entra las edades los 6 estudiantes.")


"""
edades: Arreglo de 0 a 5 de int
aux, i, j: int
"""


def ordenar_edades_creciente(edades: list[int]):
    for i in range(5):
        for j in range(i + 1, 6):
            if edades[i] > edades[j]:
                aux = edades[j]
                edades[j] = edades[i]
                edades[i] = aux


"""
fecha_nros: Arreglo de 0 a 2 de int
fecha_actual: datetime
fecha: str
anio, dia, edad, mes: int
"""


def calcular_edad(fecha: str) -> int:
    fecha_actual = datetime.now()
    fecha_nros = obtener_valores_fecha(fecha)

    dia = fecha_nros[0]
    mes = fecha_nros[1]
    anio = fecha_nros[2]
    edad = fecha_actual.year - anio

    if fecha_actual.month <= mes and fecha_actual.day < dia:
        edad = edad - 1

    return edad


"""
edades: Arreglo de 0 a 5 de int
"""


def huecos_edades():
    edades = [21, 18, 20, 19, 23, 24]

    limpiar_consola()
    print("Las edades de los estudiantes obtenidas del reporte son:")
    mostrar_edades(edades)

    print("\nLas edades de los estudiantes ordenadas de forma creciente son:")
    ordenar_edades_creciente(edades)
    mostrar_edades(edades)
    detectar_huecos_entre_edades(edades[:])

    input("Presiona Enter para volver al inicio...")


"""
fecha_nros: Arreglo de 0 a 2 de int
fecha: str
f: datetime
"""


def obtener_valores_fecha(fecha: str) -> list[int]:
    fecha_nros = [0] * 3

    f = datetime.fromisoformat(fecha)

    fecha_nros[0] = f.day
    fecha_nros[1] = f.month
    fecha_nros[2] = f.year

    return fecha_nros


"""
fecha_nros: Arreglo de 0 a 2 de int
fecha, formato_espaniol_nacimiento: str
"""


def formatear_fecha_espaniol(fecha: str) -> str:
    fecha_nros = obtener_valores_fecha(fecha)
    formato_espaniol_nacimiento = (
        str(fecha_nros[0]) + "/" + str(fecha_nros[1]) + "/" + str(fecha_nros[2])
    )

    return formato_espaniol_nacimiento


"""
fecha: Arreglo de 0 a 2 de string
f: date
"""


def solicitar_fecha_nacimiento() -> str:
    fecha = ingresar_fecha()
    validar_fecha(fecha)

    f = date(int(fecha[2]), int(fecha[1]), int(fecha[0]))

    return f.isoformat()


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
cant_est, cant_matcheos: int
"""


def matcheos_combinados(estudiantes: list[list[str]], estados: list[bool]):
    limpiar_consola()
    cant_est = contar_estudiantes_activos(estudiantes[:], estados[:])
    cant_matcheos = cant_est * (cant_est - 1) // 2

    print(
        f"La cantidad de matcheos posibles entre los {cant_est} estudiantes actuales es igual a {cant_matcheos}."
    )
    input("\nPresiona Enter para volver al inicio...")


### Mocks ###

"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
"""


def inicializar_estudiantes():
    global ar_lo_estudiantes

    ar_lo_estudiantes.seek(0, 0)
    est = Estudiante()

    est.id = 0
    est.email = formatear_cadena("estudiante1@ayed.com", 32)
    est.password = formatear_cadena("111222", 32)
    est.nombre = formatear_cadena("Juan Peréz", 32)
    est.fecha_nac = "2001-10-01"
    est.biografia = formatear_cadena(
        "Juan Peréz es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías.",
        255,
    )
    est.hobbies = formatear_cadena("Lectura - Senderismo - Juegos de mesa", 255)
    est.genero = GENERO[1]
    est.ciudad = formatear_cadena("Rosario", 32)
    est.pais = formatear_cadena("Argentina", 32)
    est.estado = True

    pickle.dump(est, ar_lo_estudiantes)

    est.id = 1
    est.email = formatear_cadena("estudiante2@ayed.com", 32)
    est.password = formatear_cadena("333444", 32)
    est.nombre = formatear_cadena("María García", 32)
    est.fecha_nac = "1998-04-11"
    est.biografia = formatear_cadena(
        "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística.",
        255,
    )
    est.hobbies = formatear_cadena(
        "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas", 255
    )
    est.genero = GENERO[0]
    est.ciudad = "Madrid"
    est.pais = "España"
    est.estado = True

    pickle.dump(est, ar_lo_estudiantes)

    est.id = 2
    est.email = formatear_cadena("estudiante3@ayed.com", 32)
    est.password = formatear_cadena("555666", 32)
    est.nombre = formatear_cadena("Carlos Martínez", 32)
    est.fecha_nac = "2005-06-30"
    est.biografia = "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
    est.hobbies = formatear_cadena(
        "Correr - Tocar la guitarra - Cocinar platos internacionales", 255
    )
    est.genero = GENERO[1]
    est.ciudad = formatear_cadena("La Paz", 32)
    est.pais = formatear_cadena("Bolivia", 32)
    est.estado = True

    pickle.dump(est, ar_lo_estudiantes)

    est.id = 3
    est.email = formatear_cadena("estudiante4@ayed.com", 32)
    est.password = formatear_cadena("789101", 32)
    est.nombre = formatear_cadena("Ana López", 32)
    est.fecha_nac = "2001-09-15"
    est.biografia = formatear_cadena(
        "Ana López es una estudiante de ingeniería informática interesada en la inteligencia artificial y la ciberseguridad. Aspira a desarrollar tecnologías innovadoras que mejoren la seguridad digital.",
        255,
    )
    est.hobbies = formatear_cadena(
        "Leer ciencia ficción - Pintar - Practicar yoga", 255
    )
    est.genero = GENERO[0]
    est.ciudad = formatear_cadena("Asunción", 32)
    est.pais = formatear_cadena("Paraguay", 32)
    est.estado = True

    pickle.dump(est, ar_lo_estudiantes)

    ar_lo_estudiantes.flush()


"""
moderadores: Arreglo multi de 2x4 de string
"""


def inicializar_moderadores():
    global ar_lo_moderadores

    ar_lo_moderadores.seek(0, 0)
    mod = Moderador()

    mod.id = 0
    mod.email = formatear_cadena("moderador1@ayed.com", 32)
    mod.password = formatear_cadena("111222", 32)
    mod.estado = True

    pickle.dump(mod, ar_lo_moderadores)

    ar_lo_moderadores.flush()


"""
reportes: Arreglo de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
"""


def inicializar_reportes():
    global ar_lo_reportes

    ar_lo_reportes.seek(0, 0)

    re = Reporte()

    re.id_reportante = 0
    re.id_reportado = 1
    re.razon = formatear_cadena("Motivo 1", 255)
    re.estado = True

    pickle.dump(re, ar_lo_reportes)

    re.id_reportante = 0
    re.id_reportado = 2
    re.razon = formatear_cadena("Motivo 2", 255)
    re.estado = True

    pickle.dump(re, ar_lo_reportes)

    re.id_reportante = 2
    re.id_reportado = 3
    re.razon = formatear_cadena("Motivo 3", 255)
    re.estado = True

    pickle.dump(re, ar_lo_reportes)

    ar_lo_reportes.flush()


def mostrar_likes():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    like = Likes()
    ar_lo_likesEstudiantes.seek(0, 0)
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)

    while ar_lo_likesEstudiantes.tell() < tam_ar:
        like = cast(Likes, pickle.load(ar_lo_likesEstudiantes))
        print(f"Remitente {like.remitente}, Destinatario: {like.destinatario}")


"""
me_gusta: Arreglo multi de 8x8 de bool
"""


def inicializar_likes():
    global ar_lo_likesEstudiantes

    ar_lo_likesEstudiantes.seek(0, 0)

    cant_est = contar_estudiantes()

    like = Likes()

    for id_remitente in range(cant_est):
        for id_destinatario in range(cant_est):
            if id_destinatario != id_remitente and randint(0, 100) > 60:
                like.destinatario = id_destinatario
                like.remitente = id_remitente

                pickle.dump(like, ar_lo_likesEstudiantes)

    ar_lo_likesEstudiantes.flush()


def inicializar_administradores():
    global ar_lo_administradores

    ar_lo_administradores.seek(0, 0)

    ad = Administrador()

    ad.id = 0
    ad.email = formatear_cadena("administrador1@ayed.com", 32)
    ad.password = formatear_cadena("111222", 32)

    pickle.dump(ad, ar_lo_administradores)

    ar_lo_administradores.flush()


### Registro y Conexión ###

"""
password: string
"""


def ingresar_contrasenia() -> str:
    password = getpass("Ingrese su contraseña: ")

    while password == "":
        password = getpass("Debe ingresar una contraseña: ")

    return password


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
email: string
ind: int
valido: bool
"""


def email_existente(
    email: str, estudiantes: list[list[str]], moderadores: list[list[str]]
) -> bool:
    valido = True

    ind = 0
    while ind < 8 and estudiantes[ind][0] != email:
        ind = ind + 1

    if ind < 8:
        valido = False
    else:
        ind = 0
        while ind < 4 and moderadores[ind][0] != email:
            ind = ind + 1

        if ind != 4:
            valido = False

    return valido


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
estados: Arreglo de 0 a 7 de bool
acceso_valido: Arreglo de 0 a 1 de string
intentos, ind: int
email, password: string
"""


def validar_acceso(
    acceso_valido: list[int],
    estudiantes: list[list[str]],
    moderadores: list[list[str]],
    estados: list[bool],
):
    intentos = 3

    while intentos > 0 and acceso_valido[0] == "":
        email = input("Ingrese su email: ")
        password = getpass("Ingrese su contraseña: ")

        ind = 0
        while ind < 8 and (
            estudiantes[ind][0] != email or estudiantes[ind][1] != password
        ):
            ind = ind + 1

        if ind < 8 and estados[ind]:
            acceso_valido[0] = ind
            acceso_valido[1] = 1
        else:
            ind = 0
            while ind < 4 and (
                moderadores[ind][0] != email or moderadores[ind][1] != password
            ):
                ind = ind + 1

            if ind < 4:
                acceso_valido[0] = ind
                acceso_valido[1] = 0
            else:
                limpiar_consola()
                intentos = intentos - 1
                print("Datos incorrectos. Intentos restantes:", intentos, "\n")

    if intentos == 0:
        print("Ha superado el número máximo de intentos. El programa se cerrará.")
        input("Presione Enter para continuar... ")
    limpiar_consola()


def buscar_usuario_por_email(email: str, datos: io.BufferedRandom, archivo: str) -> int:
    id_usua = -1

    datos.seek(0, 0)
    tam_ar = os.path.getsize(archivo)

    while datos.tell() < tam_ar and id_usua == -1:
        reg = pickle.load(datos)

        print(reg.__dict__)
        if reg.email.strip() == email:
            id_usua = reg.id
    return id_usua


def validar_login(
    id_user: str, email: str, password: str, tipo_user: str, archivo: io.BufferedRandom
) -> bool:
    es_valido = False

    archivo.seek(0, 0)

    reg = pickle.load(archivo)

    tam_reg = archivo.tell()
    print(tam_reg, id_user)
    archivo.seek(tam_reg * id_user, 0)

    reg = pickle.load(archivo)

    if tipo_user != 2:
        es_valido = (
            reg.email.strip() == email
            and reg.password.strip() == password
            and reg.estado
        )
    else:
        es_valido = reg.email.strip() == email and reg.password.strip() == password

    return es_valido


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
estados: Arreglo de 0 a 7 de bool
acceso_valido: Arreglo de 0 a 1 de int
"""


def log_in() -> list[int]:
    global ar_lo_estudiantes, ar_fi_estudiantes, ar_lo_moderadores, ar_fi_moderadores, ar_lo_administradores, ar_fi_administradores

    acceso_valido = [-1] * 2
    intentos = 3

    limpiar_consola()
    print("\n........Ingreso........\n")

    """ 
    crear tres funciones que busquen la posición del usuario
    y tres funciones de queden sus datos
    """
    archivos = [
        [ar_lo_estudiantes, ar_fi_estudiantes],
        [ar_lo_moderadores, ar_fi_moderadores],
        [ar_lo_administradores, ar_fi_administradores],
    ]

    while intentos > 0 and acceso_valido[0] == -1:
        email = input("Ingrese su email: ")
        password = getpass("Ingrese su contraseña: ")
        id_usua = -1
        tipo_usua = 0

        while id_usua == -1 and tipo_usua < 3:
            id_usua = buscar_usuario_por_email(
                email, archivos[tipo_usua][0], archivos[tipo_usua][1]
            )

            if id_usua != -1:
                acceso_valido[0] = id_usua
                acceso_valido[1] = tipo_usua

            tipo_usua = tipo_usua + 1

        if id_usua != -1 and validar_login(
            id_usua, email, password, acceso_valido[1], archivos[id_usua][0]
        ):
            acceso_valido[0] = id_usua
        else:
            limpiar_consola()
            intentos = intentos - 1
            print("Datos incorrectos. Intentos restantes:", intentos, "\n")

    if intentos == 0:
        print("Ha superado el número máximo de intentos. El programa se cerrará.")
        input("Presione Enter para continuar... ")
    limpiar_consola()

    return acceso_valido


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
estados: Arreglo de 0 a 7 de bool
decision, email, password, rol: string
registrado: bool
"""


def registrar():
    registrado = False
    decision = ""

    # limpiar_consola()
    # while not registrado and decision != "N":
    #     print("\n........Registro........\n")

    #     email = ingresar_propiedad("email")
    #     password = ingresar_contrasenia()
    #     rol = input("Ingrese el rol estudiante(E) o moderador(M). (E/M): ").upper()

    #     while rol != "E" and rol != "M":
    #         print("\nNo es un rol válido.")
    #         rol = input("ingrese E (Estudiante) o M (Moderador): ")

    #     if rol == "E":
    #         registrado = registrar_estudiante(
    #             email, password, estudiantes, moderadores, estados
    #         )

    #     elif rol == "M":
    #         registrado = registrar_moderador(email, password, estudiantes, moderadores)

    #     if not registrado:
    #         decision = input("\nIntentar registrarse nuevamente. S/N ").upper()
    #         decision = validar_continuacion(decision)

    limpiar_consola()


### Estudiante ###


def contar_estudiantes():
    global ar_fi_estudiantes, ar_lo_estudiantes

    cant = 0

    ar_lo_estudiantes.seek(0, 0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    while ar_lo_estudiantes.tell() < tam_ar:
        est = cast(Estudiante, pickle.load(ar_lo_estudiantes))
        if est.estado:
            cant = cant + 1

    return cant


"""
prop, valor: string
"""


def ingresar_propiedad(prop: str) -> str:
    if prop == PROPS_ESTUDIANTE[4]:
        valor = input(f"Ingrese {GENERO[1]} o {GENERO[0]}: ")

        while valor != GENERO[0] and valor != GENERO[1]:
            valor = input(f"Debe ingresar {prop}:\n\t")
    elif prop == PROPS_ESTUDIANTE[1]:
        print("\nFecha de nacimiento")
        valor = solicitar_fecha_nacimiento()
    else:
        valor = input(f"Ingrese {prop}:\n\t")
        while valor == "":
            valor = input(f"Debe ingresar {prop}:\n\t")

    return valor


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
estados: Arreglo de 0 a 7 de bool
email, password: string
cant, ind: int
registrado: bool
"""


def registrar_estudiante(
    email: str,
    password: str,
    estudiantes: list[list[str]],
    moderadores: list[list[str]],
    estados: list[bool],
) -> bool:
    registrado = False
    # cant = contar_estudiantes(estudiantes[:])

    # if cant == 8:
    #     print("Por el momento no se pueden registrar nuevos estudiantes.")
    # elif not email_existente(email, estudiantes[:], moderadores[:]):
    #     print("El email ingresado ya está en uso.")
    # else:
    #     estudiantes[cant][0] = email
    #     estudiantes[cant][1] = password
    #     estados[cant] = True

    #     for ind in range(2, 9):
    #         estudiantes[cant][ind] = ingresar_propiedad(PROPS_ESTUDIANTE[ind - 2])

    #     registrado = True
    #     print("\nRegistro exitoso!!!")

    # input("Presione Enter para continuar...")

    return registrado


"""
estudiantes: Arreglo multi de 9x8 de string
est_id: int
"""


def validar_id_estudiante(est_id: int, estudiantes: list[list[str]]) -> bool:
    return 0 <= est_id and est_id <= contar_estudiantes()


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
cant, ind: int
"""


def contar_estudiantes_activos(
    estudiantes: list[list[str]], estados: list[bool]
) -> int:
    cant = 0
    ind = 0

    while ind < 8 and estudiantes[ind][0] != "":
        if estados[ind]:
            cant = cant + 1
        ind = ind + 1

    return cant


"""
me_gusta: Arreglo multi de 8x8 de bool
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
cant, est_id, ind: int
"""


def contar_estudiantes_activos_no_matcheados(
    est_id: int,
    estudiantes: list[list[str]],
    estados: list[bool],
    me_gusta: list[list[bool]],
) -> int:
    cant = 0
    ind = 0

    while ind < 8 and estudiantes[ind][0] != "":
        if ind != est_id and estados[ind] and not me_gusta[est_id][ind]:
            cant = cant + 1

        ind = ind + 1

    return cant


"""
estudiantes: Arreglo multi de 9x8 de string
ind: int
nombre: string
"""


def obtener_id_estudiante_por_nombre(nombre: str, estudiantes: list[list[str]]) -> int:
    ind = 0

    while ind < 8 and estudiantes[ind][2] != nombre:
        ind = ind + 1

    return ind


"""
estudiantes: Arreglo multi de 9x8 de string
est_id, ind: int
"""


def obtener_nombre_estudiante_por_id(est_id: int, estudiantes: list[list[str]]) -> str:
    ind = 0

    while ind < 8 and ind != est_id:
        ind = ind + 1

    return estudiantes[ind][2]


"""
estados: Arreglo de 0 a 7 de bool
est_id: int
opc: string
"""


def eliminar_perfil(est_id: int, estados: list[bool]):
    print("\n")
    opc = input("¿Desea eliminar su perfil? (S/N) ").upper()
    opc = validar_continuacion(opc)

    if opc == "S":
        estados[est_id] = False

        print("Perfil borrado con exito.")
        input("Presione Enter para continuar ")


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
estados: Arreglo de 0 a 7 de bool
est_id, reporte_id, reporte_ind, reportado_id: int
decision, motivo, opc, reportado: string
"""


def reportar_candidato(
    est_id: int,
    estudiantes: list[list[str]],
    estados: list[bool],
    reportes: list[list[int]],
    motivo_reportes: list[str],
):
    decision = ""
    reportado_id = -1

    limpiar_consola()
    while decision != "N":
        reportado = input("Ingrese el nombre o el id del candidato: ")

        if not reportado.isdigit():
            reportado_id = obtener_id_estudiante_por_nombre(reportado, estudiantes)
        else:
            reportado_id = int(reportado) - 1

        if (
            est_id == reportado_id
            or not validar_id_estudiante(reportado_id, estudiantes[:])
            or not estados[reportado_id]
        ):
            print("El usuario ha reportar no es válido.\n")
        else:
            limpiar_consola()
            opc = input(
                "Seguro que desea continuar con reporte del candidato. S/N "
            ).upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                motivo = input("Motivo:\n\t")

                while motivo == "":
                    print("Debe ingresar el motivo del reporte.")
                    motivo = input("Por favor. Ingrese el motivo:\n\t")

                reporte_ind = contar_reportes(reportes[:])

                if reporte_ind == 40:
                    print("\nError al generar el reporte.")
                else:
                    reportes[reporte_ind][0] = 0
                    reportes[reporte_ind][1] = est_id
                    reportes[reporte_ind][2] = reportado_id

                    motivo_reportes[reporte_ind] = motivo

                    print("Reporte generado con éxito.")

                input("Presione Enter para continuar... ")
                decision = input("\nGenerar un nuevo reporte. S/N: ").upper()
                decision = validar_continuacion(decision)


"""
estudiantes: Arreglo multi de 9x8 de string
est_id, ind: int
"""


def mostrar_datos_estudiante(est_id: int):
    print("Datos de usuario\n")

    # for ind in range(2, 9):
    #     if ind - 2 == 1:
    #         print(
    #             PROPS_ESTUDIANTE[ind - 2],
    #             ":",
    #             formatear_fecha_espaniol(estudiantes[est_id][ind]),
    #         )
    #     else:
    #         print(PROPS_ESTUDIANTE[ind - 2], ":", estudiantes[est_id][ind])


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
est_id: int
opc: string
"""


def manejador_submenu_gestionar_perfil(est_id: int):
    opc = ""

    # while opc != "c" and estados[est_id]:
    #     limpiar_consola()
    #     print("........Gestionar Perfil........\n")
    #     print("a. Editar mis datos personales")
    #     print("b. Eliminar mi perfil")
    #     print("c. Volver")

    #     opc = input("\nSeleccione una opción: ")

    #     while opc != "a" and opc != "b" and opc != "c":
    #         print("\nNo es una opción válida.")
    #         opc = input("Ingrese una opción válida: ")

    #     if opc == "a":
    #         editar_datos_estudiante(est_id)
    #     elif opc == "b":
    #         eliminar_perfil(est_id)


"""
estudiantes: Arreglo multi de 9x8 de string
nombre: string
est_id: int
"""


def validar_nombre(nombre: str, estudiantes: list[list[str]]) -> str:
    est_id = obtener_id_estudiante_por_nombre(nombre, estudiantes[:])

    while est_id == -1:
        print("No existe el estudiante", nombre)
        nombre = input("Ingrese un nombre de estudiante: ")
        est_id = obtener_id_estudiante_por_nombre(nombre, estudiantes[:])

    return nombre


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
formato_espaniol_nacimiento: string
edad, est_id, ind: int
"""


def ver_perfil_estudiante(
    est_id: int,
    estudiantes: list[list[str]],
    estados: list[bool],
    me_gusta: list[list[bool]],
):
    ind = 0

    limpiar_consola()
    while ind < 8 and estudiantes[ind][0] != "":
        if ind != est_id and estados[ind]:
            edad = calcular_edad(estudiantes[ind][3])
            formato_espaniol_nacimiento = formatear_fecha_espaniol(estudiantes[ind][3])

            print("Nombre:", estudiantes[ind][2])
            print("Fecha de nacimiento:", formato_espaniol_nacimiento)
            print("Edad:", edad)
            print("Biografía:\n\t" + estudiantes[ind][4])
            print("Hobbies:\n\t", estudiantes[ind][5])
            print("Ciudad: ", estudiantes[ind][7])
            print("País: ", estudiantes[ind][8])

            if me_gusta[est_id][ind]:
                print("Estado del Match: Tienes match ✔️")
            else:
                print("Estado del Match: No tienes match ❌")

            print("\n")

        ind = ind + 1


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
est_id, match_id: int
decision, nombre_estudiante: string
"""


def marcar_match(
    est_id: int,
    estudiantes: list[list[str]],
    estados: list[bool],
    me_gusta: list[list[bool]],
):
    decision = "S"

    if decision == "S":
        nombre_estudiante = input(
            "\nIngrese el nombre del estudiante con el que quiere hacer matcheo: "
        )

        nombre_estudiante = validar_nombre(nombre_estudiante, estudiantes[:])
        match_id = obtener_id_estudiante_por_nombre(nombre_estudiante, estudiantes[:])

        if me_gusta[est_id][match_id]:
            print("\nYa tiene match con", nombre_estudiante)
        else:
            me_gusta[est_id][match_id] = True

            limpiar_consola()
            ver_perfil_estudiante(est_id, estudiantes[:], estados[:], me_gusta[:])
            print("Se envío el match a", nombre_estudiante)

        input("Presione Enter para continuar... ")


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
est_id: int
decision, opc: string
realizo_matcheo: bool
"""


def manejador_matcheo_estudiantes(
    est_id: int,
    estudiantes: list[list[str]],
    estados: list[bool],
    me_gusta: list[list[bool]],
):
    opc = ""

    ver_perfil_estudiante(est_id, estudiantes[:], estados[:], me_gusta[:])
    decision = input(
        "Le gustaría en un futuro hacer matcheo con algún estudiante. (S/N) "
    ).upper()

    while decision != "S" and decision != "N":
        decision = input("Desea hacer matcheo con algún estudiante S o N: ").upper()

    while opc != "N" and decision != "N":
        ver_perfil_estudiante(est_id, estudiantes[:], estados[:], me_gusta[:])
        marcar_match(est_id, estudiantes[:], estados[:], me_gusta)

        opc = input("\nRealizar un nuevo match, S/N: ").upper()

        while opc != "S" and opc != "N":
            limpiar_consola()
            opc = input("Realizar un nuevo match, S/N: ").upper()


"""
estudiantes: Arreglo multi de 9x8 de string
me_gusta: Arreglo multi de 8x8 de bool
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
estados: Arreglo de 0 a 7 de bool
opc: string
est_id: int
"""


def manejador_submenu_gestionar_candidatos(
    est_id: int,
    reportes: list[list[int]],
    motivo_reportes: list[str],
    estudiantes: list[list[str]],
    estados: list[bool],
    me_gusta: list[list[bool]],
):
    opc = ""

    while opc != "c":
        limpiar_consola()
        print("........Gestionar Candidatos........\n")
        print("a. Ver candidatos")
        print("b. Reportar un candidato")
        print("c. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b" and opc != "c":
            print("\nNo es una opción válida.")
            opc = input("\nSeleccione una opción: ")

        if opc == "a":
            manejador_matcheo_estudiantes(est_id, estudiantes[:], estados[:], me_gusta)

        if opc == "b":
            reportar_candidato(
                est_id, estudiantes[:], estados[:], reportes, motivo_reportes
            )


"""
opc: string
"""


def manejador_submenu_matcheos():
    opc = ""

    while opc != "c":
        limpiar_consola()
        print("........Matcheos........\n")
        print("a. Ver matcheos")
        print("b. Eliminar un matcheo")
        print("c. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b" and opc != "c":
            print("\nNo es una opción válida.")
            opc = input("\nSeleccione una opción: ")

        if opc == "a" or opc == "b":
            en_construccion()


"""
estudiantes: Arreglo multi de 9x8 de string
est_id: int
opc, valor: str
"""


def editar_datos_estudiante(est_id: int):
    opc = ""

    # while opc != "n":
    #     limpiar_consola()
    #     mostrar_datos_estudiante(est_id)

    #     print("\n\n........Actualizar perfil........\n")
    #     print("a. Cambiar fecha de nacimiento")
    #     print("b. Editar biografía")
    #     print("c. Editar hobbies")
    #     print("d. Cambiar género")
    #     print("e. Cambiar ciudad")
    #     print("f. Cambiar país")
    #     print("n. Finalizar\n")

    #     opc = input("Seleccione una opción: ")

    #     print("\n")
    #     while (
    #         opc != "a"
    #         and opc != "b"
    #         and opc != "c"
    #         and opc != "d"
    #         and opc != "e"
    #         and opc != "f"
    #         and opc != "n"
    #     ):
    #         print("No es una opción válida.")
    #         opc = input("Ingrese una opción válida: ")

    #     match opc:
    #         case "a":
    #             valor = solicitar_fecha_nacimiento()
    #             estudiantes[est_id][3] = valor
    #         case "b":
    #             valor = ingresar_propiedad(PROPS_ESTUDIANTE[2])
    #             estudiantes[est_id][4] = valor
    #         case "c":
    #             valor = ingresar_propiedad(PROPS_ESTUDIANTE[3])
    #             estudiantes[est_id][5] = valor
    #         case "d":
    #             valor = ingresar_propiedad(PROPS_ESTUDIANTE[4])
    #             estudiantes[est_id][6] = valor
    #         case "e":
    #             valor = ingresar_propiedad(PROPS_ESTUDIANTE[5])
    #             estudiantes[est_id][7] = valor
    #         case "f":
    #             valor = ingresar_propiedad(PROPS_ESTUDIANTE[6])
    #             estudiantes[est_id][8] = valor


"""
estudiantes: Arreglo de multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
cant_estudiantes, est_id, ind, likes_dados, likes_recibidos, matches: int
like_dado, like_recibido: bool
porcentaje: float
"""


def reportes_estadisticos_estudiante(
    est_id: int,
    estudiantes: list[list[str]],
    estados: list[bool],
    me_gusta: list[list[bool]],
):
    likes_dados = 0
    likes_recibidos = 0
    matches = 0

    cant_estudiantes = contar_estudiantes_activos(estudiantes[:], estados[:])

    for ind in range(cant_estudiantes):
        if est_id != ind and estados[ind]:
            like_dado = me_gusta[est_id][ind]
            like_recibido = me_gusta[ind][est_id]

            if like_dado and like_recibido:
                matches = matches + 1
            elif like_dado and not like_recibido:
                likes_dados = likes_dados + 1
            elif not like_dado and like_recibido:
                likes_recibidos = likes_recibidos + 1

    porcentaje = 0.0

    if likes_dados != 0 or likes_recibidos != 0 or matches != 0:
        porcentaje = matches / (likes_recibidos + likes_dados + matches) * 100

    limpiar_consola()
    print(f"Matcheados sobre el % posible: {porcentaje:.1f}%")
    print("Likes dados y no recibidos:", likes_dados)
    print("Likes recibidos y no respondidos:", likes_recibidos)
    input("Presiona Enter para volver al menú... ")


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
decision, estudiante, opc: string
est_id: int
"""


def desactivar_usuario(estudiantes: list[list[str]], estados: list[bool]):
    decision = ""

    while decision != "N":
        limpiar_consola()
        estudiante = input("Ingrese el ID o el nombre del usuario: ")
        est_id = -1

        if not estudiante.isdigit():
            est_id = obtener_id_estudiante_por_nombre(estudiante, estudiantes[:])
        else:
            est_id = int(estudiante) - 1

        if not validar_id_estudiante(est_id, estudiantes[:]) or not estados[est_id]:
            print("El usuario no existe.\n")
        elif not estados[est_id]:
            print("El usuario ya está desactivado.\n")
        else:
            limpiar_consola()
            opc = input(
                "Seguro que desea continuar con la desactivación del usuario. S/N "
            ).upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                estados[est_id] = False

                print("Perfil borrado con exito.")

        input("Presione Enter para continuar ")

        limpiar_consola()
        decision = input("Desactivar otra cuenta. S/N: ").upper()
        decision = validar_continuacion(decision)


"""
cand: Arreglo multi de 2x3 de int
valores: Arreglo de 0 a 2 de int
ind: int
"""


def calcular_eleccion_candidatos(valores: list[int], cand: list[list[int]]):
    for ind in range(3):
        valores[ind] = randint(0, 100) * cand[ind][1]


"""
candidatos: Arreglo multi de 2x3 de int
est_id, ind: int
"""


def comprobar_nuevo_candidato(est_id: int, candidatos: list[list[int]]) -> bool:
    ind = 0

    while ind < 3 and candidatos[ind][0] != est_id:
        ind = ind + 1

    return ind == 3


"""
cand: Arreglo multi de 2x3 de int
ind, total: int
"""


def calcular_probabilidad_total_candidatos(cand: list[list[int]]) -> int:
    total = 0

    for ind in range(3):
        total = total + cand[ind][1]

    return total


"""
estudiantes: Arreglo multi de 9x8 de string
cand: Arreglo multi de 2x3 de int
est_id, ind: int
"""


def mostrar_candidatos(cand: list[list[int]], estudiantes: list[list[str]]):
    for ind in range(3):
        est_id = cand[ind][0]

        print(f"{ind + 1}. {obtener_nombre_estudiante_por_id(est_id, estudiantes[:])}")


"""
valores: Arreglo de 0 a 2 de int
ind, mayor, pos, valor: int
"""


def buscar_candidato_mayor_valor(valores: list[int]) -> int:
    mayor = -1
    pos = 0

    for ind in range(3):
        valor = valores[ind]

        if valores[ind] > mayor:
            mayor = valor
            pos = ind

    return pos


"""
estudiantes: Arreglo multi de 9x8 de string
candidatos: Arreglo multi de 2x3 de int
candidato_ind, cant_est_totales, est_id, usuario_id: int
"""


def obtener_candidatos(
    usuario_id: int, candidatos: list[list[int]], estudiantes: list[list[str]]
):
    for candidato_ind in range(3):
        cant_est_totales = contar_estudiantes()
        est_id = randint(0, cant_est_totales - 1)

        while est_id == usuario_id or not comprobar_nuevo_candidato(
            est_id, candidatos[:]
        ):
            est_id = randint(0, cant_est_totales - 1)

        candidatos[candidato_ind][0] = est_id


"""
estudiantes: Arreglo multi de 9x8 de string
candidatos: Arreglo multi de 2x3 de int
me_gusta: Arreglo multi de 8x8 de bool
valores: Arreglo de 0 a 2 de int
usuario_id, pos_elegido, pos_match, usuario: int
nombre_match: string
"""


def matchear_candidato(
    usuario_id: int,
    valores: list[int],
    candidatos: list[list[int]],
    me_gusta: list[list[bool]],
    estudiantes: list[list[str]],
):
    pos_elegido = buscar_candidato_mayor_valor(valores[:])

    nombre_match = obtener_nombre_estudiante_por_id(
        candidatos[pos_elegido][0], estudiantes[:]
    )
    pos_match = candidatos[pos_elegido][0]
    me_gusta[usuario_id][pos_match] = True

    print("\nTu match es la persona", nombre_match)


"""
estudiantes: Arreglo multi de 9x8 de string
me_gusta: Arreglo multi de 8x8 de bool
candidatos: Arreglo multi de 2x3 de int
estados: Arreglo de 0 a 7 de bool
valores_eleccion_candidatos: Arreglo de 0 a 2 de int
continuar, valor: string
cant_est_posibles, probabilidad_ingresada, probabilidad_match_1, probabilidad_match_2, probabilidad_match_3, usuario_id: int
"""


def ruleta(
    usuario_id: int,
    estudiantes: list[list[str]],
    estados: list[bool],
    me_gusta: list[list[bool]],
):
    cant_est_posibles = contar_estudiantes_activos_no_matcheados(
        usuario_id, estudiantes[:], estados[:], me_gusta[:]
    )

    if cant_est_posibles < 3:
        print("No hay suficientes estudiantes activos para esta función.")
    else:
        continuar = ""

        while continuar != "N" and cant_est_posibles >= 3:
            limpiar_consola()

            candidatos = [[-1] * 2 for n in range(3)]
            obtener_candidatos(usuario_id, candidatos, estudiantes[:])

            print("........RULETA........")
            print(
                "A continuación, se le pedirá ingresar la probabilidad de matcheo con tres estudiantes."
            )
            print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

            while calcular_probabilidad_total_candidatos(candidatos[:]) != 100:
                mostrar_candidatos(candidatos[:], estudiantes[:])

                print("\n")
                for probabilidad_ingresada in range(3):
                    valor = input(
                        f"Ingresar la probabilidad del estudiante {probabilidad_ingresada + 1}: "
                    )

                    while not valor.isnumeric():
                        valor = input("Por favor ingrese un valor numérico entero: ")

                    candidatos[probabilidad_ingresada][1] = int(valor)

                probabilidad_total = calcular_probabilidad_total_candidatos(
                    candidatos[:]
                )

                if probabilidad_total != 100:
                    limpiar_consola()
                    print(
                        "La probabilidad total debe ser igual a 100 y el introducido es",
                        probabilidad_total,
                        ".",
                    )
                    print("Vuelva a introducir los valores.\n")

            valores_eleccion_candidatos = [0] * 3

            calcular_eleccion_candidatos(valores_eleccion_candidatos, candidatos[:])
            matchear_candidato(
                usuario_id,
                valores_eleccion_candidatos[:],
                candidatos[:],
                me_gusta,
                estudiantes[:],
            )

            continuar = input("Usar la ruleta nuevamente. S/N ").upper()
            continuar = validar_continuacion(continuar)
            cant_est_posibles = contar_estudiantes_activos_no_matcheados(
                usuario_id, estudiantes[:], estados[:], me_gusta[:]
            )

        if cant_est_posibles < 3 and continuar == "S":
            print("No hay suficientes estudiantes activos para esta función.")
            input("Presione Enter para volver al inicio... ")


### Reporte ###

"""
reportes: Arreglo multi de 3x40 de int
ind: int
"""


def contar_reportes(reportes: list[list[int]]) -> int:
    ind = 0

    while ind < 40 and reportes[ind][0] != -1:
        ind = ind + 1

    return ind


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de sring
nombre_reportante, nombre_reportado: string
reporte_id: int
"""


def mostrar_detalle_reporte(
    reporte_id: int,
    reportes: list[list[int]],
    motivo_reportes: list[str],
    estudiantes: list[list[str]],
):
    nombre_reportante = obtener_nombre_estudiante_por_id(
        reportes[reporte_id][1], estudiantes[:]
    )
    nombre_reportado = obtener_nombre_estudiante_por_id(
        reportes[reporte_id][2], estudiantes[:]
    )

    print(f"........Reporte {reporte_id + 1}........\n")
    print("Reportante:", nombre_reportante)
    print("Reportado:", nombre_reportado)
    print(f"Motivo:\n\t{motivo_reportes[reporte_id]}\n\n")


"""
reportes: Arreglo multi de 3x40 de int
reporte_id: int
"""


def ignorar_reporte(reporte_id: int, reportes: list[list[int]]):
    reportes[reporte_id][0] = 2
    print("Procesado el reporte", (reporte_id + 1))
    print("El reporte fue ignorado.")


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
reportes: Arreglo multi de 3x40 de int
cant_reportes, ind, reporte_id, reportado_id: int
nombre_reportado: string
"""


def bloquear_reportado(
    reporte_id: int,
    reportes: list[list[int]],
    estudiantes: list[list[str]],
    estados: list[bool],
):
    cant_reportes = contar_reportes(reportes[:])
    reportado_id = reportes[reporte_id][2]
    estados[reportado_id] = False
    nombre_reportado = obtener_nombre_estudiante_por_id(reportado_id, estudiantes)

    print("Procesado el reporte", (reporte_id + 1))
    print(f"El reportado {nombre_reportado} fue bloqueado.")

    ind = 0
    for ind in range(0, cant_reportes):
        if reportes[ind][2] == reportado_id:
            reportes[ind][0] = 1


"""
reportes: Arreglo multi de 3x40 de int
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
opc: string
ind, reportado_id, reporte_id: int
"""


def procesar_reporte(
    reporte_id: int,
    reportes: list[list[int]],
    estudiantes: list[list[str]],
    estados: list[bool],
):
    print("¿Cómo proceder?\n")
    print("1. Ignorar reporte")
    print("2. Bloquear al reportado")

    opc = input("\n\nSeleccione una opción: ")

    while opc != "1" and opc != "2":
        print("\nNo es una opción válida.")
        opc = input("Ingrese una opción válida: ")

    if opc == "1":
        ignorar_reporte(reporte_id, reportes)
    else:
        bloquear_reportado(reporte_id, reportes, estudiantes, estados)


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
reporte: Arreglo de 0 a 4 de string
cant_reportes, ind: int
opc: string
estudiantes_activos: bool
"""


def ver_reportes(
    reportes: list[list[int]],
    motivo_reportes: list[str],
    estudiantes: list[list[str]],
    estados: list[bool],
):
    ind = 0
    opc = ""

    cant_reportes = contar_reportes(reportes)

    while ind < cant_reportes and opc != "N" and reportes[ind][0] != -1:

        limpiar_consola()
        estudiantes_activos = estados[reportes[ind][1]] and estados[reportes[ind][2]]

        if estudiantes_activos and reportes[ind][0] == 0:
            mostrar_detalle_reporte(
                ind, reportes[:], motivo_reportes[:], estudiantes[:]
            )
            procesar_reporte(ind, reportes, estudiantes, estados)

            opc = input("Continuar revisando reportes. (S/N) ").upper()
            opc = validar_continuacion(opc)

        ind = ind + 1

    if ind == cant_reportes:
        print("No quedan más reportes pendientes.")
        input("Presione Enter para continuar... ")


### Moderador ###

"""
moderadores: Arreglo multi de 2x4 de string
ind: int
"""


def contar_moderadores(moderadores: list[list[str]]) -> int:
    ind = 0

    while ind < 4 and moderadores[ind][0] != "":
        ind = ind + 1

    return ind


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
email, password: string
registrado: bool
cant: int
"""


def registrar_moderador(
    email: str,
    password: str,
    estudiantes: list[list[str]],
    moderadores: list[list[str]],
) -> bool:
    registrado = False
    cant = contar_moderadores(moderadores[:])

    if cant == 4:
        print("Por el momento no se pueden registrar nuevos moderadores.")
    elif not email_existente(email, estudiantes[:], moderadores[:]):
        print("El email ingresado ya está en uso.")
    else:
        moderadores[cant][0] = email
        moderadores[cant][1] = password
        registrado = True
        print("\nRegistro exitoso!!!")

    input("Presione Enter para continuar...")

    return registrado


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
opc: string
"""


def manejador_submenu_gestionar_usuarios(
    estudiantes: list[list[str]], estados: list[bool]
):
    opc = ""

    while opc != "b":
        limpiar_consola()
        print("........Gestionar Usuarios........\n")
        print("a. Desactivar usuario")
        print("b. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            desactivar_usuario(estudiantes[:], estados)


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
opc: string
"""


def manejador_submenu_gestionar_reportes(
    estudiantes: list[list[str]],
    reportes: list[list[int]],
    motivo_reportes: list[str],
    estados: list[bool],
):
    opc = ""

    while opc != "b":
        limpiar_consola()
        print("........Gestionar Reportes........\n")
        print("a. Ver reportes")
        print("b. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            ver_reportes(reportes, motivo_reportes, estudiantes, estados)


### Mostrar ###

"""
opcion: string
"""


def mostrar_menu_principal_estudiante() -> str:
    limpiar_consola()

    print("\n........Home........")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("6. Hueco edades estudiantes")
    print("7. Matcheos combinandos")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    while (
        opcion != "1"
        and opcion != "2"
        and opcion != "3"
        and opcion != "4"
        and opcion != "5"
        and opcion != "6"
        and opcion != "7"
        and opcion != "0"
    ):
        print("La opción introducida no es válida.")
        opcion = input("Por favor, introduzca una opción válida: ")

    return opcion


"""
opc: string
"""


def mostrar_menu_principal_moderadores() -> str:
    limpiar_consola()

    print("\n........Home........")
    print("1. Gestionar Usuarios")
    print("2. Gestionar Reportes")
    print("3. Reportes Estadísticos")
    print("0. Salir")

    opc = input("\nSeleccione una opción: ")

    while opc != "1" and opc != "2" and opc != "3" and opc != "0":
        print("\nLa opción introducida no es válida.")
        opc = input("Por favor, introduzca una opción válida: ")

    return opc


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
me_gusta: Arreglo multi de 8x8 de bool
estados: Arreglo de 0 a 7 de bool
rol, usuario_id: int
"""


def mostrar_menu_usuario(usuario_id: int, rol: int):
    if rol == 0:
        manejador_menu_principal_estudiante(usuario_id)
    # elif rol == 1:
    #     manejador_menu_principal_moderador()


"""
opcion: string
"""


def mostrar_menu_principal() -> str:
    limpiar_consola()

    print("\n........Bienvenido........\n")
    print("1. Conectarse")
    print("2. Registrarse")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    while opcion != "1" and opcion != "2" and opcion != "0":
        print("La opción introducida no es válida.")
        opcion = input("Por favor, introduzca una opción válida: ")

    return opcion


### Gestionar ###

"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
est_id: int
opc: string
"""


def manejador_menu_principal_estudiante(est_id: int):
    opc = ""

    # while opc != "0" and estados[est_id]:
    #     opc = mostrar_menu_principal_estudiante()

    #     match opc:
    #         case "1":
    #             manejador_submenu_gestionar_perfil(est_id)

    #         case "2":
    #             manejador_submenu_gestionar_candidatos(est_id)

    #         case "3":
    #             manejador_submenu_matcheos()

    #         case "4":
    #             reportes_estadisticos_estudiante(est_id)

    #         case "5":
    #             ruleta(est_id)

    #         case "6":
    #             huecos_edades()

    #         case "7":
    #             matcheos_combinados()

    #         case "0":
    #             limpiar_consola()


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
estados: Arreglo de 0 a 7 de bool
opc: string
"""


def manejador_menu_principal_moderador(
    reportes: list[list[int]],
    motivo_reportes: list[str],
    estudiantes: list[list[str]],
    estados: list[bool],
):
    opc = "1"

    while opc != "0":
        opc = mostrar_menu_principal_moderadores()

        match opc:
            case "1":
                manejador_submenu_gestionar_usuarios(estudiantes, estados)

            case "2":
                manejador_submenu_gestionar_reportes(
                    estudiantes, reportes, motivo_reportes, estados
                )

            case "3":
                en_construccion()

            case "0":
                limpiar_consola()
                print("¡Hasta luego!")


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
me_gusta: Arreglo multi de 8x8 de bool
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
usuario: Arreglo de 0 a 1 de int
estados: Arreglo de 0 a 7 de bool
opc: string
"""


def main():
    inicializar_archivos()

    opc = ""
    usuario = [0] * 2

    while opc != "0" and usuario[0] != -1:
        opc = mostrar_menu_principal()

        match opc:
            case "0":
                limpiar_consola()
                print("¡Hasta luego!")
            case "1":
                usuario = log_in()

                # if usuario[0] != -1 or usuario[0] != -2:
                #     mostrar_menu_usuario(usuario[0], usuario[1])
            case "2":
                registrar()

    finalizar_archivos()


main()
