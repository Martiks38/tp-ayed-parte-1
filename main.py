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
        self.super_like = False
        self.creditos_revelar = 0


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


"""
ar_nombre, ruta: str
"""


def crear_ruta_archivo(ruta: str, ar_nombre: str) -> str:
    return os.path.join(ruta, ar_nombre)


"""
RUTA_ARCHIVOS: str
"""
RUTA_ARCHIVOS = os.path.join(".", "archivos")


"""
ar_fi_administradores, ar_fi_estudiantes, ar_fi_likesEstudiantes, ar_fi_moderadores, ar_fi_reportes: str
"""
ar_fi_estudiantes = crear_ruta_archivo(RUTA_ARCHIVOS, "estudiantes.dat")
ar_fi_likesEstudiantes = crear_ruta_archivo(RUTA_ARCHIVOS, "likes_estudiantes.dat")
ar_fi_moderadores = crear_ruta_archivo(RUTA_ARCHIVOS, "moderadores.dat")
ar_fi_administradores = crear_ruta_archivo(RUTA_ARCHIVOS, "administradores.dat")
ar_fi_reportes = crear_ruta_archivo(RUTA_ARCHIVOS, "reportes.dat")


"""
ar_lo_estudiantes, ar_lo_likesEstudiantes, ar_lo_moderadores, ar_lo_administradores, ar_lo_reportes: BufferedRandom
"""
ar_lo_estudiantes: io.BufferedRandom
ar_lo_likesEstudiantes: io.BufferedRandom
ar_lo_moderadores: io.BufferedRandom
ar_lo_administradores: io.BufferedRandom
ar_lo_reportes: io.BufferedRandom


### Útiles ###


