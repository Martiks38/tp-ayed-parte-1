"""
  Integrantes:
    - CAPPA, Giuliano Martin
    - CARRIZO, Adrián Osvaldo
"""

import io
import os
import pickle
import platform
from datetime import date, datetime
from getpass import getpass
from random import randint

# Entidades


class Administrador:
    def __init__(self):
        self.id = -1
        self.email = ""
        self.password = ""
        self.estado = False


class Estudiante:
    def __init__(self):
        self.id = -1
        self.nombre = ""
        self.email = ""
        self.password = ""
        self.fecha_nac = ""
        self.biografia = ""
        self.hobbies = ""
        self.genero = ""
        self.ciudad = ""
        self.pais = ""
        self.estado = False
        self.cant_reportes = 0


class Moderador:
    def __init__(self):
        self.id = -1
        self.email = ""
        self.password = ""
        self.estado = False
        self.cant_ignorados = 0
        self.cant_aceptados = 0


class Reporte:
    def __init__(self):
        self.id = -1
        self.id_reportante = -1
        self.id_reportado = -1
        self.razon = ""
        self.estado = -1


class Like:
    def __init__(self):
        self.remitente = -1
        self.destinatario = -1


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


def formatear_estudiante(est: Estudiante):
    est.email = formatear_cadena(est.email, 32)
    est.password = formatear_cadena(est.password, 32)
    est.nombre = formatear_cadena(est.nombre, 32)
    est.biografia = formatear_cadena(est.biografia, 255)
    est.fecha_nac = formatear_cadena(est.fecha_nac, 10)
    est.hobbies = formatear_cadena(est.hobbies, 255)
    est.ciudad = formatear_cadena(est.ciudad, 32)
    est.pais = formatear_cadena(est.pais, 32)


def formatear_moderador(mod: Moderador):
    mod.email = formatear_cadena(mod.email, 32)
    mod.password = formatear_cadena(mod.password, 32)


def formatear_administrador(ad: Administrador):
    ad.email = formatear_cadena(ad.email, 32)
    ad.password = formatear_cadena(ad.password, 32)


def formatear_reporte(re: Reporte):
    re.razon = formatear_cadena(re.razon, 255)


def desformatear_estudiante(est: Estudiante):
    est.email = est.email.strip()
    est.password = est.password.strip()
    est.nombre = est.nombre.strip()
    est.biografia = est.biografia.strip()
    est.hobbies = est.hobbies.strip()
    est.ciudad = est.ciudad.strip()
    est.pais = est.pais.strip()


def desformatear_moderador(mod: Moderador):
    mod.email = mod.email.strip()
    mod.password = mod.password.strip()


def desformatear_administrador(ad: Administrador):
    ad.email = ad.email.strip()
    ad.password = ad.password.strip()


def desformatear_reporte(re: Reporte):
    re.razon = re.razon.strip()


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


def obtener_largo_registro(datos: io.BufferedRandom):
    datos.seek(0)
    pickle.load(datos)

    return datos.tell()


def crear_archivos():
    os.mkdir(RUTA_ARCHIVOS)

    inicializar_estudiantes()
    inicializar_likes()
    inicializar_moderadores()
    inicializar_reportes()
    inicializar_administradores()


def comprobar_existencia_archivos():
    global ar_lo_estudiantes, ar_lo_likesEstudiantes, ar_lo_moderadores, ar_lo_administradores, ar_lo_reportes, ar_fi_estudiantes, ar_fi_likesEstudiantes, ar_fi_moderadores, ar_fi_administradores, ar_fi_administradores, ar_fi_reportes

    if not os.path.exists(ar_fi_estudiantes):
        inicializar_estudiantes()
    else:
        ar_lo_estudiantes = open(ar_fi_estudiantes, "r+b")

    if not os.path.exists(ar_fi_likesEstudiantes):
        inicializar_likes()
    else:
        ar_lo_likesEstudiantes = open(ar_fi_likesEstudiantes, "r+b")

    if not os.path.exists(ar_fi_moderadores):
        inicializar_moderadores()
    else:
        ar_lo_moderadores = open(ar_fi_moderadores, "r+b")

    if not os.path.exists(ar_fi_administradores):
        inicializar_administradores()
    else:
        ar_lo_administradores = open(ar_fi_administradores, "rb")

    if not os.path.exists(ar_fi_reportes):
        inicializar_reportes()
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


def matcheos_combinados():
    limpiar_consola()
    cant_est = contar_estudiantes_activos()
    cant_matcheos = cant_est * (cant_est - 1) // 2

    print(
        f"La cantidad de matcheos posibles entre los {cant_est} estudiantes activos es igual a {cant_matcheos}."
    )
    input("\nPresiona Enter para volver al inicio...")


### Mocks ###

