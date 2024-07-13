"""
  Integrantes:
    - CAPPA, Giuliano Martin
    - ROBLEDO, Camila Antonella
"""

from datetime import date, datetime
from getpass import getpass
import math
import os
import platform
import random

# Campos de propiedades de estudiante
"""
NACIMIENTO, BIOGRAFIA, HOBBIES: string
"""
NACIMIENTO = "nacimiento"
BIOGRAFIA = "biografia"
HOBBIES = "hobbies"
ESTADOS_ESTUDIANTES = ["INACTIVO", "ACTIVO"]


# Mock de la base de datos de estudiantes
"""
ESTUDIANTE_1_EMAIL, ESTUDIANTE_1_PASSWORD, estudiante_1_nacimiento, estudiante_1_nombre, estudiante_1_biografia, estudiante_1_hobbies: string
"""
estudiantes = [[""]*7 for n in range(8)]
moderadores = [[""]*3 for n in range(4)]

def validar_continuacion(opc):
    while opc != "S" or opc != "N":
        opc = input("Opción incorrecta S o N: ").upper()

    limpiar_consola()

    return opc == "S"

def inicializar_moderadores_mock(mod):
    mod[0][0] = "0"
    mod[0][1] = "moderador1@ayed.com"
    mod[0][2] = "111222"


def cargar_moderador(mod):
    cant_inicializados = 0
    continuar = True

    while(cant_inicializados <= 4 and continuar):
        mod[cant_inicializados][0] = cant_inicializados
        mod[cant_inicializados][1] = input("Ingrese el email: ")
        mod[cant_inicializados][2] = getpass("Ingrese la contraseña: ")

        cant_inicializados = cant_inicializados + 1

        opc = input("Añadir un nuevo moderador (S/N) ").upper()
        opc = validar_continuacion(opc)


def inicializar_estudiantes_mock(est):
    est[0][0] = "0"
    est[0][1] = "estudiante1@ayed.com"
    est[0][2] = "111222"
    est[0][3] = "2001-10-01"
    est[0][4] = "Juan Peréz"
    est[0][5] = "Juan Peréz es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías."
    est[0][6] = "Lectura - Senderismo - Juegos de mesa"

    est[1][0] = "1"
    est[1][1] = "estudiante2@ayed.com"
    est[1][2] = "333444"
    est[1][3] = "1998-04-11"
    est[1][4] = "María García"
    est[1][5] = "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
    est[1][6] = "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"

    est[2][0] = "2"
    est[2][1] = "estudiante3@ayed.com"
    est[2][2] = "555666"
    est[2][3] = "2005-06-30"
    est[2][4] = "Carlos Martínez"
    est[2][5] = "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
    est[2][6] = "Correr - Tocar la guitarra - Cocinar platos internacionales"

    est[3][0] = "3"
    est[3][1] = "estudiante4@ayed.com"
    est[3][2] = "789101"
    est[3][3] = "2001-09-15"
    est[3][4] = "Ana López"
    est[3][5] = "Ana López es una estudiante de ingeniería informática interesada en la inteligencia artificial y la ciberseguridad. Aspira a desarrollar tecnologías innovadoras que mejoren la seguridad digital."
    est[3][6] = "Leer ciencia ficción - Pintar - Practicar yoga"