"""
cad: str
largo: int
"""


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
    while opc.upper() != "S" and opc.upper() != "N":
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
long: int
cad: string
"""


def validar_cadena(cad: str, long: int) -> str:
    while long < len(cad):
        print(f"No es válido debe tener como máximo {long} caracteres.\n")
        cad = input("Por favor. Vuelva a intentar: ")

    return cad


"""
like: Like
tam_ar: int
"""


# ! Borrar
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


"""
est: Estudiante
nom: string
"""


def validar_nombre(nom: str) -> str:
    est = Estudiante()
    est = obtener_estudiante_por_nombre(nom)

    while est.id == -1:
        print("No existe el estudiante", nom)
        nom = input("Ingrese un nombre de estudiante: ")
        est = obtener_estudiante_por_nombre(nom)

    return nom


"""
long: int
cad: string
"""


def verificar_longitud_cadena(cad: str, long: int) -> bool:
    return len(cad) == long


"""
cand: Arreglo de 0 a 2 de int
valores: Arreglo de 0 a 2 de int
ind: int
"""


def calcular_eleccion_candidatos(valores: list[int], cand: list[int]):
    for ind in range(3):
        valores[ind] = randint(0, 100) * cand[ind][1]


"""
cand: Arreglo de 0 a 2 de int
ind, total: int
"""


def calcular_probabilidad_total_candidatos(cand: list[int]) -> int:
    total = 0

    for ind in range(3):
        total = total + cand[ind][1]

    return total


"""
list: Arreglo de 0 a 2 de int
ind, valor: int
pertenece: boolean
"""


def pertenece_array(valor: int, lista: list[int]):
    pertenece = False
    ind = 0

    while ind < 3 and not pertenece:
        if lista[ind] == valor:
            pertenece = True

        ind = ind + 1

    return pertenece


# Fin utiles
### Registro ###


"""
est: Estudiante
"""


def formatear_estudiante(est: Estudiante):
    est.email = formatear_cadena(est.email, 32)
    est.password = formatear_cadena(est.password, 32)
    est.nombre = formatear_cadena(est.nombre, 32)
    est.biografia = formatear_cadena(est.biografia, 255)
    est.fecha_nac = formatear_cadena(est.fecha_nac, 10)
    est.hobbies = formatear_cadena(est.hobbies, 255)
    est.ciudad = formatear_cadena(est.ciudad, 32)
    est.pais = formatear_cadena(est.pais, 32)


"""
mod: Moderador
"""


def formatear_moderador(mod: Moderador):
    mod.email = formatear_cadena(mod.email, 32)
    mod.password = formatear_cadena(mod.password, 32)


"""
ad: Administrador
"""


def formatear_administrador(ad: Administrador):
    ad.email = formatear_cadena(ad.email, 32)
    ad.password = formatear_cadena(ad.password, 32)


"""
re: Reporte
"""


def formatear_reporte(re: Reporte):
    re.razon = formatear_cadena(re.razon, 255)


"""
est: Estudiante
"""


def desformatear_estudiante(est: Estudiante):
    est.email = est.email.strip()
    est.password = est.password.strip()
    est.nombre = est.nombre.strip()
    est.biografia = est.biografia.strip()
    est.hobbies = est.hobbies.strip()
    est.ciudad = est.ciudad.strip()
    est.pais = est.pais.strip()


"""
re: Reporte
"""


def desformatear_reporte(re: Reporte):
    re.razon = re.razon.strip()


"""
datos: BufferedRandom
"""


def obtener_largo_registro(datos: io.BufferedRandom) -> int:
    datos.seek(0)
    pickle.load(datos)

    return datos.tell()


### Mocks ###

"""
est: Estudiante
ESTUDIANTES: Arreglo multi de 4x9 de string
ind: int
"""


def mockear_estudiantes():
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
    est.super_like = True
    est.creditos_revelar = 1

    for ind in range(4):
        est.id = ind
        est.email = validar_cadena(ESTUDIANTES[ind][0], 32)
        est.password = validar_cadena(ESTUDIANTES[ind][1], 32)
        est.nombre = validar_cadena(ESTUDIANTES[ind][2], 32)
        est.fecha_nac = validar_cadena(ESTUDIANTES[ind][3], 10)
        est.biografia = validar_cadena(ESTUDIANTES[ind][4], 255)
        est.hobbies = validar_cadena(ESTUDIANTES[ind][5], 255)
        est.genero = validar_cadena(ESTUDIANTES[ind][6], 1)
        est.ciudad = validar_cadena(ESTUDIANTES[ind][7], 32)
        est.pais = validar_cadena(ESTUDIANTES[ind][8], 32)

        formatear_estudiante(est)
        pickle.dump(est, ar_lo_estudiantes)
        ar_lo_estudiantes.flush()


"""
mod: Moderador
MODERADORES: Arreglo multi de 2x2 de string
ind: int
"""


def mockear_moderadores():
    global ar_lo_moderadores, ar_fi_moderadores

    ar_lo_moderadores = open(ar_fi_moderadores, "w+b")
    ar_lo_moderadores.seek(0)

    MODERADORES = [["moderador1@ayed.com", "111222"], ["moderador2@ayed.com", "333444"]]

    mod = Moderador()
    mod.estado = True
    mod.cant_aceptados = 0
    mod.cant_ignorados = 0

    for ind in range(1):
        mod.id = ind
        mod.email = validar_cadena([ind][0], 32)
        mod.password = validar_cadena(MODERADORES[ind][1], 32)

        formatear_moderador(mod)
        pickle.dump(mod, ar_lo_moderadores)

    ar_lo_moderadores.flush()


"""
re: Reporte
REPORTES: Arreglo multi de 3x2 de int
MOTIVOS: Arreglo de 0 a 2 de string
ind: int
"""


def mockear_reportes():
    global ar_lo_reportes, ar_fi_reportes

    ar_lo_reportes = open(ar_fi_reportes, "w+b")
    ar_lo_reportes.seek(0)

    REPORTES = [
        [0, 1],
        [1, 2],
        [2, 3],
    ]
    MOTIVOS = ["Motivo 0", "Motivo 1", "Motivo 2"]

    re = Reporte()
    re.estado = 0

    for ind in range(3):
        re.id = ind
        re.id_reportante = REPORTES[ind][0]
        re.id_reportado = REPORTES[ind][1]
        re.razon = validar_cadena(MOTIVOS[ind], 255)
        formatear_reporte(re)
        pickle.dump(re, ar_lo_reportes)

    ar_lo_reportes.flush()


"""
like: Like
cant_est, id_destinatario, id_remitente: int
"""


def mockear_likes():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    ar_lo_likesEstudiantes = open(ar_fi_likesEstudiantes, "w+b")
    ar_lo_likesEstudiantes.seek(0)

    cant_est = contar_estudiantes()

    like = Like()

    for id_remitente in range(cant_est):
        for id_destinatario in range(cant_est):
            if id_destinatario != id_remitente and randint(0, 100) > 40:
                like.destinatario = id_destinatario
                like.remitente = id_remitente

                pickle.dump(like, ar_lo_likesEstudiantes)

    ar_lo_likesEstudiantes.flush()


"""
ad: Administrador
ADMINISTRADORES: Arreglo multi de 1x2 de string
ind: int
"""


def mockear_administradores():
    global ar_lo_administradores, ar_fi_administradores

    ar_lo_administradores = open(ar_fi_administradores, "w+b")
    ar_lo_administradores.seek(0)

    ADMINISTRADORES = [["administrador1@ayed.com", "111222"]]

    ad = Administrador()
    ad.estado = True

    for ind in range(1):
        ad.id = ind
        ad.email = validar_cadena(ADMINISTRADORES[ind][0], 32)
        ad.password = validar_cadena(ADMINISTRADORES[ind][1], 32)

        formatear_administrador(ad)
        pickle.dump(ad, ar_lo_administradores)

    ar_lo_administradores.close()
    ar_lo_administradores = open(ar_fi_administradores, "rb")


### Archivos ###


def crear_archivos():
    os.mkdir(RUTA_ARCHIVOS)

    mockear_estudiantes()
    mockear_likes()
    mockear_moderadores()
    mockear_reportes()
    mockear_administradores()


def comprobar_existencia_archivos():
    global ar_lo_estudiantes, ar_lo_likesEstudiantes, ar_lo_moderadores, ar_lo_administradores, ar_lo_reportes, ar_fi_estudiantes, ar_fi_likesEstudiantes, ar_fi_moderadores, ar_fi_administradores, ar_fi_administradores, ar_fi_reportes

    if not os.path.exists(ar_fi_estudiantes):
        mockear_estudiantes()
    else:
        ar_lo_estudiantes = open(ar_fi_estudiantes, "r+b")

    if not os.path.exists(ar_fi_likesEstudiantes):
        mockear_likes()
    else:
        ar_lo_likesEstudiantes = open(ar_fi_likesEstudiantes, "r+b")

    if not os.path.exists(ar_fi_moderadores):
        mockear_moderadores()
    else:
        ar_lo_moderadores = open(ar_fi_moderadores, "r+b")

    if not os.path.exists(ar_fi_administradores):
        mockear_administradores()
    else:
        ar_lo_administradores = open(ar_fi_administradores, "rb")

    if not os.path.exists(ar_fi_reportes):
        mockear_reportes()
    else:
        ar_lo_reportes = open(ar_fi_reportes, "r+b")


def inicializar_archivos():
    if os.path.exists(RUTA_ARCHIVOS):
        comprobar_existencia_archivos()
    else:
        crear_archivos()


def finalizar_archivos():
    global ar_lo_administradores, ar_lo_estudiantes, ar_lo_likesEstudiantes, ar_lo_moderadores, ar_lo_reportes

    ar_lo_administradores.close()
    ar_lo_estudiantes.close()
    ar_lo_likesEstudiantes.close()
    ar_lo_moderadores.close()
    ar_lo_reportes.close()


### Log in y Registro ###


"""
password: string
"""


def ingresar_contrasenia() -> str:
    password = getpass("Ingrese su contraseña: ")

    while password == "":
        password = getpass("Debe ingresar una contraseña: ")

    return password


"""
email: string
pos: int
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
datos: BufferedRandom
archivo, email: string
id_usua, tam_ar: int
"""


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


"""
archivo: BufferedRandom
email, password: string
id_user, tam_reg: int
"""


def validar_login(
    id_user: int, email: str, password: str, archivo: io.BufferedRandom
) -> bool:
    tam_reg = obtener_largo_registro(archivo)
    archivo.seek(tam_reg * id_user, 0)

    reg = pickle.load(archivo)

    return (
        reg.email.strip() == email and reg.password.strip() == password and reg.estado
    )


"""
datos: Arreglo de 0 a 2 de BufferedRandom
archivos: Arreglo de 0 a 2 de string
acceso_valido: Arreglo de 0 a 1 de int
id_usua, intentos, tipo_usua: int
email, password: string
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
        email = validar_cadena(email, 32)

        password = ingresar_contrasenia()
        password = validar_cadena(email, 32)

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