"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
"""


def inicializar_estudiantes():
    global ar_lo_estudiantes, ar_fi_estudiantes

    ar_lo_estudiantes = open(ar_fi_estudiantes, "w+b")
    ar_lo_estudiantes.seek(0)

    ESTUDIANTES = [
        [
            "estudiante1@ayed.com",
            "111222",
            "Juan Perez",
            "2001-10-01",
            "Juan Perez es un estudiante de informatica apasionado por la programacion. Le encanta aprender nuevos lenguajes y tecnologias.",
            "Lectura - Senderismo - Juegos de mesa",
            GENERO[1],
            "Rosario",
            "Argentina",
        ],
        [
            "estudiante2@ayed.com",
            "333444",
            "Maria Garcia",
            "1998-04-11",
            "Maria Garcia es una estudiante de arte con una pasion por la pintura y el dibujo desde una edad temprana. Actualmente esta explorando nuevas formas de expresion artistica.",
            "Pintura al oleo - Dibujo de retratos - Lectura de novelas historicas",
            GENERO[0],
            "Madrid",
            "Espana",
        ],
        [
            "estudiante3@ayed.com",
            "555666",
            "Carlos Martinez",
            "2005-06-30",
            "Carlos Martinez es un estudiante de medicina enfocado en la investigacion de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos mas efectivos y accesibles.",
            "Correr - Tocar la guitarra - Cocinar platos internacionales",
            GENERO[1],
            "La Paz",
            "Bolivia",
        ],
        [
            "estudiante4@ayed.com",
            "777888",
            "Ana Lopez",
            "2001-09-15",
            "Ana Lopez es una estudiante de ingenieria informatica interesada en la inteligencia artificial y la ciberseguridad. Aspira a desarrollar tecnologias innovadoras que mejoren la seguridad digital.",
            "Leer ciencia ficcion - Pintar - Practicar yoga",
            GENERO[0],
            "Asuncion",
            "Paraguay",
        ],
    ]

    est = Estudiante()
    est.estado = True
    est.cant_reportes = 0

    for ind in range(4):
        est.id = ind
        est.email = ESTUDIANTES[ind][0]
        est.password = ESTUDIANTES[ind][1]
        est.nombre = ESTUDIANTES[ind][2]
        est.fecha_nac = ESTUDIANTES[ind][3]
        est.biografia = ESTUDIANTES[ind][4]
        est.hobbies = ESTUDIANTES[ind][5]
        est.genero = ESTUDIANTES[ind][6]
        est.ciudad = ESTUDIANTES[ind][7]
        est.pais = ESTUDIANTES[ind][8]

        formatear_estudiante(est)
        pickle.dump(est, ar_lo_estudiantes)
        ar_lo_estudiantes.flush()


"""
moderadores: Arreglo multi de 2x4 de string
"""


def inicializar_moderadores():
    global ar_lo_moderadores, ar_fi_moderadores

    ar_lo_moderadores = open(ar_fi_moderadores, "w+b")
    ar_lo_moderadores.seek(0)

    MODERADORES = [["moderador1@ayed.com", "111222"]]

    mod = Moderador()
    mod.estado = True
    mod.cant_aceptados = 0
    mod.cant_ignorados = 0

    for ind in range(1):
        mod.id = ind
        mod.email = MODERADORES[ind][0]
        mod.password = MODERADORES[ind][1]

        formatear_moderador(mod)
        pickle.dump(mod, ar_lo_moderadores)

    ar_lo_moderadores.flush()


"""
reportes: Arreglo de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
"""


def inicializar_reportes():
    global ar_lo_reportes, ar_fi_reportes

    ar_lo_reportes = open(ar_fi_reportes, "w+b")
    ar_lo_reportes.seek(0)

    REPORTES = [
        [0, 1, "Motivo 0"],
        [1, 2, "Motivo 1"],
        [2, 3, "Motivo 2"],
    ]

    re = Reporte()
    re.estado = 0

    for ind in range(3):
        re.id = ind
        re.id_reportante = REPORTES[ind][0]
        re.id_reportado = REPORTES[ind][1]
        re.razon = REPORTES[ind][2]
        formatear_reporte(re)
        pickle.dump(re, ar_lo_reportes)

    ar_lo_reportes.flush()


def mostrar_likes():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    like = Like()
    ar_lo_likesEstudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)

    while ar_lo_likesEstudiantes.tell() < tam_ar:
        like: Like = pickle.load(ar_lo_likesEstudiantes)
        print(f"Remitente {like.remitente}, Destinatario: {like.destinatario}")
    test()


"""
me_gusta: Arreglo multi de 8x8 de bool
"""


def inicializar_likes():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    ar_lo_likesEstudiantes = open(ar_fi_likesEstudiantes, "w+b")
    ar_lo_likesEstudiantes.seek(0)

    cant_est = contar_estudiantes()

    like = Like()

    for id_remitente in range(cant_est):
        for id_destinatario in range(cant_est):
            if id_destinatario != id_remitente and randint(0, 100) > 60:
                like.destinatario = id_destinatario
                like.remitente = id_remitente

                pickle.dump(like, ar_lo_likesEstudiantes)

    ar_lo_likesEstudiantes.flush()


def inicializar_administradores():
    global ar_lo_administradores, ar_fi_administradores

    ar_lo_administradores = open(ar_fi_administradores, "w+b")
    ar_lo_administradores.seek(0)

    ADMINISTRADORES = [["administrador1@ayed.com", "111222"]]

    ad = Administrador()
    ad.estado = True

    for ind in range(1):
        ad.id = ind
        ad.email = ADMINISTRADORES[ind][0]
        ad.password = ADMINISTRADORES[ind][1]

        formatear_administrador(ad)
        pickle.dump(ad, ar_lo_administradores)

    ar_lo_administradores.close()
    ar_lo_administradores = open(ar_fi_administradores, "rb")


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


def validar_email(email: str) -> bool:
    global ar_lo_estudiantes, ar_lo_moderadores, ar_lo_administradores, ar_fi_estudiantes, ar_fi_moderadores, ar_fi_administradores

    pos = buscar_id_usuario_por_email(email, ar_lo_estudiantes, ar_fi_estudiantes)

    if pos == -1:
        pos = buscar_id_usuario_por_email(email, ar_lo_moderadores, ar_fi_moderadores)

    if pos == -1:
        pos = buscar_id_usuario_por_email(
            email, ar_lo_administradores, ar_fi_administradores
        )

    return pos == -1


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


def buscar_id_usuario_por_email(
    email: str, datos: io.BufferedRandom, archivo: str
) -> int:
    id_usua = -1

    datos.seek(0)
    tam_ar = os.path.getsize(archivo)

    while datos.tell() < tam_ar and id_usua == -1:
        reg = pickle.load(datos)

        if reg.email.strip() == email:
            id_usua = reg.id

    return id_usua


def validar_login(
    id_user: int, email: str, password: str, archivo: io.BufferedRandom
) -> bool:
    tam_reg = obtener_largo_registro(archivo)
    archivo.seek(tam_reg * id_user, 0)

    reg = pickle.load(archivo)

    return (
        reg.email.strip() == email
        and reg.password.strip() == password
        and bool(reg.estado)
    )


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

    datos = [ar_lo_estudiantes, ar_lo_moderadores, ar_lo_administradores]
    archivos = [ar_fi_estudiantes, ar_fi_moderadores, ar_fi_administradores]

    while intentos > 0 and acceso_valido[0] == -1:
        email = input("Ingrese su email: ")
        password = getpass("Ingrese su contraseña: ")
        id_usua = -1
        tipo_usua = 0

        while id_usua == -1 and tipo_usua < 3:
            id_usua = buscar_id_usuario_por_email(
                email, datos[tipo_usua], archivos[tipo_usua]
            )

            if id_usua == -1:
                tipo_usua = tipo_usua + 1

        if id_usua != -1 and validar_login(id_usua, email, password, datos[tipo_usua]):
            acceso_valido[0] = id_usua
            acceso_valido[1] = tipo_usua
        else:
            limpiar_consola()
            intentos = intentos - 1
            print(f"Datos incorrectos. Intentos restantes: {intentos}\n")

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

    limpiar_consola()
    while not registrado and decision != "N":
        print("\n........Registro........\n")

        email = ingresar_propiedad("email")
        password = ingresar_contrasenia()
        rol = input("Ingrese el rol estudiante(E) o moderador(M). (E/M): ").upper()

        while rol != "E" and rol != "M":
            print("\nNo es un rol válido.")
            rol = input("ingrese E (Estudiante) o M (Moderador): ")

        if rol == "E":
            registrado = registrar_estudiante(email, password)
        elif rol == "M":
            registrado = registrar_moderador(email, password)

        if not registrado:
            decision = input("\nIntentar registrarse nuevamente. S/N ").upper()
            decision = validar_continuacion(decision)

    limpiar_consola()


### Estudiante ###


def contar_estudiantes():
    global ar_fi_estudiantes, ar_lo_estudiantes

    cant = 0

    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    while ar_lo_estudiantes.tell() < tam_ar:
        pickle.load(ar_lo_estudiantes)
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


def test():
    input("test")


def registrar_estudiante(email: str, password: str) -> bool:
    global ar_lo_estudiantes

    registrado = False

    if validar_email(email):
        print("El email ingresado ya está en uso.")
    else:
        cant_est = contar_estudiantes()

        ar_lo_estudiantes.seek(0, 2)

        nuevo_est = Estudiante()
        nuevo_est.id = cant_est
        nuevo_est.email = email
        nuevo_est.password = password
        nuevo_est.nombre = ingresar_propiedad(PROPS_ESTUDIANTE[0])
        nuevo_est.fecha_nac = ingresar_propiedad(PROPS_ESTUDIANTE[1])
        nuevo_est.biografia = ingresar_propiedad(PROPS_ESTUDIANTE[2])
        nuevo_est.hobbies = ingresar_propiedad(PROPS_ESTUDIANTE[3])
        nuevo_est.genero = ingresar_propiedad(PROPS_ESTUDIANTE[4])
        nuevo_est.ciudad = ingresar_propiedad(PROPS_ESTUDIANTE[5])
        nuevo_est.pais = ingresar_propiedad(PROPS_ESTUDIANTE[6])
        nuevo_est.estado = True

        formatear_estudiante(nuevo_est)
        pickle.dump(nuevo_est, ar_lo_estudiantes)

        ar_lo_estudiantes.flush()

        registrado = True
        print("\nRegistro exitoso!!!")

    input("Presione Enter para continuar...")

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


def contar_estudiantes_activos() -> int:
    global ar_lo_estudiantes, ar_fi_estudiantes

    cant = 0
    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    while ar_lo_estudiantes.tell() < tam_ar:
        est: Estudiante = pickle.load(ar_lo_estudiantes)

        if est.estado:
            cant = cant + 1

    return cant


"""
me_gusta: Arreglo multi de 8x8 de bool
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
cant, est_id, ind: int
"""


def contar_estudiantes_activos_no_matcheados(est_id: int) -> int:
    global ar_lo_estudiantes, ar_lo_likesEstudiantes, ar_fi_estudiantes, ar_fi_likesEstudiantes

    cant = 0
    tam_ar_est = os.path.getsize(ar_fi_estudiantes)
    tam_ar_likes = os.path.getsize(ar_fi_likesEstudiantes)

    ar_lo_estudiantes.seek(0)
    ar_lo_likesEstudiantes.seek(0)

    pos_est = ar_lo_estudiantes.tell()
    pos_like = ar_lo_likesEstudiantes.tell()

    # while pos_est < tam_ar_est:
    # while pos_like < tam_ar_likes:
    #     if ind != est_id and estados[ind] and not me_gusta[est_id][ind]:
    #     cant = cant + 1

    # ind = ind + 1

    return cant


"""
estudiantes: Arreglo multi de 9x8 de string
ind: int
nombre: string
"""


def obtener_id_estudiante_por_nombre(nombre: str) -> int:
    ind = 0

    # while ind < 8 and estudiantes[ind][2] != nombre:
    #     ind = ind + 1

    return ind


"""
estudiantes: Arreglo multi de 9x8 de string
est_id, ind: int
"""


def obtener_nombre_estudiante_por_id(est_id: int) -> str:
    global ar_lo_estudiantes

    tam_reg = obtener_largo_registro(ar_lo_estudiantes)

    ar_lo_estudiantes.seek(tam_reg * est_id, 0)
    est: Estudiante = pickle.load(ar_lo_estudiantes)

    return est.nombre


"""
estados: Arreglo de 0 a 7 de bool
est_id: int
opc: string
"""


def eliminar_perfil(est_id: int):
    print("\n")
    opc = input("¿Desea eliminar su perfil? (S/N) ").upper()
    opc = validar_continuacion(opc)

    if opc == "S":
        est = obtener_estudiante_por_id(est_id)
        est.estado = False

        actualizar_estudiante(est)
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


def crear_reporte(reportante_id: int, reportado_id: int):
    global ar_lo_reportes

    r = Reporte()

    motivo = input("Motivo:\n\t")

    while motivo == "":
        print("Debe ingresar el motivo del reporte.")
        motivo = input("Por favor. Ingrese el motivo:\n\t")

    r.id = contar_reportes()
    r.id_reportante = reportante_id
    r.id_reportado = reportado_id
    r.razon = motivo
    r.estado = 0

    formatear_reporte(r)

    ar_lo_reportes.seek(0, 2)
    pickle.dump(r, ar_lo_reportes)
    ar_lo_reportes.flush()

    print("Reporte generado con éxito.")


def reportar_candidato(est_id: int):
    decision = ""

    limpiar_consola()
    while decision != "N":
        reportado = input("Ingrese el nombre o el id del candidato: ")

        if not reportado.isdigit():
            est_repor = obtener_estudiante_por_nombre(reportado)
        else:
            est_repor = obtener_estudiante_por_id(int(reportado))

        if est_repor.id == -1 or not est_repor.estado or est_repor.id == est_id:
            print("El usuario ha reportar no es válido.\n")
        else:
            limpiar_consola()
            opc = input(
                "Seguro que desea continuar con reporte del candidato. S/N "
            ).upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                crear_reporte(est_id, est_repor.id)

                input("Presione Enter para continuar... ")
                decision = input("\nGenerar un nuevo reporte. S/N: ").upper()
                decision = validar_continuacion(decision)


"""
estudiantes: Arreglo multi de 9x8 de string
est_id, ind: int
"""


def mostrar_datos_estudiante(est: Estudiante):
    fec = formatear_fecha_espaniol(est.fecha_nac)

    print("Datos\n")
    print(f"Nombre: {est.nombre}")
    print(f"Fecha de nacimiento: {fec}")
    print(f"Biografía: {est.biografia}")
    print(f"Hobbies: {est.hobbies}")

    if est.genero == GENERO[0]:
        genero = "Femenino"
    else:
        genero = "Masculino"
    print(f"Género: {genero}")
    print(f"Ciudad: {est.ciudad}")
    print(f"País: {est.pais}")


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
est_id: int
opc: string
"""