def cargar_estudiantes(est):
    cant_estudiantes = 0
    continuar = True

    print("A continuación ingrese los datos iniciales de los estudiantes.\n\n")

    while cant_estudiantes < 4 or (continuar and cant_estudiantes <= 7):
        est[cant_estudiantes][0] = str(cant_estudiantes)

        for prop in range(1, 7):
            match prop:
                case 1:
                    est[cant_estudiantes][prop] = input("Ingrese el email: ")
                    limpiar_consola()
                case 2:
                    est[cant_estudiantes][prop] = getpass("Ingrese la contraseña: ")
                    limpiar_consola()
                case 3:
                    est[cant_estudiantes][prop] = input("Ingrese la fecha de nacimiento: ")
                    limpiar_consola()
                case 4:
                    est[cant_estudiantes][prop] = input("Ingrese el nombre: ")
                    limpiar_consola()
                case 5:
                    est[cant_estudiantes][prop] = input("Ingrese su biografía: ")
                    limpiar_consola()
                case 6:
                    est[cant_estudiantes][prop] = ESTADOS_ESTUDIANTES[1]

        opc = input("Añadir un nuevo estudiante (S/N) ").upper()
        opc = validar_continuacion(opc)

        cant_estudiantes = cant_estudiantes + 1

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
nacimiento, biografia, formato_espaniol_nacimiento, hobbies, nombre: string
nacimiento_estudiante, fecha_actual: datetime
edad, dia, mes, anios: int
"""


def vista_perfil_estudiante(nombre, nacimiento, biografia, hobbies):
    fecha_actual = datetime.now()
    nacimiento_estudiante = datetime.fromisoformat(nacimiento)

    anios = nacimiento_estudiante.year
    mes = nacimiento_estudiante.month
    dia = nacimiento_estudiante.day
    edad = fecha_actual.year - anios
    formato_espaniol_nacimiento = str(dia) + "/" + str(mes) + "/" + str(anios)

    if fecha_actual.month <= mes and fecha_actual.day < dia:
        edad = edad - 1

    print("Nombre:", nombre)
    print("Fecha de nacimiento:", formato_espaniol_nacimiento)
    print("Edad:", edad)
    print("Biografía:\n\t" + biografia)
    print("Hobbies:\n\t", hobbies)


"""
me_gusta, estudiante_id: string
"""


def vista_perfil_estudiantes(estudiante_id):
    me_gusta = ""

    # if estudiante_id != ESTUDIANTE_1_EMAIL:
    #     vista_perfil_estudiante(
    #         estudiante_1_nombre,
    #         estudiante_1_nacimiento,
    #         estudiante_1_biografia,
    #         estudiante_1_hobbies,
    #     )
    #     print("\n")

    # if estudiante_id != ESTUDIANTE_2_EMAIL:
    #     vista_perfil_estudiante(
    #         estudiante_2_nombre,
    #         estudiante_2_nacimiento,
    #         estudiante_2_biografia,
    #         estudiante_2_hobbies,
    #     )
    #     print("\n")

    # if estudiante_id != ESTUDIANTE_3_EMAIL:
    #     vista_perfil_estudiante(
    #         estudiante_3_nombre,
    #         estudiante_3_nacimiento,
    #         estudiante_3_biografia,
    #         estudiante_3_hobbies,
    #     )
    #     print("\n")

    # if estudiante_id != ESTUDIANTE_4_EMAIL:
    #     vista_perfil_estudiante(
    #         estudiante_4_nombre,
    #         estudiante_4_nacimiento,
    #         estudiante_4_biografia,
    #         estudiante_4_hobbies,
    #     )
    #     print("\n")

    decision = input(
        "Le gustaría en un futuro hacer matcheo con algún estudiante. (S/N) "
    )

    while decision != "S" and decision != "N":
        decision = input("Desea hacer matcheo con algún estudiante S o N: ")

    if decision == "S":
        nombre_estudiante = input(
            "Ingrese el nombre del estudiante con el que quiere hacer matcheo: "
        )

        # while (
        #     nombre_estudiante != estudiante_1_nombre
        #     and nombre_estudiante != estudiante_2_nombre
        #     and nombre_estudiante != estudiante_3_nombre
        #     and nombre_estudiante != estudiante_4_nombre
        # ):
        #     print("No existe el estudiante", nombre_estudiante)
        #     nombre_estudiante = input("Ingrese un nombre de estudiante: ")

        me_gusta = nombre_estudiante


"""
opcion: string
"""


def ver_menu_principal_estudiante():
    limpiar_consola()

    print("\n........Home........")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    while (
        opcion != "1"
        and opcion != "2"
        and opcion != "3"
        and opcion != "4"
        and opcion != "5"
        and opcion != "0"
    ):
        print("La opción introducida no es válida.")
        opcion = input("Por favor, introduzca una opción válida: ")

    return opcion


"""
valid_email, valid_password: boolean
email, password, acceso_valido: string
intentos: int
"""
def log_in():
    acceso_valido = ""
    intentos = 3

    print("\n........Bienvenido........\n")

    while intentos > 0 and acceso_valido == "":
        email = input("Ingrese su email: ")
        password = getpass("Ingrese su contraseña: ")

        login_valido = False

        for ind in range(0, 8):
            if not login_valido:
                login_valido = estudiantes[ind][1] == email and estudiantes[ind][2] == password
                acceso_valido = str(ind)

        if not login_valido:
            for ind in range(0, 4):
                if not login_valido:
                    login_valido = moderadores[ind][1] == email and moderadores[ind][2] == password
                    acceso_valido = str(ind)

        if login_valido:
            acceso_valido = email
        else:
            intentos = intentos - 1
            print("Datos incorrectos. Intentos restantes:", intentos, "\n")

    if intentos == 0:
        print("Ha superado el número máximo de intentos. El programa se cerrará.")

    return acceso_valido


"""
probabilidad: int
rand: float
"""
def calcular__valor_persona(probabilidad):
    rand = random.random()
    return math.floor(rand * probabilidad * 100)


"""
person_name: string
probabilidad_match_1, probabilidad_match_2, probabilidad_match_3: int
"""
def ruleta(student_id):
    limpiar_consola()

    nombre_estudiante_1 = ""
    probabilidad_match_1 = 0
    nombre_estudiante_2 = ""
    probabilidad_match_2 = 0
    nombre_estudiante_3 = ""
    probabilidad_match_3 = 0
    nombre_match = ""

    print("........RULETA........")
    print(
        "A continuación, se le pedirá ingresar la probabilidad de matcheo con tres estudiantes."
    )
    print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

    while probabilidad_match_1 + probabilidad_match_2 + probabilidad_match_3 != 100:
        # if student_id != ESTUDIANTE_1_EMAIL:
        #     print(estudiante_1_nombre)

        # if student_id != ESTUDIANTE_2_EMAIL:
        #     print(estudiante_2_nombre)

        # if student_id != ESTUDIANTE_3_EMAIL:
        #     print(estudiante_3_nombre)

        # if student_id != ESTUDIANTE_4_EMAIL:
        #     print(estudiante_4_nombre)

        # if student_id == ESTUDIANTE_1_EMAIL:
        #     nombre_estudiante_1 = estudiante_2_nombre
        #     nombre_estudiante_2 = estudiante_3_nombre
        #     nombre_estudiante_3 = estudiante_4_nombre

        # elif student_id == ESTUDIANTE_2_EMAIL:
        #     nombre_estudiante_1 = estudiante_1_nombre
        #     nombre_estudiante_2 = estudiante_3_nombre
        #     nombre_estudiante_3 = estudiante_4_nombre

        # elif student_id == ESTUDIANTE_3_EMAIL:
        #     nombre_estudiante_1 = estudiante_1_nombre
        #     nombre_estudiante_2 = estudiante_2_nombre
        #     nombre_estudiante_3 = estudiante_4_nombre

        # elif student_id == ESTUDIANTE_4_EMAIL:
        #     nombre_estudiante_1 = estudiante_1_nombre
        #     nombre_estudiante_2 = estudiante_2_nombre
        #     nombre_estudiante_3 = estudiante_3_nombre

        probabilidades_ingresadas = 0

        print("\n")
        while probabilidades_ingresadas < 3:
            valor = input(
                "Ingresar la probabilidad del estudiante "
                + str(probabilidades_ingresadas + 1)
                + ": "
            )

            while not valor.isnumeric():
                valor = input("Por favor ingrese un valor numérico entero: ")

            probabilidades_ingresadas = probabilidades_ingresadas + 1

            if probabilidades_ingresadas == 1:
                probabilidad_match_1 = int(valor)

            elif probabilidades_ingresadas == 2:
                probabilidad_match_2 = int(valor)

            else:
                probabilidad_match_3 = int(valor)

        probabilidad_total = (
            probabilidad_match_1 + probabilidad_match_2 + probabilidad_match_3
        )

        if probabilidad_total != 100:
            limpiar_consola()
            print(
                "\n\nLa probabilidad total debe ser igual a 100 y el introducido es",
                probabilidad_total,
                ".",
            )
            print("Vuelva a introducir los valores.\n\n")

    Valor_persona_1 = calcular__valor_persona(probabilidad_match_1)
    valor_persona_2 = calcular__valor_persona(probabilidad_match_2)
    valor_persona_3 = calcular__valor_persona(probabilidad_match_3)

    # Existe una pequeña probabilidad de que den iguales
    if valor_persona_2 <= Valor_persona_1 and valor_persona_3 <= Valor_persona_1:
        nombre_match = nombre_estudiante_1
    elif valor_persona_2 >= valor_persona_3:
        nombre_match = nombre_estudiante_2
    else:
        nombre_match = nombre_estudiante_3

    print("\nTu match es la persona", nombre_match)
    input("\nPresiona Enter para volver al inicio...")


"""
opcion, estudiante_id: string
"""
def submenu_gestionar_candidatos(estudiante_id):
    opcion = ""

    while opcion != "c":
        limpiar_consola()
        print("........Gestionar Candidatos........\n")
        print("a. Ver candidatos")
        print("b. Reportar un candidato")
        print("c. Volver")

        opcion = input("\nSeleccione una opción: ")

        while opcion != "a" and opcion != "b" and opcion != "c":
            print("\nNo es una opción válida.")
            opcion = input("\nSeleccione una opción: ")

        if opcion == "a":
            vista_perfil_estudiantes(estudiante_id)

        if opcion == "b":
            en_construccion()


"""
opcion: string
"""
def submenu_matcheos():
    opcion = ""

    while opcion != "c":
        limpiar_consola()
        print("........Matcheos........\n")
        print("a. Ver matcheos")
        print("b. Eliminar un matcheo")
        print("c. Volver")

        opcion = input("\nSeleccione una opción: ")

        while opcion != "a" and opcion != "b" and opcion != "c":
            print("\nNo es una opción válida.")
            opcion = input("\nSeleccione una opción: ")

        if opcion == "a" or opcion == "b":
            en_construccion()


"""
max_dia_febrero, dia, mes, anio: int
es_valido: bool
"""
def validar_fecha(dia, mes, anio):
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

        if (
            anio% 4 == 0
            and anio % 100 != 0
            or anio%400 == 0
        ):
            max_dia_febrero = max_dia_febrero + 1

        if dia < 1 or dia > max_dia_febrero:
            es_valido = False
    elif anio > 2006 or anio < 1959:
        es_valido = False

    return es_valido


"""
estudiante_id, propiedad, valor, estudiante_1_nacimiento, estudiante_1_biografia, estudiante_1_hobbies,
estudiante_2_nacimiento, estudiante_2_biografia, estudiante_2_hobbies,estudiante_3_nacimiento, estudiante_3_biografia, estudiante_3_hobbies,estudiante_4_nacimiento, estudiante_4_biografia, estudiante_4_hobbies, ESTUDIANTE_1_EMAIL, NACIMIENTO, BIOGRAFIA, HOBBIES, ESTUDIANTE_2_EMAIL, ESTUDIANTE_3_EMAIL: string
"""
def actualizar_estudiante(estudiante_id, propiedad, valor):
    # Si no aparece "global", los datos no se modifican
    global estudiante_1_nacimiento, estudiante_1_biografia, estudiante_1_hobbies
    global estudiante_2_nacimiento, estudiante_2_biografia, estudiante_2_hobbies
    global estudiante_3_nacimiento, estudiante_3_biografia, estudiante_3_hobbies
    global estudiante_4_nacimiento, estudiante_4_biografia, estudiante_4_hobbies

    # if estudiante_id == ESTUDIANTE_1_EMAIL:
    #     if propiedad == NACIMIENTO:
    #         estudiante_1_nacimiento = valor
    #     elif propiedad == BIOGRAFIA:
    #         estudiante_1_biografia = valor
    #     elif propiedad == HOBBIES:
    #         estudiante_1_hobbies = valor

    # if estudiante_id == ESTUDIANTE_2_EMAIL:
    #     if propiedad == NACIMIENTO:
    #         estudiante_2_nacimiento = valor
    #     elif propiedad == BIOGRAFIA:
    #         estudiante_2_biografia = valor
    #     elif propiedad == HOBBIES:
    #         estudiante_2_hobbies = valor

    # if estudiante_id == ESTUDIANTE_3_EMAIL:
    #     if propiedad == NACIMIENTO:
    #         estudiante_3_nacimiento = valor
    #     elif propiedad == BIOGRAFIA:
    #         estudiante_3_biografia = valor
    #     elif propiedad == HOBBIES:
    #         estudiante_3_hobbies = valor

    # if estudiante_id == ESTUDIANTE_4_EMAIL:
    #     if propiedad == NACIMIENTO:
    #         estudiante_4_nacimiento = valor
    #     elif propiedad == BIOGRAFIA:
    #         estudiante_4_biografia = valor
    #     elif propiedad == HOBBIES:
    #         estudiante_4_hobbies = valor


"""
estudiante_id, opcion: string
"""
def submenu_gestionar_perfil(estudiante_id):
    opcion = ""

    while opcion != "c":
        limpiar_consola()
        print("........Gestionar Perfil........\n")
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil")
        print("c. Volver")

        opcion = input("\nSeleccione una opción: ")

        while opcion != "a" and opcion != "b" and opcion != "c":
            print("\nNo es una opción válida.")
            opcion = input("Ingrese una opción válida: ")

        if opcion == "a":
            editar_datos_estudiante(estudiante_id)
        elif opcion == "b":
            en_construccion()


"""
email, ESTUDIANTE_1_EMAIL, ESTUDIANTE_2_EMAIL, ESTUDIANTE_3_EMAIL, ESTUDIANTE_4_EMAIL, estudiante_1_nombre,
estudiante_1_nacimiento, estudiante_1_biografia, estudiante_1_hobbies, estudiante_2_nombre, estudiante_2_nacimiento,
estudiante_2_biografia, estudiante_2_hobbies, estudiante_3_nombre, estudiante_3_nacimiento, estudiante_3_biografia, 
estudiante_3_hobbies, estudiante_4_nombre, estudiante_4_nacimiento, estudiante_4_biografia, estudiante_4_hobbies: string
"""
def print_student_data(email):
    print("Modificar")
    # if email == ESTUDIANTE_1_EMAIL:
    #     print("Nombre:", estudiante_1_nombre)
    #     print("Fecha de nacimiento:", estudiante_1_nacimiento)
    #     print("Biografía:", estudiante_1_biografia)
    #     print("Hobbies:", estudiante_1_hobbies)
    # elif email == ESTUDIANTE_2_EMAIL:
    #     print("Nombre:", estudiante_2_nombre)
    #     print("Fecha de nacimiento:", estudiante_2_nacimiento)
    #     print("Biografía:", estudiante_2_biografia)
    #     print("Hobbies:", estudiante_2_hobbies)
    # elif email == ESTUDIANTE_3_EMAIL:
    #     print("Nombre:", estudiante_3_nombre)
    #     print("Fecha de nacimiento:", estudiante_3_nacimiento)
    #     print("Biografía:", estudiante_3_biografia)
    #     print("Hobbies:", estudiante_3_hobbies)
    # elif email == ESTUDIANTE_4_EMAIL:
    #     print("Nombre:", estudiante_4_nombre)
    #     print("Fecha de nacimiento:", estudiante_4_nacimiento)
    #     print("Biografía:", estudiante_4_biografia)
    #     print("Hobbies:", estudiante_4_hobbies)


"""
estudiante_id, opcion, dia, mes, anio, nacimiento, bibligrafia, hobbies, NACIMIENTO, BIBLIOGRAFIA, HOBBIES:str   
fecha: date
"""
def editar_datos_estudiante(estudiante_id):
    opcion = ""

    while opcion != "n":
        print("\n")
        print_student_data(estudiante_id)

        print("\n\n........Actualizar perfil........\n")
        print("a. Editar fecha de nacimiento")
        print("b. Editar biografía")
        print("c. Editar hobbies")
        print("n. Finalizar\n")

        opcion = input("Seleccione una opción: ")

        while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "n":
            print("\nNo es una opción válida.")
            opcion = input("Ingrese una opción válida: ")

        if opcion == "a":
            dia = input("Ingresa el día de nacimiento: ")
            mes = input("Ingresa el mes de nacimiento: ")
            anio = input("Ingresa el año de nacimento: ")

            while not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
                print("Los datos ingresados no son válidos")
                dia = input("Ingresa el día de nacimiento: ")
                mes = input("Ingresa el mes de nacimiento: ")
                anio = input("Ingresa el año de nacimento: ")

            while not validar_fecha(int(dia), int(mes), int(anio)):
                print("Los datos ingresados no son válidos")
                dia = input("Ingresa el día de nacimiento: ")
                mes = input("Ingresa el mes de nacimiento: ")
                anio = input("Ingresa el año de nacimento: ")

            fecha = date(int(anio), int(mes), int(dia))
            nacimiento = fecha.isoformat()

            actualizar_estudiante(estudiante_id, NACIMIENTO, nacimiento)

        elif opcion == "b":
            biografia = input("Nueva biografía:\n")
            actualizar_estudiante(estudiante_id, BIOGRAFIA, biografia)

        elif opcion == "c":
            hobbies = input("Nuevos Hobbies:\n")
            actualizar_estudiante(estudiante_id, HOBBIES, hobbies)


"""
accedio, opcion_menu_principal: string
"""
def main():
    # cargar_estudiantes(estudiantes)
    # cargar_moderador(moderadores)
    inicializar_estudiantes_mock(estudiantes)
    inicializar_moderadores_mock(moderadores)

    usuario_id = log_in()

    if usuario_id != "":
        opcion_menu_principal = "1"

        while opcion_menu_principal != "0":
            opcion_menu_principal = ver_menu_principal_estudiante()

            match opcion_menu_principal:
                case "1":
                    submenu_gestionar_perfil(usuario_id)

                case "2":
                    submenu_gestionar_candidatos(usuario_id)

                case "3":
                    submenu_matcheos()

                case "4":
                    en_construccion()

                case "5":
                    ruleta(usuario_id)

                case "0":
                    limpiar_consola()
                    print("¡Hasta luego!")


main()