### Reporte ###


"""
r: Reporte
reportante_id, reportado_id: int
motivo: string
"""


def crear_reporte(reportante_id: int, reportado_id: int):
    global ar_lo_reportes

    r = Reporte()

    motivo = input("Motivo:\n\t")
    while motivo == "":
        print("Debe ingresar el motivo del reporte.")
        motivo = input("Por favor. Ingrese el motivo:\n\t")
        motivo = validar_cadena(motivo, 255)

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


"""
tam_ar, tam_reg: int
"""


def contar_reportes() -> int:
    global ar_lo_reportes, ar_fi_reportes

    tam_reg = obtener_largo_registro(ar_lo_reportes)
    tam_ar = os.path.getsize(ar_fi_reportes)

    return tam_ar // tam_reg


"""
rep: Reporte
nom_reportado, nom_reportante: string
"""


def mostrar_detalle_reporte(rep: Reporte, nom_reportante: str, nom_reportado: str):
    print(f"........Reporte {rep.id}........\n")
    print("Reportante:", nom_reportante)
    print("Reportado:", nom_reportado)
    print(f"Motivo:\n\t{rep.razon}\n\n")


"""
re: Reporte
"""


def ignorar_reporte(re: Reporte):
    re.estado = 2

    actualizar_reporte(re)
    print("\nProcesado el reporte", re.id)
    print("El reporte fue ignorado.\n")


"""
re: Reporte
tam_reg: int
"""


def actualizar_reporte(re: Reporte):
    global ar_lo_reportes

    tam_reg = obtener_largo_registro(ar_lo_reportes)
    ar_lo_reportes.seek(re.id * tam_reg, 0)

    formatear_reporte(re)

    pickle.dump(re, ar_lo_reportes)
    ar_lo_reportes.flush()


"""
re: Reporte
id_reportado, tam_ar: int
"""


def actualizar_reportes(id_reportado: int):
    global ar_lo_reportes, ar_fi_reportes

    ar_lo_reportes.seek(0)
    tam_ar = os.path.getsize(ar_fi_reportes)

    re = Reporte()
    while ar_lo_reportes.tell() < tam_ar:
        re: Reporte = pickle.load(ar_lo_reportes)

        if re.id_reportado == id_reportado:
            re.estado = 2
            actualizar_reporte(re)


"""
est: Estudiante
r, re: Reporte
pos, pos_re, tam_ar: int
"""


def bloquear_reportado(pos_re: int, est: Estudiante, re: Reporte):
    global ar_lo_reportes, ar_fi_reportes

    r = Reporte()
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
            ar_lo_reportes.seek(pos, 0)


### Likes ###


"""
like: Like
id_destinatario, id_remitente, tam_ar: int
tiene_l: boolean
"""


def tiene_like(id_remitente: int, id_destinatario: int) -> bool:
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    like = Like()
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)

    ar_lo_likesEstudiantes.seek(0)
    like: Like = pickle.load(ar_lo_likesEstudiantes)
    tiene_l = like.remitente == id_remitente and like.destinatario == id_destinatario

    while ar_lo_likesEstudiantes.tell() < tam_ar and not tiene_l:
        like = pickle.load(ar_lo_likesEstudiantes)
        tiene_l = (
            like.remitente == id_remitente and like.destinatario == id_destinatario
        )

    return tiene_l


"""
like: Like
est_id, pos, tam_ar, tam_re: int
"""


def buscar_primer_like(est_id: int) -> int:
    global ar_lo_likesEstudiantes, ar_fi_estudiantes

    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    tam_re = obtener_largo_registro(ar_lo_likesEstudiantes)
    ar_lo_likesEstudiantes.seek(0)

    like = Like()
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


"""
like_1, like_2: Like
cant_re, i, j, tam_ar, tam_re: int
"""


def ordenar_likes():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    tam_re = obtener_largo_registro(ar_lo_likesEstudiantes)
    cant_re = tam_ar // tam_re

    for i in range(cant_re - 2):
        for j in range(i + 1, cant_re - 1):
            ar_lo_likesEstudiantes.seek(i * tam_re, 0)
            like_1 = Like()
            like_1: Like = pickle.load(ar_lo_likesEstudiantes)

            ar_lo_likesEstudiantes.seek(j * tam_re, 0)
            like_2 = Like()
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


"""
l: Like
remitente_id, destinatario_id: int
"""


def crear_like(remitente_id: int, destinatario_id: int):
    global ar_lo_likesEstudiantes

    ar_lo_likesEstudiantes.seek(0, 2)

    l = Like()
    l.remitente = remitente_id
    l.destinatario = destinatario_id

    pickle.dump(l, ar_lo_likesEstudiantes)
    ar_lo_likesEstudiantes.flush()
    ordenar_likes()