def manejador_submenu_gestionar_perfil(est_id: int):
    opc = ""
    esta_borrado = False

    while opc != "c" and not esta_borrado:
        limpiar_consola()
        print("........Gestionar Perfil........\n")
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil")
        print("c. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b" and opc != "c":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            editar_datos_estudiante(est_id)
        elif opc == "b":
            eliminar_perfil(est_id)
            esta_borrado = True


"""
estudiantes: Arreglo multi de 9x8 de string
nombre: string
est_id: int
"""


def validar_nombre(nom: str) -> str:
    est = obtener_estudiante_por_nombre(nom)

    while est.id == -1:
        print("No existe el estudiante", nom)
        nom = input("Ingrese un nombre de estudiante: ")
        est = obtener_estudiante_por_nombre(nom)

    return nom


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
formato_espaniol_nacimiento: string
edad, est_id, ind: int
"""


def tiene_like(id_remitente: int, id_destinatario: int) -> bool:
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    ar_lo_likesEstudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    like: Like = pickle.load(ar_lo_likesEstudiantes)
    tiene = like.remitente == id_remitente and like.destinatario == id_destinatario

    while ar_lo_likesEstudiantes.tell() < tam_ar and not tiene:
        like = pickle.load(ar_lo_likesEstudiantes)
        tiene = like.remitente == id_remitente and like.destinatario == id_destinatario

    return tiene


def ver_perfil_estudiantes(est_id: int):
    global ar_lo_estudiantes, ar_fi_estudiantes, ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    limpiar_consola()

    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    ar_lo_likesEstudiantes.seek(0)

    while ar_lo_likesEstudiantes.tell() < os.path.getsize(ar_fi_likesEstudiantes):
        like: Like = pickle.load(ar_lo_likesEstudiantes)
        print(like.__dict__)
    while ar_lo_estudiantes.tell() < tam_ar:
        est: Estudiante = pickle.load(ar_lo_estudiantes)

        if est.id != est_id and est.estado:
            edad = calcular_edad(est.fecha_nac)
            formato_espaniol_nacimiento = formatear_fecha_espaniol(est.fecha_nac)

            print("Nombre:", est.nombre)
            print("Fecha de nacimiento:", formato_espaniol_nacimiento)
            print("Edad:", edad)
            print(f"Biografía:\n\t{est.biografia}")
            print(f"Hobbies:\n\t{est.hobbies}")
            print(f"Ciudad: {est.ciudad}")
            print(f"País: {est.pais}")

            if tiene_like(est_id, est.id):
                print("Has dado like ✔️")
            else:
                print("No le has dado like ❌")

            print("\n")


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
est_id, match_id: int
decision, nombre_estudiante: string
"""


def crear_like(remitente_id, destinatario_id):
    global ar_lo_likesEstudiantes

    ar_lo_likesEstudiantes.seek(0, 2)

    l = Like()
    l.remitente = remitente_id
    l.destinatario = destinatario_id

    pickle.dump(l, ar_lo_likesEstudiantes)
    ar_lo_likesEstudiantes.flush()
    ordenar_likes()


def marcar_match(est_id: int):
    decision = "S"

    if decision == "S":
        est_nom = input(
            "\nIngrese el nombre del estudiante con el que quiere hacer matcheo: "
        )

        est_nom = validar_nombre(est_nom)
        est_match = obtener_estudiante_por_nombre(est_nom)
        match_id = est_match.id

        if tiene_like(est_id, match_id):
            print("\nYa tiene match con", est_nom)
        else:
            crear_like(est_id, match_id)

            limpiar_consola()
            ver_perfil_estudiantes(est_id)
            print("Se envío el match a", est_nom)

        input("Presione Enter para continuar... ")


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
est_id: int
decision, opc: string
realizo_matcheo: bool
"""


def manejador_matcheo_estudiantes(est_id: int):
    opc = ""

    ver_perfil_estudiantes(est_id)

    decision = input(
        "Le gustaría en un futuro hacer matcheo con algún estudiante. (S/N) "
    ).upper()

    while decision != "S" and decision != "N":
        decision = input("Desea hacer matcheo con algún estudiante S o N: ").upper()

    while opc != "N" and decision != "N":
        ver_perfil_estudiantes(est_id)
        marcar_match(est_id)

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


def manejador_submenu_gestionar_candidatos(est_id: int):
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
            manejador_matcheo_estudiantes(est_id)

        if opc == "b":
            reportar_candidato(est_id)


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


def verificar_longitud_cadena(cad: str, long: int) -> bool:
    return len(cad) == long


"""
estudiantes: Arreglo multi de 9x8 de string
est_id: int
opc, valor: str
"""


def editar_datos_estudiante(est_id: int):
    global ar_lo_estudiantes, ar_fi_estudiantes

    opc = ""
    est = obtener_estudiante_por_id(est_id)
    tam_reg = obtener_largo_registro(ar_lo_estudiantes)

    while opc != "n":
        ar_lo_estudiantes.seek(est_id * tam_reg, 0)

        limpiar_consola()
        mostrar_datos_estudiante(est)

        print("\n\n........Actualizar perfil........\n")
        print("a. Cambiar fecha de nacimiento")
        print("b. Editar biografía")
        print("c. Editar hobbies")
        print("d. Cambiar género")
        print("e. Cambiar ciudad")
        print("f. Cambiar país")
        print("n. Finalizar\n")

        opc = input("Seleccione una opción: ")

        print("\n")
        while opc < "a" and "f" < opc and opc != "n":
            print("No es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        match opc:
            case "a":
                valor = solicitar_fecha_nacimiento()
                est.fecha_nac = valor
            case "b":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[2])
                est.biografia = valor
            case "c":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[3])
                est.hobbies = valor
            case "d":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[4])
                est.genero = valor
            case "e":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[5])
                est.ciudad = valor
            case "f":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[6])
                est.pais = valor

        formatear_estudiante(est)
        pickle.dump(est, ar_lo_estudiantes)
        ar_lo_estudiantes.flush()


"""
estudiantes: Arreglo de multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
me_gusta: Arreglo multi de 8x8 de bool
cant_estudiantes, est_id, ind, likes_dados, likes_recibidos, matches: int
like_dado, like_recibido: bool
porcentaje: float
"""


def buscar_like(like: Like) -> int:
    global ar_lo_likesEstudiantes, ar_fi_estudiantes

    tam_re = obtener_largo_registro(ar_lo_likesEstudiantes)
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    inf = 0
    sup = tam_ar // tam_re
    med = (inf + sup) // 2

    pos = med
    ar_lo_likesEstudiantes.seek(med * tam_re, 0)
    l: Like = pickle.load(ar_lo_likesEstudiantes)

    while inf < sup and (
        l.destinatario != like.destinatario or l.remitente != like.remitente
    ):
        if l.remitente > like.remitente or (
            l.remitente == like.remitente and l.destinatario > like.destinatario
        ):
            sup = med - 1
        elif l.remitente < like.remitente or (
            l.remitente == like.remitente and l.destinatario < like.destinatario
        ):
            inf = med + 1

        med = (inf + sup) // 2
        pos = med
        ar_lo_likesEstudiantes.seek(med * tam_re, 0)
        l = pickle.load(ar_lo_likesEstudiantes)

    if l.destinatario != like.destinatario or l.remitente != like.remitente:
        pos = -1

    return pos


def buscar_primer_like(est_id: int) -> int:
    global ar_lo_likesEstudiantes, ar_fi_estudiantes

    like = Like()
    tam_re = obtener_largo_registro(ar_lo_likesEstudiantes)
    ar_lo_likesEstudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    like: Like = pickle.load(ar_lo_likesEstudiantes)
    pos = ar_lo_likesEstudiantes.tell()

    while ar_lo_likesEstudiantes.tell() < tam_ar and like.remitente != est_id:
        like: Like = pickle.load(ar_lo_likesEstudiantes)
        pos = ar_lo_likesEstudiantes.tell()

    if like.remitente != est_id:
        pos = -1
    else:
        pos = pos - tam_re

    return pos


def ordenar_likes():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    tam_re = obtener_largo_registro(ar_lo_likesEstudiantes)
    cant_re = tam_ar // tam_re

    for i in range(cant_re - 2):
        for j in range(i + 1, cant_re - 1):
            ar_lo_likesEstudiantes.seek(i * tam_re, 0)
            like_1: Like = pickle.load(ar_lo_likesEstudiantes)

            ar_lo_likesEstudiantes.seek(j * tam_re, 0)
            like_2: Like = pickle.load(ar_lo_likesEstudiantes)

            if (
                like_1.remitente > like_2.remitente
                or like_1.destinatario > like_2.destinatario
            ):
                ar_lo_likesEstudiantes.seek(i * tam_re)
                pickle.dump(like_2, ar_lo_likesEstudiantes)
                ar_lo_likesEstudiantes.seek(j * tam_re, 0)
                pickle.dump(like_1, ar_lo_likesEstudiantes)

    ar_lo_likesEstudiantes.flush()


def reportes_estadisticos_estudiante(est_id: int):
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    like_dados = 0
    like_recibidos = 0
    matches = 0

    pri_l_est = buscar_primer_like(est_id)

    if pri_l_est != -1:
        ar_lo_likesEstudiantes.seek(pri_l_est, 0)
        like: Like = pickle.load(ar_lo_likesEstudiantes)
        pos = ar_lo_likesEstudiantes.tell()

        while like.remitente == est_id:
            est_destinatario = obtener_estudiante_por_id(like.destinatario)

            if est_destinatario.estado:
                if tiene_like(like.destinatario, est_id):
                    matches = matches + 1
                else:
                    like_dados = like_dados + 1

            ar_lo_likesEstudiantes.seek(pos)
            pos = ar_lo_likesEstudiantes.tell()
            like: Like = pickle.load(ar_lo_likesEstudiantes)

        ar_lo_likesEstudiantes.seek(0)
        tam_ar = os.path.getsize(ar_fi_likesEstudiantes)

        while ar_lo_likesEstudiantes.tell() < tam_ar:
            like: Like = pickle.load(ar_lo_likesEstudiantes)
            pos = ar_lo_likesEstudiantes.tell()

            if like.destinatario == est_id and not tiene_like(like.remitente, est_id):
                like_recibido = like_recibido + 1

            ar_lo_likesEstudiantes.seek(pos)
            like: Like = pickle.load(ar_lo_likesEstudiantes)

    cant_est_act = contar_estudiantes_activos()
    porcentaje = matches / (cant_est_act - 1) * 100

    limpiar_consola()
    print(f"Matcheados sobre el % posible: {porcentaje:.1f}%")
    print("Likes dados y no recibidos:", like_dados)
    print("Likes recibidos y no respondidos:", like_recibidos)
    input("Presiona Enter para volver al menú... ")


def obtener_estudiante_por_nombre(nom_est: str) -> Estudiante:
    global ar_lo_estudiantes, ar_fi_estudiantes

    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    est = Estudiante()
    est: Estudiante = pickle.load(ar_lo_estudiantes)

    while ar_lo_estudiantes.tell() < tam_ar and est.nombre.strip() != nom_est:
        est: Estudiante = pickle.load(ar_lo_estudiantes)

    if est.nombre.strip() != nom_est:
        est.id = -1

    desformatear_estudiante(est)
    return est


def obtener_estudiante_por_id(id_est: int) -> Estudiante:
    global ar_lo_estudiantes

    tam_reg = obtener_largo_registro(ar_lo_estudiantes)
    ar_lo_estudiantes.seek(id_est * tam_reg, 0)

    est = Estudiante()
    est: Estudiante = pickle.load(ar_lo_estudiantes)
    desformatear_estudiante(est)

    return est


def actualizar_estudiante(est: Estudiante):
    global ar_lo_estudiantes

    tam_reg = obtener_largo_registro(ar_lo_estudiantes)
    ar_lo_estudiantes.seek(tam_reg * est.id, 0)

    formatear_estudiante(est)

    pickle.dump(est, ar_lo_estudiantes)
    ar_lo_estudiantes.flush()


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
decision, estudiante, opc: string
est_id: int
"""


def desactivar_estudiante():
    global ar_lo_estudiantes

    decision = ""
    while decision != "N":
        limpiar_consola()
        dato_est = input("Ingrese el ID o el nombre del usuario: ")
        est = Estudiante()

        if not dato_est.isdigit():
            est = obtener_estudiante_por_nombre(dato_est)
        else:
            est = obtener_estudiante_por_id(int(dato_est))

        if est.id == -1:
            print("El usuario no existe.\n")
        elif not est.estado:
            print("El usuario ya está desactivado.\n")
        else:
            limpiar_consola()
            opc = input(
                "Seguro que desea continuar con la desactivación del usuario. S/N "
            ).upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                est.estado = False

                actualizar_estudiante(est)

                ar_lo_estudiantes.seek(0)
                est: Estudiante = pickle.load(ar_lo_estudiantes)

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

        # print(f"{ind + 1}. {obtener_nombre_estudiante_por_id(est_id, estudiantes[:])}")


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

    # nombre_match = obtener_nombre_estudiante_por_id()
    pos_match = candidatos[pos_elegido][0]
    me_gusta[usuario_id][pos_match] = True

    # print("\nTu match es la persona", nombre_match)


"""
estudiantes: Arreglo multi de 9x8 de string
me_gusta: Arreglo multi de 8x8 de bool
candidatos: Arreglo multi de 2x3 de int
estados: Arreglo de 0 a 7 de bool
valores_eleccion_candidatos: Arreglo de 0 a 2 de int
continuar, valor: string
cant_est_posibles, probabilidad_ingresada, probabilidad_match_1, probabilidad_match_2, probabilidad_match_3, usuario_id: int
"""


def ruleta(est_id: int):
    cant_est_posibles = contar_estudiantes_activos_no_matcheados(est_id)

    # if cant_est_posibles < 3:
    #     print("No hay suficientes estudiantes activos para esta función.")
    # else:
    #     continuar = ""

    #     while continuar != "N" and cant_est_posibles >= 3:
    #         limpiar_consola()

    #         candidatos = [[-1] * 2 for n in range(3)]
    #         candidatos = obtener_candidatos(est_id)

    #         print("........RULETA........")
    #         print(
    #             "A continuación, se le pedirá ingresar la probabilidad de matcheo con tres estudiantes."
    #         )
    #         print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

    #         while calcular_probabilidad_total_candidatos(candidatos[:]) != 100:
    #             mostrar_candidatos(candidatos[:], estudiantes[:])

    #             print("\n")
    #             for probabilidad_ingresada in range(3):
    #                 valor = input(
    #                     f"Ingresar la probabilidad del estudiante {probabilidad_ingresada + 1}: "
    #                 )

    #                 while not valor.isnumeric():
    #                     valor = input("Por favor ingrese un valor numérico entero: ")

    #                 candidatos[probabilidad_ingresada][1] = int(valor)

    #             probabilidad_total = calcular_probabilidad_total_candidatos(
    #                 candidatos[:]
    #             )

    #             if probabilidad_total != 100:
    #                 limpiar_consola()
    #                 print(
    #                     "La probabilidad total debe ser igual a 100 y el introducido es",
    #                     probabilidad_total,
    #                     ".",
    #                 )
    #                 print("Vuelva a introducir los valores.\n")

    #         valores_eleccion_candidatos = [0] * 3

    #         calcular_eleccion_candidatos(valores_eleccion_candidatos, candidatos[:])
    #         matchear_candidato(
    #             est_id,
    #             valores_eleccion_candidatos[:],
    #             candidatos[:],
    #             me_gusta,
    #             estudiantes[:],
    #         )

    #         continuar = input("Usar la ruleta nuevamente. S/N ").upper()
    #         continuar = validar_continuacion(continuar)
    #         cant_est_posibles = contar_estudiantes_activos_no_matcheados(
    #             est_id, estudiantes[:], estados[:], me_gusta[:]
    #         )

    #     if cant_est_posibles < 3 and continuar == "S":
    #         print("No hay suficientes estudiantes activos para esta función.")
    #         input("Presione Enter para volver al inicio... ")


### Reporte ###

"""
reportes: Arreglo multi de 3x40 de int
ind: int
"""


def contar_reportes() -> int:
    global ar_lo_reportes, ar_fi_reportes

    tam_reg = obtener_largo_registro(ar_lo_reportes)
    tam_ar = os.path.getsize(ar_fi_reportes)

    return tam_ar // tam_reg


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de sring
nombre_reportante, nombre_reportado: string
reporte_id: int
"""


def mostrar_detalle_reporte(rep: Reporte, nom_reportante: str, nom_reportado: str):
    print(f"........Reporte {rep.id}........\n")
    print("Reportante:", nom_reportante)
    print("Reportado:", nom_reportado)
    print(f"Motivo:\n\t{rep.razon}\n\n")


def actualizar_reporte(rep: Reporte):
    global ar_lo_reportes

    tam_reg = obtener_largo_registro(ar_lo_reportes)
    ar_lo_reportes.seek(rep.id * tam_reg, 0)

    formatear_reporte(rep)

    pickle.dump(rep, ar_lo_reportes)
    ar_lo_reportes.flush()


"""
reportes: Arreglo multi de 3x40 de int
reporte_id: int
"""


def ignorar_reporte(re: Reporte):
    re.estado = 2

    actualizar_reporte(re)
    print("\nProcesado el reporte", re.id)
    print("El reporte fue ignorado.\n")


def actualizar_reportes(id_reportado: int):
    global ar_lo_reportes, ar_fi_reportes

    ar_lo_reportes.seek(0)
    tam_ar = os.path.getsize(ar_fi_reportes)

    while ar_lo_reportes.tell() < tam_ar:
        re: Reporte = pickle.load(ar_lo_reportes)

        if re.id_reportado == id_reportado:
            re.estado = 2
            actualizar_reporte(re)


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
reportes: Arreglo multi de 3x40 de int
cant_reportes, ind, reporte_id, reportado_id: int
nombre_reportado: string
"""


def bloquear_reportado(pos_re: int, est: Estudiante, re: Reporte):
    global ar_lo_reportes, ar_fi_reportes

    pos = pos_re
    est.estado = False
    actualizar_estudiante(est)

    print("Procesado el reporte", re.id)
    print(f"El reportado {est.nombre} fue bloqueado.")

    tam_ar = os.path.getsize(ar_fi_reportes)
    ar_lo_reportes.seek(pos_re, 0)
    while pos < tam_ar:
        r: Reporte = pickle.load(ar_lo_reportes)
        pos = ar_lo_reportes.tell()
        if r.id_reportado == re.id_reportado and r.estado == 0:
            r.estado = 2
            actualizar_reporte(r)


"""
reportes: Arreglo multi de 3x40 de int
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
opc: string
ind, reportado_id, reporte_id: int
"""


def obtener_moderador_por_id(mod_id: int):
    global ar_lo_moderadores

    tam_re = obtener_largo_registro(ar_lo_moderadores)
    ar_lo_moderadores.seek(mod_id * tam_re, 0)
    mod: Moderador = pickle.load(ar_lo_moderadores)

    return mod


def incrementar_reporte_ignorado(usua_id: int):
    mod = obtener_moderador_por_id(usua_id)
    mod.cant_ignorados = mod.cant_ignorados + 1

    pickle.dump(mod, ar_lo_moderadores)
    ar_lo_moderadores.flush()


def incrementar_reporte_aceptado(usua_id: int):
    mod = obtener_moderador_por_id(usua_id)
    mod.cant_aceptados = mod.cant_aceptados + 1

    pickle.dump(mod, ar_lo_moderadores)
    ar_lo_moderadores.flush()


def procesar_reporte(pos_re: int, est: Estudiante, usua: list[int], rep: Reporte):
    print("¿Cómo proceder?\n")
    print("1. Ignorar reporte")
    print("2. Bloquear al reportado")

    opc = input("\n\nSeleccione una opción: ")

    while opc != "1" and opc != "2":
        print("\nNo es una opción válida.")
        opc = input("Ingrese una opción válida: ")

    if opc == "1":
        ignorar_reporte(rep)
        if usua[1] == 1:
            incrementar_reporte_ignorado(usua[0])
    else:
        bloquear_reportado(pos_re, est, rep)
        if usua[1] == 1:
            incrementar_reporte_aceptado(usua[0])


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


def ver_reportes(usua: list[int]):
    global ar_lo_reportes, ar_fi_reportes

    opc = ""

    ar_lo_reportes.seek(0)
    tam_ar = os.path.getsize(ar_fi_reportes)

    pos = 0
    while pos < tam_ar and opc != "N":
        rep: Reporte = pickle.load(ar_lo_reportes)
        pos = ar_lo_reportes.tell()

        desformatear_reporte(rep)

        limpiar_consola()

        est_reportado = obtener_estudiante_por_id(rep.id_reportado)
        est_reportante = obtener_estudiante_por_id(rep.id_reportante)

        estudiantes_activos = est_reportante.estado and est_reportado.estado

        if estudiantes_activos and rep.estado == 0:
            mostrar_detalle_reporte(rep, est_reportante.nombre, est_reportado.nombre)
            procesar_reporte(pos, est_reportado, usua, rep)

            opc = input("Continuar revisando reportes. (S/N) ").upper()
            opc = validar_continuacion(opc)

    if ar_lo_reportes.tell() == tam_ar:
        print("No quedan más reportes pendientes.")
        input("Presione Enter para continuar... ")


### Moderador ###

"""
moderadores: Arreglo multi de 2x4 de string
ind: int
"""


def contar_moderadores() -> int:
    global ar_lo_moderadores, ar_fi_moderadores

    ar_lo_moderadores.seek(0)
    tam_ar = os.path.getsize(ar_fi_moderadores)

    cant = 0
    while ar_lo_moderadores.tell() < tam_ar:
        mod: Moderador = pickle.load(ar_lo_moderadores)

        if mod.estado:
            cant = cant + 1

    return cant


"""
estudiantes: Arreglo multi de 9x8 de string
moderadores: Arreglo multi de 2x4 de string
email, password: string
registrado: bool
cant: int
"""


def registrar_moderador(email: str, password: str) -> bool:
    global ar_lo_moderadores

    registrado = False

    if validar_email(email):
        print("El email ingresado ya está en uso.")
    else:
        ar_lo_moderadores.seek(0, 2)

        mod: Moderador = pickle.load(ar_lo_moderadores)

        nuevo_mod = Moderador()

        nuevo_mod.id = mod.id + 1
        nuevo_mod.email = email
        nuevo_mod.password = password
        nuevo_mod.estado = True

        formatear_moderador(nuevo_mod)
        pickle.dump(nuevo_mod, ar_lo_moderadores)

        ar_lo_moderadores.flush()

        registrado = True
        print("\nRegistro exitoso!!!")

    input("Presione Enter para continuar...")

    return registrado


"""
estudiantes: Arreglo multi de 9x8 de string
estados: Arreglo de 0 a 7 de bool
opc: string
"""


# TODO: identificar si es estudiante o moderador
def eliminar_usuario():
    global ar_lo_estudiantes

    decision = ""
    while decision != "N":
        limpiar_consola()
        dato_est = input("Ingrese el ID o el nombre del usuario: ")
        est = Estudiante()

        if not dato_est.isdigit():
            est = obtener_estudiante_por_nombre(dato_est)
        else:
            est = obtener_estudiante_por_id(int(dato_est))

        if est.id == -1:
            print("El usuario no existe.\n")
        elif not est.estado:
            print("El usuario ya está desactivado.\n")
        else:
            limpiar_consola()
            opc = input(
                "Seguro que desea continuar con la desactivación del usuario. S/N "
            ).upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                est.estado = False

                actualizar_estudiante(est)

                print("Perfil borrado con exito.")

        input("Presione Enter para continuar ")

        limpiar_consola()
        decision = input("Desactivar otra cuenta. S/N: ").upper()
        decision = validar_continuacion(decision)


def dar_alta_moderador():
    limpiar_consola()
    print("\n........Registro moderador........\n")

    email = ingresar_propiedad("email")
    password = ingresar_contrasenia()
    registrar_moderador(email, password)


def manejador_submenu_gestionar_usuarios():
    opc = ""

    while opc != "b":
        limpiar_consola()
        print("........Gestionar Usuarios........\n")
        print("a. Eliminar usuario")
        print("b. Dar de alta un moderador")
        print("c. Desactivar usuario")
        print("d. Volver")

        opc = input("\nSeleccione una opción: ")

        while "a" <= opc and opc <= "d":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            eliminar_usuario()
        if opc == "b":
            dar_alta_moderador()
        if opc == "c":
            en_construccion()


def manejador_submenu_gestionar_estudiantes():
    opc = ""

    while opc != "b":
        limpiar_consola()
        print("........Gestionar Estudiantes........\n")
        print("a. Desactivar estudiante")
        print("b. Volver")

        opc = input("\nSeleccione una opción: ")

        while opc != "a" and opc != "b":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            desactivar_estudiante()


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
opc: string
"""


def manejador_submenu_gestionar_reportes(usua: list[int]):
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
            ver_reportes(usua)


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


def mostrar_menu_principal_administradores() -> str:
    limpiar_consola()

    print("\n........Home........")
    print("1. Gestionar Usuarios")
    print("2. Gestionar Reportes")
    print("3. Reportes Estadísticos")
    print("4. Puntuar candidatos")
    print("0. Salir")

    opc = input("\nSeleccione una opción: ")

    while opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "0":
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


def mostrar_menu_usuario(usuario: list[int]):
    if usuario[1] == 0:
        manejador_menu_principal_estudiante(usuario[0])
    elif usuario[1] == 1:
        manejador_menu_principal_moderador(usuario)
    elif usuario[1] == 2:
        manejador_menu_principal_administrador(usuario)


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

    est = obtener_estudiante_por_id(est_id)

    while opc != "0" and est.estado:
        opc = mostrar_menu_principal_estudiante()

        match opc:
            case "1":
                manejador_submenu_gestionar_perfil(est_id)
            case "2":
                manejador_submenu_gestionar_candidatos(est_id)
            case "3":
                manejador_submenu_matcheos()
            case "4":
                reportes_estadisticos_estudiante(est_id)
            case "5":
                # ruleta(est_id)
                en_construccion()
            case "6":
                huecos_edades()
            case "7":
                matcheos_combinados()
            case "0":
                limpiar_consola()

        est = obtener_estudiante_por_id(est_id)


"""
estudiantes: Arreglo multi de 9x8 de string
reportes: Arreglo multi de 3x40 de int
motivo_reportes: Arreglo de 0 a 39 de string
estados: Arreglo de 0 a 7 de bool
opc: string
"""


def mostrar_estudiantes():
    global ar_lo_estudiantes, ar_fi_estudiantes

    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    while ar_lo_estudiantes.tell() < tam_ar:
        est: Estudiante = pickle.load(ar_lo_estudiantes)
        print(est.__dict__)
        # print(ar_lo_estudiantes.tell())

    test()


def manejador_menu_principal_moderador(usuario: list[int]):
    opc = ""

    while opc != "0":
        opc = mostrar_menu_principal_moderadores()

        match opc:
            case "1":
                manejador_submenu_gestionar_estudiantes()
            case "2":
                manejador_submenu_gestionar_reportes(usuario)
            case "3":
                en_construccion()


def mostrar_puntuacion(est_id: int, score: list[int]):
    est: Estudiante = obtener_estudiante_por_id(est_id)

    print(f"El estudiante {est.nombre}")
    print(f"Puntuaje: {score[0]}")
    print(f"Mayor racha: {score[2]}\n")


def actualizar_puntuacion(score: list[int], like: Like):
    tiene_match = tiene_like(like.destinatario, like.remitente)

    if tiene_match and score[1] < 3:
        score[0] = score[0] + 1
        score[1] = score[1] + 1
    elif tiene_match:
        score[0] = score[0] + 2
        score[1] = score[1] + 1

        if score[1] > score[2]:
            score[2] = score[1]
    else:
        score[0] = score[0] - 1
        score[1] = 0


def puntuar_candidatos():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    ar_lo_likesEstudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)

    est_id = -1
    score = [0, 0, 0]

    limpiar_consola()
    print("........Puntuación de candidatos........\n\n")

    while ar_lo_likesEstudiantes.tell() < tam_ar:
        like: Like = pickle.load(ar_lo_likesEstudiantes)
        pos = ar_lo_likesEstudiantes.tell()

        if est_id == -1:
            est_id = like.remitente

        if est_id != like.remitente:
            mostrar_puntuacion(est_id, score)
            est_id = like.remitente
            score = [0, 0, 0]

            actualizar_puntuacion(score, like)
        else:
            actualizar_puntuacion(score, like)

        ar_lo_likesEstudiantes.seek(pos, 0)

    mostrar_puntuacion(est_id, score)
    input("\nPresiona Enter para continuar...")


def manejador_menu_principal_administrador(usuario: list[int]):
    opc = ""

    while opc != "0":
        opc = mostrar_menu_principal_administradores()

        match opc:
            case "1":
                # TODO: Hacer
                manejador_submenu_gestionar_usuarios()
            case "2":
                manejador_submenu_gestionar_reportes(usuario)
            case "3":
                en_construccion()
            case "4":
                puntuar_candidatos()


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
            case "1":
                usuario = log_in()

                if usuario[0] != -1:
                    mostrar_menu_usuario(usuario)
            case "2":
                registrar()

    limpiar_consola()
    print("¡Hasta luego!")

    finalizar_archivos()


main()