### Estudiante ###


"""
est: Estudiante
nom_est: string
tam_ar: int
"""


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


"""
est: Estudiante
id_est, tam_ar, tam_reg: int
"""


def obtener_estudiante_por_id(id_est: int) -> Estudiante:
    global ar_lo_estudiantes, ar_fi_estudiantes

    est = Estudiante()
    tam_ar = os.path.getsize(ar_fi_estudiantes)
    tam_reg = obtener_largo_registro(ar_lo_estudiantes)

    if 0 <= id_est and id_est <= tam_ar // tam_reg:
        ar_lo_estudiantes.seek(id_est * tam_reg, 0)
        est: Estudiante = pickle.load(ar_lo_estudiantes)
        desformatear_estudiante(est)
    else:
        est.id = -1

    return est


"""
est: Estudiante
tam_reg: int
"""


def actualizar_estudiante(est: Estudiante):
    global ar_lo_estudiantes

    tam_reg = obtener_largo_registro(ar_lo_estudiantes)
    ar_lo_estudiantes.seek(tam_reg * est.id, 0)

    formatear_estudiante(est)

    pickle.dump(est, ar_lo_estudiantes)
    ar_lo_estudiantes.flush()


"""
cant, tam_ar: int
"""


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


# ! Borrar
def test():
    input("test")


"""
nuevo_est: Estudiante
email, password: string
registrado: boolean
cant_est: int
"""


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
        nuevo_est.nombre = validar_cadena(nuevo_est.nombre, 32)
        nuevo_est.fecha_nac = ingresar_propiedad(PROPS_ESTUDIANTE[1])
        nuevo_est.biografia = ingresar_propiedad(PROPS_ESTUDIANTE[2])
        nuevo_est.biografia = validar_cadena(nuevo_est.biografia, 255)
        nuevo_est.hobbies = ingresar_propiedad(PROPS_ESTUDIANTE[3])
        nuevo_est.hobbies = validar_cadena(nuevo_est.hobbies, 255)
        nuevo_est.genero = ingresar_propiedad(PROPS_ESTUDIANTE[4])
        nuevo_est.ciudad = ingresar_propiedad(PROPS_ESTUDIANTE[5])
        nuevo_est.ciudad = validar_cadena(nuevo_est.ciudad, 32)
        nuevo_est.pais = ingresar_propiedad(PROPS_ESTUDIANTE[6])
        nuevo_est.pais = validar_cadena(nuevo_est.pais, 32)
        nuevo_est.estado = True
        nuevo_est.super_like = True
        nuevo_est.creditos_revelar = 1

        formatear_estudiante(nuevo_est)
        pickle.dump(nuevo_est, ar_lo_estudiantes)

        ar_lo_estudiantes.flush()

        registrado = True
        print("\nRegistro exitoso!!!")

    input("Presione Enter para continuar...")

    return registrado


"""
est: Estudiante
cant, tam_ar: int
"""


def contar_estudiantes_activos() -> int:
    global ar_lo_estudiantes, ar_fi_estudiantes

    cant = 0
    est = Estudiante()
    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    while ar_lo_estudiantes.tell() < tam_ar:
        est: Estudiante = pickle.load(ar_lo_estudiantes)

        if est.estado:
            cant = cant + 1

    return cant


"""
est: Estudiante
dato_est, opc: string
"""


def desactivar_estudiante():
    global ar_lo_estudiantes

    est = Estudiante()
    dato_est = input("Ingrese el ID o el nombre del estudiante: ")

    if not dato_est.isdigit():
        est = obtener_estudiante_por_nombre(dato_est)
    else:
        est = obtener_estudiante_por_id(int(dato_est))

    if est.id == -1:
        print("El estudiante no existe.\n")
    elif not est.estado:
        print("El estudiante ya está desactivado.\n")
    else:
        limpiar_consola()
        opc = input(
            "Seguro que desea continuar con la desactivación del estudiante. S/N "
        ).upper()
        opc = validar_continuacion(opc)

        if opc == "S":
            est.estado = False

            actualizar_estudiante(est)

            print("Perfil borrado con exito.")


"""
cant_est_act, cant_likes, est_id, pos, tam_ar: int
cambio_est: boolean
"""


def contar_estudiantes_activos_no_matcheados(est_id: int) -> int:
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    cant_est_act = contar_estudiantes_activos() - 1
    cant_likes = 0
    pos = buscar_primer_like(est_id)
    cambio_est = False

    ar_lo_likesEstudiantes.seek(pos, 0)
    while ar_lo_likesEstudiantes.tell() < tam_ar and not cambio_est:
        like: Like = pickle.load(ar_lo_likesEstudiantes)

        if like.remitente != est_id:
            cambio_est = True
        elif tiene_like(like.destinatario, est_id):
            cant_likes = cant_likes + 1

    return cant_est_act - cant_likes


"""
est: Estudiante
est_id, tam_reg: int
"""


def obtener_nombre_estudiante_por_id(est_id: int) -> str:
    global ar_lo_estudiantes

    tam_reg = obtener_largo_registro(ar_lo_estudiantes)
    ar_lo_estudiantes.seek(tam_reg * est_id, 0)

    est = Estudiante()
    est: Estudiante = pickle.load(ar_lo_estudiantes)

    return est.nombre


"""
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
est_repor: Estudiante
est_id: int
decision, opc, reportado: string
"""


def reportar_candidato(est_id: int):
    decision = ""

    limpiar_consola()
    while decision != "N":
        reportado = input("Ingrese el nombre o el id del candidato: ")

        est_repor = Estudiante()
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
est: Estudiante
fec, genero: string
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
est: Estudiante
edad, est_id, tam_ar: int
formato_espaniol_nacimiento: string
"""


def ver_perfil_estudiantes(est_id: int):
    global ar_lo_estudiantes, ar_fi_estudiantes

    limpiar_consola()

    est = Estudiante()
    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

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
est: Estudiante
est_match: Estudiante
est_id, match_id: int
decision, est_nom: string
"""


def marcar_match(est_id: int):
    decision = "S"

    est = Estudiante()
    est: Estudiante = obtener_estudiante_por_id(est_id)

    usar_super_like = False

    if est.super_like:
        decision_super_like = input("\nUtilizar super like. (S/N)")
        decision_super_like = validar_continuacion(decision_super_like)

        usar_super_like = decision_super_like == "S"

    if decision == "S":
        est_nom = input(
            "\nIngrese el nombre del estudiante con el que quiere hacer matcheo: "
        )

        est_nom = validar_nombre(est_nom)

        est_match = Estudiante()
        est_match = obtener_estudiante_por_nombre(est_nom)
        match_id = est_match.id

        if tiene_like(est_id, match_id):
            print("\nYa tiene match con", est_nom)
        else:
            crear_like(est_id, match_id)

            if usar_super_like:
                crear_like(match_id, est_id)
                est.super_like = False

                actualizar_estudiante(est)

            limpiar_consola()
            ver_perfil_estudiantes(est_id)
            print("Se envío el match a", est_nom)

        input("Presione Enter para continuar... ")


"""
est_id: int
decision, opc: string
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
est, usua: Estudiante
like: Like
cant_mostrado, est_id, pos, tam_ar: int
"""


def revelar_candidatos(est_id: int):
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    est = Estudiante()
    usua = Estudiante()
    like = Like()

    cant_mostrado = 0
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)
    ar_lo_likesEstudiantes.seek(0)

    limpiar_consola()

    while ar_lo_likesEstudiantes.tell() < tam_ar and cant_mostrado < 3:
        like: Like = pickle.load(ar_lo_likesEstudiantes)
        pos = ar_lo_likesEstudiantes.tell()

        if like.destinatario == est_id and tiene_like(est_id, like.remitente):
            cant_mostrado = cant_mostrado + 1
            est = obtener_estudiante_por_id(like.remitente)

            print(f"Candidato {cant_mostrado}: {est.nombre}")

        ar_lo_likesEstudiantes.seek(pos, 0)

    if est.id == -1:
        print("No hay candidatos que te hayan dado like.")

    usua: Estudiante = obtener_estudiante_por_id(est_id)
    usua.creditos_revelar = usua.creditos_revelar - 1
    actualizar_estudiante(usua)
    input("\nPresiona Enter para continuar...")


"""
est: Estudiante
opc: string
est_id, tam_re: int
"""


def manejador_submenu_gestionar_candidatos(est_id: int):
    global ar_lo_estudiantes

    opc = ""

    tam_re = obtener_largo_registro(ar_lo_estudiantes)
    ar_lo_estudiantes.seek(est_id * tam_re, 0)

    est = Estudiante()
    est: Estudiante = pickle.load(ar_lo_estudiantes)

    while opc != "f":
        limpiar_consola()
        print("........Gestionar Candidatos........\n")
        print("a. Ver candidatos")
        print("b. Reportar un candidato")

        if est.creditos_revelar > 0:
            print("c. Revelar candidato")

        print("f. Volver")

        opc = input("\nSeleccione una opción: ")

        while (
            opc != "a"
            and opc != "b"
            and opc == "c"
            and opc != "f"
            and not (opc == "c" and est.creditos_revelar == 0)
        ):
            print("\nNo es una opción válida.")
            opc = input("\nSeleccione una opción: ")

        if opc == "a":
            manejador_matcheo_estudiantes(est_id)

        if opc == "b":
            reportar_candidato(est_id)

        if opc == "c":
            revelar_candidatos(est_id)

        est = obtener_estudiante_por_id(est_id)


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
est: Estudiante
est_id, tam_reg: int
opc, valor: str
"""


def editar_datos_estudiante(est_id: int):
    global ar_lo_estudiantes, ar_fi_estudiantes

    est = Estudiante()
    est = obtener_estudiante_por_id(est_id)
    tam_reg = obtener_largo_registro(ar_lo_estudiantes)

    opc = ""

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
                est.biografia = validar_cadena(valor, 255)
            case "c":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[3])
                est.hobbies = validar_cadena(valor, 255)
            case "d":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[4])
                est.genero = valor
            case "e":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[5])
                est.ciudad = validar_cadena(valor, 32)
            case "f":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[6])
                est.pais = validar_cadena(valor, 32)

        formatear_estudiante(est)

        pickle.dump(est, ar_lo_estudiantes)
        ar_lo_estudiantes.flush()


"""
like: Like
est_destinatario: Estudiante
cant_est_act, est_id, like_dados, like_recibidos, matches, pos, pri_l_est, tam_ar: int
porcentaje: float
"""


def reportes_estadisticos_estudiante(est_id: int):
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    like_dados = 0
    like_recibidos = 0
    matches = 0

    pri_l_est = buscar_primer_like(est_id)

    if pri_l_est != -1:
        ar_lo_likesEstudiantes.seek(pri_l_est, 0)

        like = Like()
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
                like_recibidos = like_recibidos + 1

            ar_lo_likesEstudiantes.seek(pos)
            like: Like = pickle.load(ar_lo_likesEstudiantes)

    cant_est_act = contar_estudiantes_activos()
    porcentaje = matches / (cant_est_act - 1) * 100

    limpiar_consola()
    print(f"Matcheados sobre el % posible: {porcentaje:.1f}%")
    print("Likes dados y no recibidos:", like_dados)
    print("Likes recibidos y no respondidos:", like_recibidos)
    input("Presiona Enter para volver al menú... ")


"""
cand: Arreglo de 0 a 2 de int
ind: int
nom: string
"""


def mostrar_candidatos(cand: list[int]):
    for ind in range(3):
        nom = obtener_nombre_estudiante_por_id(cand[ind])

        print(f"{ind + 1}. {nom}")


"""
valores: Arreglo de 0 a 2 de int
ind, mayor, pos: int
"""


def buscar_candidato_mayor_valor(valores: list[int]) -> int:
    mayor = -1
    pos = 0

    for ind in range(3):
        if valores[ind] > mayor:
            mayor = valores[ind]
            pos = ind

    return pos


"""
est: Estudiante
candidatos: Arreglo de 0 a 2 de int
cant_est, elegidos, est_id, rand_id: int
"""


def obtener_candidatos(est_id: int, candidatos: list[int]):
    cant_est = contar_estudiantes()
    elegidos = 0
    est = Estudiante()

    while elegidos < 3:
        rand_id = randint(0, cant_est - 1)
        est = obtener_estudiante_por_id(rand_id)

        if (
            est.estado
            and not tiene_like(est_id, rand_id)
            and not pertenece_array(rand_id, candidatos[:])
        ):
            rand_id = randint(0, cant_est - 1)
            elegidos = elegidos + 1


"""
like: Like
candidatos: Arreglo de 0 a 2 de int
valores: Arreglo de 0 a 2 de int
elegido_id, pos_elegido, usua_id: int
nombre_match: string
"""


def matchear_candidato(usua_id: int, candidatos: list[int], valores: list[int]):
    global ar_lo_likesEstudiantes

    ar_lo_likesEstudiantes.seek(0, 2)

    pos_elegido = buscar_candidato_mayor_valor(valores[:])
    elegido_id = candidatos[pos_elegido]
    nombre_match = obtener_nombre_estudiante_por_id(elegido_id)

    like = Like()
    like.remitente = usua_id
    like.destinatario = elegido_id
    pickle.dump(ar_lo_likesEstudiantes)

    print("\nTu match es la persona", nombre_match)


"""
puntuaciones: Arreglo de 0 a 2 de int
candidatos: Arreglo de 0 a 2 de int
valores_eleccion_candidatos: Arreglo de 0 a 2 de int
continuar, valor: string
cant_est_posibles, est_id, prob_ingresada, probabilidad_total: int
"""


def ruleta(est_id: int):
    cant_est_posibles = contar_estudiantes_activos_no_matcheados(est_id)

    if cant_est_posibles < 3:
        print("No hay suficientes estudiantes activos para esta función.")
    else:
        continuar = ""

        while continuar != "N" and cant_est_posibles >= 3:
            limpiar_consola()

            puntuaciones = [0] * 3
            candidatos = [0] * 3
            obtener_candidatos(est_id, candidatos)

            print("........RULETA........")
            print(
                "A continuación, se le pedirá ingresar la probabilidad de matcheo con tres estudiantes."
            )
            print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

            while calcular_probabilidad_total_candidatos(puntuaciones[:]) != 100:
                mostrar_candidatos(candidatos[:])

                print("\n")
                for prob_ingresada in range(3):
                    valor = input(
                        f"Ingresar la probabilidad del estudiante {prob_ingresada + 1}: "
                    )

                    while not valor.isnumeric():
                        valor = input("Por favor ingrese un valor numérico entero: ")

                    puntuaciones[prob_ingresada] = int(valor)

                probabilidad_total = calcular_probabilidad_total_candidatos(
                    puntuaciones[:]
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
                est_id,
                candidatos[:],
                valores_eleccion_candidatos[:],
            )

            continuar = input("Usar la ruleta nuevamente. S/N ").upper()
            continuar = validar_continuacion(continuar)
            cant_est_posibles = contar_estudiantes_activos_no_matcheados(est_id)

        if cant_est_posibles < 3 and continuar == "S":
            print("No hay suficientes estudiantes activos para esta función.")
            input("Presione Enter para volver al inicio... ")


### Moderador ###


"""
mod: Moderador
mod_id, tam_ar, tam_re: int
"""


def obtener_moderador_por_id(mod_id: int) -> Moderador:
    global ar_lo_moderadores, ar_fi_moderadores

    mod = Moderador()

    tam_ar = os.path.getsize(ar_fi_moderadores)
    tam_re = obtener_largo_registro(ar_lo_moderadores)

    if 0 <= mod_id and mod_id <= tam_ar // tam_re:
        ar_lo_moderadores.seek(mod_id * tam_re, 0)
        mod: Moderador = pickle.load(ar_lo_moderadores)
    else:
        mod.id = -1

    return mod


"""
mod: Moderador
usua_id: int
"""


def incrementar_reporte_ignorado(usua_id: int):
    mod = Moderador()
    mod = obtener_moderador_por_id(usua_id)
    mod.cant_ignorados = mod.cant_ignorados + 1

    pickle.dump(mod, ar_lo_moderadores)
    ar_lo_moderadores.flush()


"""
mod: Moderador
usua_id: int
"""


def incrementar_reporte_aceptado(usua_id: int):
    mod = Moderador()
    mod = obtener_moderador_por_id(usua_id)
    mod.cant_aceptados = mod.cant_aceptados + 1

    pickle.dump(mod, ar_lo_moderadores)
    ar_lo_moderadores.flush()


"""
est: Estudiante
rep: Reporte
usua: Arreglo de 0 a 1 de int
pos_re: int
opc: string
"""


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
est_reportado, est_reportante: Estudiante
rep: Reporte
usua: Arreglo de 0 a 1 de int
opc: string
pos, tam_ar: int
estudiantes_activos: boolean
"""


def ver_reportes(usua: list[int]):
    global ar_lo_reportes, ar_fi_reportes

    opc = ""

    ar_lo_reportes.seek(0)
    tam_ar = os.path.getsize(ar_fi_reportes)

    pos = 0
    while pos < tam_ar and opc != "N":
        rep = Reporte()
        rep = pickle.load(ar_lo_reportes)
        pos = ar_lo_reportes.tell()

        desformatear_reporte(rep)

        limpiar_consola()

        est_reportado = Estudiante()
        est_reportado = obtener_estudiante_por_id(rep.id_reportado)
        est_reportante = Estudiante()
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


"""
mod: Moderador
tam_reg: int
"""


def actualizar_moderador(mod: Moderador):
    global ar_lo_moderadores, ar_fi_moderadores

    tam_reg = obtener_largo_registro(ar_lo_moderadores)
    ar_lo_moderadores.seek(tam_reg * mod.id, 0)

    formatear_moderador(mod)

    pickle.dump(mod, ar_lo_moderadores)
    ar_lo_moderadores.flush()


"""
mod: Moderador
dato_mod, opc: string
"""


def desactivar_moderador():
    global ar_lo_moderadores

    mod = Moderador()
    dato_mod = input("Ingrese el ID del moderador: ")

    while not dato_mod.isdigit():
        dato_mod = input("Ingrese el ID del moderador: ")

    mod = obtener_moderador_por_id(dato_mod)

    if mod.id == -1:
        print("El moderador no existe.\n")
    elif not mod.estado:
        print("El moderador ya está desactivado.\n")
    else:
        limpiar_consola()
        opc = input(
            "Seguro que desea continuar con la desactivación del moderador. S/N "
        ).upper()
        opc = validar_continuacion(opc)

        if opc == "S":
            mod.estado = False

            actualizar_moderador(mod)

            print("Perfil borrado con exito.")

    input("Presione Enter para continuar ")


"""
mod: Moderador
cant, tam_ar: int
"""


def contar_moderadores() -> int:
    global ar_lo_moderadores, ar_fi_moderadores

    ar_lo_moderadores.seek(0)
    tam_ar = os.path.getsize(ar_fi_moderadores)

    cant = 0
    while ar_lo_moderadores.tell() < tam_ar:
        mod = Moderador()
        mod = pickle.load(ar_lo_moderadores)

        if mod.estado:
            cant = cant + 1

    return cant


"""
mod, nuevo_mod: Moderador
email, password: string
registrado: boolean
"""


def registrar_moderador(email: str, password: str) -> bool:
    global ar_lo_moderadores

    registrado = False

    if validar_email(email):
        print("El email ingresado ya está en uso.")
    else:
        ar_lo_moderadores.seek(0, 2)

        mod = Moderador()
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
decision, tipo_usua: string
"""


def eliminar_usuario():
    decision = ""

    while decision != "N":
        limpiar_consola()

        tipo_usua = input(
            "Tipo de usuario a eliminar estudiante o moderador (E/M): "
        ).lower()

        while tipo_usua != "e" or tipo_usua != "m":
            tipo_usua = input(
                "Tipo de usuario a eliminar estudiante o moderador (E/M): "
            ).lower()

        if tipo_usua == "e":
            desactivar_estudiante()
        else:
            desactivar_moderador()

        limpiar_consola()
        decision = input("Desactivar otra cuenta. S/N: ").upper()
        decision = validar_continuacion(decision)


"""
email, password: string
"""


def dar_alta_moderador():
    limpiar_consola()
    print("\n........Registro moderador........\n")

    email = ingresar_propiedad("email")
    email = validar_cadena(email, 32)
    password = ingresar_contrasenia()
    password = validar_cadena(password, 32)

    registrar_moderador(email, password)


"""
opc: string
"""


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


"""
decision, opc: string
"""


def manejador_submenu_gestionar_estudiantes():
    global ar_lo_estudiantes

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
            decision = ""

            while decision != "N":
                limpiar_consola()

                desactivar_estudiante()
                limpiar_consola()

                decision = input("Desactivar otra cuenta. S/N: ").upper()
                decision = validar_continuacion(decision)


### Administrador ###


"""
cant, tam_ar: int
"""


def contar_administradores():
    global ar_lo_administradores, ar_fi_administradores

    ar_lo_administradores.seek(0)
    tam_ar = os.path.getsize(ar_fi_administradores)
    cant = 0

    while ar_lo_administradores.tell() < tam_ar:
        cant = cant + 1

    return cant


"""
est: Estudiante
score: Arreglo de 0 a 2 de int
est_id: int
"""


def mostrar_puntuacion(est_id: int, score: list[int]):
    est = Estudiante()
    est = obtener_estudiante_por_id(est_id)

    print(f"El estudiante {est.nombre}")
    print(f"Puntuaje: {score[0]}")
    print(f"Mayor racha: {score[2]}\n")


"""
like: Like
score: Arreglo de 0 a 2 de int
tiene_match: boolean
"""


def actualizar_puntuacion(score: list[int], like: Like):
    tiene_match = tiene_like(like.destinatario, like.remitente)

    # ! Mirar funcionalidad
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


"""
like: Like
score: Arreglo de 0 a 2 de int
est_id, pos, tam_ar: int
"""


def puntuar_candidatos():
    global ar_lo_likesEstudiantes, ar_fi_likesEstudiantes

    ar_lo_likesEstudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_likesEstudiantes)

    est_id = -1
    score = [0, 0, 0]

    limpiar_consola()
    print("........Puntuación de candidatos........\n\n")

    like = Like()

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


"""
mod, mod_repo_ign, mod_repo_acep, mod_mas_repo_procesados: Moderador
cant_repo, cant_repo_ign, cant_repo_acep, cant_repo_procesados, mayor_cant_repo_ign, mayor_cant_repo_acep, mayor_cant_repo_procesados, tam_ar: int
porc_repo_ign, porc_repo_acep: float
"""


def reportes_estadisticos_administrador():
    global ar_lo_reportes, ar_fi_reportes, ar_lo_moderadores, ar_fi_moderadores

    cant_repo = contar_reportes()
    cant_repo_ign = -1
    cant_repo_acep = -1

    mayor_cant_repo_ign = -1
    mod_repo_ign = Moderador()

    mayor_cant_repo_acep = -1
    mod_repo_acep = Moderador()

    mayor_cant_repo_procesados = -1
    mod_mas_repo_procesados = Moderador()

    ar_lo_moderadores.seek(0)
    tam_ar = os.path.getsize(ar_fi_moderadores)

    while ar_lo_moderadores.tell() < tam_ar:
        mod: Moderador = pickle.load(ar_lo_moderadores)

        if mayor_cant_repo_ign < mod.cant_ignorados:
            cant_repo_ign = cant_repo_ign + mod.cant_aceptados
            mayor_cant_repo_ign = mod.cant_ignorados
            mod_repo_ign = mod

        if mayor_cant_repo_acep < mod.cant_aceptados:
            cant_repo_acep = cant_repo_acep + mod.cant_aceptados
            mayor_cant_repo_acep = mod.cant_aceptados
            mod_repo_acep = mod

        cant_repo_procesados = mod.cant_aceptados + mod.cant_ignorados

        if mayor_cant_repo_procesados < cant_repo_procesados:
            mayor_cant_repo_procesados = cant_repo_procesados
            mod_mas_repo_procesados = mod

    porc_repo_ign = cant_repo_ign / cant_repo * 100
    porc_repo_acep = cant_repo_acep / cant_repo * 100

    print(f"Los estudiantes realizaron un total de {cant_repo} reportes.")
    print(f"El porcentaje de reportes ignorados es de : {porc_repo_ign:.2f}%")
    print(f"El porcentaje de reportes aceptados es de : {porc_repo_acep:.2f}%")
    print(
        f"El moderador que mayor cantidad de reportes ha ignorado:\tId: {mod_repo_ign.id}\tEmail: {mod_repo_ign.email}"
    )
    print(
        f"El moderador que mayor cantidad de reportes ha aceptado:\tId: {mod_repo_acep.id}\tEmail: {mod_repo_acep.email}"
    )
    print(
        f"El moderador que mayor cantidad de reportes ha procesado:\tId: {mod_mas_repo_procesados.id}\t Email:{mod_mas_repo_procesados.email}"
    )

    input("\n\nPresione Enter para continuar...")


### Mostrar ###


"""
est_id: int
opc: string
esta_borrado: boolean
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
usua: Arreglo de 0 a 1 de int
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


"""
opc: string
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

    opc = input("\nSeleccione una opción: ")

    while (
        opc != "1"
        and opc != "2"
        and opc != "3"
        and opc != "4"
        and opc != "5"
        and opc != "6"
        and opc != "7"
        and opc != "0"
    ):
        print("La opción introducida no es válida.")
        opc = input("Por favor, introduzca una opción válida: ")

    return opc


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
opc: string
"""


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
usuario: Arreglo de 0 a 1 de int
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
est: Estudiante
est_id: int
opc: string
"""


def manejador_menu_principal_estudiante(est_id: int):
    opc = ""

    est = Estudiante()
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
                ruleta(est_id)
            case "6":
                huecos_edades()
            case "7":
                matcheos_combinados()
            case "0":
                limpiar_consola()

        est = obtener_estudiante_por_id(est_id)


"""
usuario: Arreglo de 0 a 1 de int
opc: string
"""


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


"""
usuario: Arreglo de 0 a 1 de int
opc: string
"""


def manejador_menu_principal_administrador(usuario: list[int]):
    opc = ""

    while opc != "0":
        opc = mostrar_menu_principal_administradores()

        match opc:
            case "1":
                manejador_submenu_gestionar_usuarios()
            case "2":
                manejador_submenu_gestionar_reportes(usuario)
            case "3":
                reportes_estadisticos_administrador()
            case "4":
                puntuar_candidatos()


"""
usuario: Arreglo de 0 a 1 de int
opc: string
"""


def mostrar_est():
    global ar_lo_estudiantes, ar_fi_estudiantes

    ar_lo_estudiantes.seek(0)
    tam_ar = os.path.getsize(ar_fi_estudiantes)

    while ar_lo_estudiantes.tell() < tam_ar:
        est: Estudiante = pickle.load(ar_lo_estudiantes)
        print(est.__dict__)
    test()


def mostrar_mod():
    global ar_lo_moderadores, ar_fi_moderadores

    ar_lo_moderadores.seek(0)
    tam_ar = os.path.getsize(ar_fi_moderadores)

    while ar_lo_moderadores.tell() < tam_ar:
        mod: Moderador = pickle.load(ar_lo_moderadores)
        print(mod.__dict__)
    test()


def verificar_cant_usuarios():
    cant_est = contar_estudiantes()
    cant_mod = contar_moderadores()
    cant_adm = contar_administradores()

    return cant_est >= 4 and cant_mod >= 1 and cant_adm >= 1

def main():
    inicializar_archivos()

    opc = ""
    usuario = [0] * 2

    # mostrar_est()
    # mostrar_mod()
    # mostrar_likes()

    while opc != "0" and usuario[0] != -1 and verificar_cant_usuarios():
        opc = mostrar_menu_principal()

        match opc:
            case "1":
                usuario = log_in()

                if usuario[0] != -1:
                    mostrar_menu_usuario(usuario)
            case "2":
                registrar()

    if not verificar_cant_usuarios():
        print("No hay la cantidad suficientes de usuarios para ejecutar la aplicación.")

    limpiar_consola()
    print("¡Hasta luego!")

    finalizar_archivos()


main()
