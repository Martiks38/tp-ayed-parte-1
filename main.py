"""
  Integrantes:
    - CAPPA, Giuliano Martin
    - ROBLEDO, Camila Antonella
"""

from datetime import date, datetime
from getpass import getpass
import os
import platform
import random

"""
NACIMIENTO, BIOGRAFIA, HOBBIES: string
PROPS_ESTUDIANTE: Arreglo de 0 a 6 de string
ESTADO_ESTUDIANTE: Arreglo de 0 a 1 de string
ESTADO_REPORTE: Arreglo de 0 a 2 de string
GENERO: Arreglo de 0 a 1 de string
ROLES: Arreglo de 0 a 1 de string
"""
NACIMIENTO = "nacimiento"
BIOGRAFIA = "biografia"
HOBBIES = "hobbies"
CIUDAD = "ciudad"
PAIS = "pais"
GENERO = ["F", "M"]
PROPS_ESTUDIANTE = ["Nacimiento", "Nombre", "Biografía", "Hobbies", "Género", "Ciudad", "País"]
ESTADO_ESTUDIANTE = ["INACTIVO", "ACTIVO"]
ESTADO_REPORTE = ["0", "1", "2"]
ROLES = ["ESTUDIANTE", "MODERADOR"]

"""
cant_total_reportes: int
estudiantes: Arreglo multi de 11x8 de string
moderadores: Arreglo multi de 3x4 de string
me_gusta: Arreglo multi de 8x8 de string
reportes: Arreglo multi de 5x40 de bool
"""
estudiantes = [[""]*11 for n in range(8)]
moderadores = [[""]*3 for n in range(4)]
me_gusta = [[False]*8 for n in range(8)]
# Estimamos un máximo de 5 reportes por estudiante,
# hay 8 estudiantes, siendo un total de 40 reportes
cant_total_reportes = 40
reportes = [[""]*5 for n in range(cant_total_reportes)]

"""
opc: string
"""
def validar_continuacion(opc):
    while opc != "S" and opc != "N":
        opc = input("Opción incorrecta S o N: ").upper()

    limpiar_consola()

    return opc

"""
cant, est_id, ind: int
"""
def contar_estudiantes_activos_no_matcheados(est_id):
    cant = 0
    ind = 0

    while ind < 8 and estudiantes[ind][0] != str(est_id):
        if estudiantes[ind][10] == ESTADO_ESTUDIANTE[1] and me_gusta[est_id - 1][ind]:
            cant = cant + 1

        ind = ind + 1

    return cant

"""
cant, ind: int
"""
def contar_estudiantes_activos():
    cant = 0
    ind = 0

    while ind < 8 and estudiantes[ind][0] != "":
        if estudiantes[ind][10] == ESTADO_ESTUDIANTE[1]:
            cant = cant + 1

        ind = ind + 1

    return cant

"""
cant_estudiantes, ind: int
est_id: string
"""
def validar_id_estudiante(est_id):
    cant_estudiantes = contar_estudiantes()
    ind = 0

    while ind < cant_estudiantes and estudiantes[ind][0] != est_id:
        ind = ind + 1

    return ind != cant_estudiantes

"""
cant, ind: int
"""
def contar_reportes():
    cant = 0
    ind = 0

    while ind < cant_total_reportes and reportes[ind][0] != "":
        cant = cant + 1
        ind = ind + 1

    return cant

"""
edades: Arreglo de 0 a 5 de int
aux, i, j: int
"""
def ordenar_edades_creciente(edades):
    for i in range(6):
        for j in range(5):
            if edades[j] > edades[j+1]:
                aux = edades[j+1]
                edades[j+1] = edades[j]
                edades[j] = aux

"""
edad, edad_1, edad_2: int
"""
def mostrar_valores_faltantes(edad_1, edad_2):
    print("\nSe detectó un hueco.")
    print(f"Los valores faltantes entre {edad_1} y {edad_2} años son:\n")

    for edad in range(edad_1 + 1, edad_2):
        print("-", edad)

    print("\n")

"""
edades: Arreglo de 0 a 5 de int
cant_huecos, ind: int
"""
def detectar_huecos_entre_edades(edades):
    cant_huecos = 0

    for ind in range(5):
        edad_1 = edades[ind]
        edad_2 = edades[ind + 1]

        if edad_2 - edad_1 != 1:
            cant_huecos = cant_huecos + 1
            mostrar_valores_faltantes(edad_1, edad_2)

    if cant_huecos != 0:
        print(f"Se encontraron {cant_huecos} huecos entre las edades de los 6 estudiantes.")
    else:
        print("No se encontrarón huecos entra las edades los 6 estudiantes.")

"""
edades: Arreglo de 0 a 5 de int
ind: int
"""
def mostrar_edades(edades):
    for ind in range(6):
        print(f"- {edades[ind]} años")

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
cant_est, cant_matcheos: int
"""
def matcheos_combinados():
    limpiar_consola()
    cant_est = contar_estudiantes_activos()
    cant_matcheos = int(cant_est*(cant_est - 1)/2)

    print(f"La cantidad de matcheos posibles entre {cant_est} estudiantes es {cant_matcheos}.")

    input("\nPresiona Enter para volver al inicio...")

"""
cant, ind: int
"""
def contar_estudiantes():
    cant = 0
    ind = 0

    while ind < 8 and estudiantes[ind][0] != "":
        cant = cant + 1
        ind = ind + 1

    return cant

"""
cant, ind: int
"""
def contar_moderadores():
    cant = 0

    for ind in range(4):
        if moderadores[ind][0] != "":
            cant = cant + 1

    return cant

"""
fecha: Arreglo de 0 a 2 de string
"""
def ingresar_fecha():
    fecha = [""]*3

    fecha[0] = input("Ingresa el día de nacimiento: ")
    fecha[1] = input("Ingresa el mes de nacimiento: ")
    fecha[2] = input("Ingresa el año de nacimento: ")

    return fecha

"""
fecha: Arreglo de 0 a 2 de string
"""
def validar_fecha(fecha):
    while not (fecha[0].isdigit() and fecha[1].isdigit() and fecha[2].isdigit()):
        print("Los datos ingresados no son válidos")
        print("\n")
        fecha = ingresar_fecha()

    while not validar_valores_fecha(int(fecha[0]), int(fecha[1]), int(fecha[2])):
        print("Los datos ingresados no son válidos")
        print("\n")
        fecha = ingresar_fecha()

"""
fecha: Arreglo de 0 a 2 de string
f: date
"""
def solicitar_fecha_nacimiento():
    fecha = ingresar_fecha()
    validar_fecha(fecha)

    f = date(int(fecha[2]), int(fecha[1]), int(fecha[0]))

    return f.isoformat()

"""
prop, valor: string
"""
def ingresar_propiedad(prop):
    if prop == PROPS_ESTUDIANTE[4]:
        valor = input(f"Ingrese {GENERO[1]} o {GENERO[0]}: ")

        while valor != GENERO[0] and valor != GENERO[1]:
            valor = input(f"Debe ingresar {prop}:\n\t")
    else:
        valor = input(f"Ingrese {prop}:\n\t")
        while valor == "":
            valor = input(f"Debe ingresar {prop}:\n\t")


    return valor

"""
password: string
"""
def ingresar_contrasenia():
    password = getpass("Ingrese su contraseña: ")

    while password == "":
        password = getpass("Debe ingresar una contraseña: ")

    return password

"""
email: string
ind: int
valido: bool
"""
def email_existente(email):
    valido = True
    ind = 0

    while ind < 8 and valido:
        if estudiantes[ind][1] == email:
            valido = False

        ind = ind + 1

    if valido:
        ind = 0

        while ind < 4 and valido:
            if moderadores[ind][1] == email:
                valido = False

            ind = ind + 1

    return valido

"""
email, password: string
cant: int
registrado: bool
"""
def registrar_estudiante(email, password, cant):
    registrado = False

    if cant == 8 or not email_existente(email):
        print("Se produjo un error al registrarse.")
        input("Presione Enter para continuar... ")
    else:
        print("F\necha de nacimiento")
        fecha = solicitar_fecha_nacimiento()

        estudiantes[cant][0] = cant + 1
        estudiantes[cant][1] = email
        estudiantes[cant][2] = password
        estudiantes[cant][3] = fecha
        estudiantes[cant][10] = ESTADO_ESTUDIANTE[1]

        for ind in range(4, 10):
            estudiantes[cant][ind] = ingresar_propiedad(PROPS_ESTUDIANTE[ind - 3])

        registrado = True
        print("\nRegistro exitoso!!!")
        input("Presione Enter para continuar...")

    return registrado

"""
email, password: string
cant: int
registrado: bool
"""
def registrar_moderador(email, password, cant):
    registrado = False

    if cant == "4" or not email_existente(email):
        print("Se produjo un error al registrarse.")
        input("Presione Enter para continuar... ")
    else:
        moderadores[cant][0] = cant + 1
        moderadores[cant][1] = email
        moderadores[cant][2] = password
        registrado = True
        print("\nRegistro exitoso!!!")
        input("Presione Enter para continuar...")

    return registrado

"""
bio, email, fecha, password, rol: string
cant: int
continuar, registrado: bool
"""
def registrar():
    registrado = False
    continuar = True

    limpiar_consola()
    while not registrado and continuar:
        print("\n........Registro........\n")

        email = ingresar_propiedad("email")
        password = ingresar_contrasenia()
        rol = input("Ingrese el rol estudiante(E) o moderador(M). (E/M): ").upper()

        while rol != "E" and rol != "M":
            print("\nNo es un rol válido.")
            rol = input("ingrese E (Estudiante) o M (Moderador): ")

        if rol == "E":
            cant = contar_estudiantes()
            registrado = registrar_estudiante(email, password, cant)

        elif rol == "M":
            cant = contar_moderadores()
            registrado = registrar_moderador(email, password, cant)

        if not registrado:
            decision = input("\nIntentar registrarse nuevamente. S/N ").upper()
            decision = validar_continuacion(decision)

            continuar = decision == "S"

    limpiar_consola()

def inicializar_reportes_mock():
    reportes[0][0] = "0"
    reportes[0][1] = "1"
    reportes[0][2] = "2"
    reportes[0][3] = "Motivo 1"
    reportes[0][4] = ESTADO_REPORTE[0]

    reportes[1][0] = "0"
    reportes[1][1] = "2"
    reportes[1][2] = "3"
    reportes[1][3] = "Motivo 2"
    reportes[1][4] = ESTADO_REPORTE[0]

"""
mod: Arreglo multi de 3x4 de string
"""
def inicializar_moderadores_mock(mod):
    mod[0][0] = "1"
    mod[0][1] = "moderador1@ayed.com"
    mod[0][2] = "111222"

"""
mod: Arreglo multi de 3x4 de string
opc: string
"""
def cargar_moderador(mod):
    cant_inicializados = contar_moderadores()
    continuar = True

    while(cant_inicializados <= 4 and continuar):
        mod[cant_inicializados][0] = str(cant_inicializados + 1) # id
        mod[cant_inicializados][1] = input("Ingrese el email: ")
        mod[cant_inicializados][2] = getpass("Ingrese la contraseña: ")

        cant_inicializados = cant_inicializados + 1

        opc = input("Añadir un nuevo moderador (S/N) ").upper()
        opc = validar_continuacion(opc)

        continuar = opc == "S"

"""
est: Arreglo multi de 8x8 de string
"""
def inicializar_estudiantes_mock(est):
    est[0][0] = "1"
    est[0][1] = "estudiante1@ayed.com"
    est[0][2] = "111222"
    est[0][3] = "2001-10-01"
    est[0][4] = "Juan Peréz"
    est[0][5] = "Juan Peréz es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías."
    est[0][6] = "Lectura - Senderismo - Juegos de mesa"
    est[0][7] = GENERO[1]
    est[0][8] = "Rosario"
    est[0][9] = "Argentina"
    est[0][10] = ESTADO_ESTUDIANTE[1]

    est[1][0] = "2"
    est[1][1] = "estudiante2@ayed.com"
    est[1][2] = "333444"
    est[1][3] = "1998-04-11"
    est[1][4] = "María García"
    est[1][5] = "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
    est[1][6] = "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"
    est[1][7] = "España"
    est[1][8] = GENERO[0]
    est[1][9] = "Madrid"
    est[1][10] = ESTADO_ESTUDIANTE[1]

    est[2][0] = "3"
    est[2][1] = "estudiante3@ayed.com"
    est[2][2] = "555666"
    est[2][3] = "2005-06-30"
    est[2][4] = "Carlos Martínez"
    est[2][5] = "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
    est[2][6] = "Correr - Tocar la guitarra - Cocinar platos internacionales"
    est[2][7] = "Bolivia"
    est[2][8] = GENERO[1]
    est[2][9] = "La Paz"
    est[2][10] = ESTADO_ESTUDIANTE[1]

    est[3][0] = "4"
    est[3][1] = "estudiante4@ayed.com"
    est[3][2] = "789101"
    est[3][3] = "2001-09-15"
    est[3][4] = "Ana López"
    est[3][5] = "Ana López es una estudiante de ingeniería informática interesada en la inteligencia artificial y la ciberseguridad. Aspira a desarrollar tecnologías innovadoras que mejoren la seguridad digital."
    est[3][6] = "Leer ciencia ficción - Pintar - Practicar yoga"
    est[3][7] = "Paraguay"
    est[3][8] = GENERO[0]
    est[3][9] = "Asuncion"
    est[3][10] = ESTADO_ESTUDIANTE[1]

"""
est: Arreglo multi de 8x8 de string
cant_estudiantes, prop: int
continuar: bool
opc: string
"""
def cargar_estudiantes(est):
    cant_estudiantes = contar_estudiantes()
    continuar = True

    print("A continuación ingrese los datos iniciales de los estudiantes.\n\n")

    while cant_estudiantes < 4 or (continuar and cant_estudiantes <= 7):
        est[cant_estudiantes][0] = str(cant_estudiantes + 1)

        for prop in range(1, 8):
            match prop:
                case 1:
                    est[cant_estudiantes][prop] = input("Ingrese el email: ")
                    limpiar_consola()
                case 2:
                    est[cant_estudiantes][prop] = getpass("Ingrese la contraseña: ")
                    limpiar_consola()
                case 3:
                    print("Fecha de nacimiento")
                    est[cant_estudiantes][prop] = solicitar_fecha_nacimiento()
                    limpiar_consola()
                case 4:
                    est[cant_estudiantes][prop] = input("Ingrese el nombre: ")
                    limpiar_consola()
                case 5:
                    est[cant_estudiantes][prop] = input("Ingrese su biografía:\n")
                    limpiar_consola()
                case 6:
                    est[cant_estudiantes][prop] = input("Ingrese sus hobbies:\n")
                case 7:
                    est[cant_estudiantes][prop] = True
                # case 8:
                #     est[cant_estudiantes][prop] = True
                # case 9:
                #     est[cant_estudiantes][prop] = True
                # case 10:
                #     est[cant_estudiantes][prop] = True

        opc = input("Añadir un nuevo estudiante (S/N) ").upper()
        opc = validar_continuacion(opc)

        continuar = opc == "S"
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

"""
"""
def en_construccion():
    limpiar_consola()
    print("En construcción.")
    input("Presiona Enter para continuar... ")

"""
opcion: string
"""
def mostrar_menu_principal():
    limpiar_consola()

    print("\n........Bienvenido........\n")
    print("1. Conectarse")
    print("2. Registrarse")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    while (
        opcion != "1"
        and opcion != "2"
        and opcion != "0"
    ):
        print("La opción introducida no es válida.")
        opcion = input("Por favor, introduzca una opción válida: ")

    return opcion

"""
fecha: Arreglo de 0 a 2 de string
fecha_nros: Arreglo de 0 a 2 de int
f: datetime
"""
def obtener_valores_fecha(fecha):
    fecha_nros = [0]*3

    f = datetime.fromisoformat(fecha)

    fecha_nros[0] = f.day
    fecha_nros[1] = f.month
    fecha_nros[2] = f.year

    return fecha_nros

"""
fecha: Arreglo de 0 a 2 de string
fecha_nros: Arreglo de 0 a 2 de int
anio, dia, formato_espaniol_nacimiento, mes: string
"""
def formatear_fecha_espaniol(fecha):
    fecha_nros = obtener_valores_fecha(fecha)

    dia = fecha_nros[0]
    mes = fecha_nros[1]
    anio = fecha_nros[2]

    formato_espaniol_nacimiento = str(dia) + "/" + str(mes) + "/" + str(anio)

    return formato_espaniol_nacimiento

"""
fecha: Arreglo de 0 a 2 de string
fecha_nros: Arreglo de 0 a 2 de int
fecha_actual: datetime
anio, dia, edad, mes: int
"""
def calcular_edad(fecha):
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
estudiante: Arreglo de 0 a 7 de string
est_id, formato_espaniol_nacimiento: string
edad, ind: int
"""
def vista_perfil_estudiante(est_id):
    ind = 0

    limpiar_consola()
    while ind < 8 and estudiantes[ind][0] != "":
        if estudiantes[ind] != str(est_id):
            estudiante = estudiantes[ind]

            edad = calcular_edad(estudiante[3])
            formato_espaniol_nacimiento = formatear_fecha_espaniol(estudiante[3])

            print("Nombre:", estudiante[4])
            print("Fecha de nacimiento:", formato_espaniol_nacimiento)
            print("Edad:", edad)
            print("Biografía:\n\t" + estudiante[5])
            print("Hobbies:\n\t", estudiante[6])

            if me_gusta[est_id - 1][ind]:
                print("Estado del Match: Tienes match ✔️")
            else:
                print("Estado del Match: No tienes match ❌")

            print("\n")

        ind = ind + 1

"""
nombre: string
est_id, ind: int
"""
def obtener_nombre_estudiante_por_id(est_id):
    nombre = ""
    ind = 0

    while ind < 8 and nombre == "":
        if estudiantes[ind][0] == est_id:
            nombre = estudiantes[ind][4]

        ind = ind + 1

    return nombre

"""
est_id, ind: int
nombre: string
"""
def obtener_id_estudiante_por_nombre(nombre):
    est_id = -1
    ind = 0

    while ind < 8 and est_id == -1:
        if estudiantes[ind][4] == nombre:
            est_id = ind + 1

        ind = ind + 1

    return est_id

"""
estudiante: Arreglo de 0 a 7 de string
estado: string
est_id, ind: int
"""
def obtener_estado_estudiante_por_id(est_id):
    encontrado = False
    ind = 0

    while ind < 8 and not encontrado:
        if estudiantes[ind][0] == est_id:
            encontrado = True
        else:
            ind = ind + 1

    return estudiantes[ind][10]

"""
nombre: string
est_id: int
"""
def validar_nombre(nombre):
    est_id = obtener_id_estudiante_por_nombre(nombre)

    while est_id == -1:
        print("No existe el estudiante", nombre)
        nombre = input("Ingrese un nombre de estudiante: ")

        est_id = obtener_id_estudiante_por_nombre(nombre)

    return nombre

"""
est_id, match_id: int
decision, nombre_estudiante: string
"""
def marcar_match(est_id, realizo_matcheo):
    decision = "S"

    if not realizo_matcheo:
        decision = input("Le gustaría en un futuro hacer matcheo con algún estudiante. (S/N) ").upper()

        while decision != "S" and decision != "N":
            decision = input("Desea hacer matcheo con algún estudiante S o N: ").upper()

    if realizo_matcheo or decision == "S":
        nombre_estudiante = input(
            "\nIngrese el nombre del estudiante con el que quiere hacer matcheo: "
        )

        nombre_estudiante = validar_nombre(nombre_estudiante)
        match_id = obtener_id_estudiante_por_nombre(nombre_estudiante)

        if me_gusta[est_id - 1][match_id - 1]:
            print("\nYa tiene match con", nombre_estudiante)
        else:
            me_gusta[est_id - 1][match_id - 1] = True

            limpiar_consola()
            vista_perfil_estudiante(est_id)
            print("Se envío el match a", nombre_estudiante)

        input("Presione Enter para continuar... ")

"""
est_id: int
opc: string
"""
def vista_perfil_estudiantes(est_id):
    opc = ""
    realizo_matcheo = False

    while opc != "N":
        vista_perfil_estudiante(est_id)
        marcar_match(est_id, realizo_matcheo)

        opc = input("\nRealizar un nuevo match, S/N: ").upper()

        while opc != "S" and opc != "N":
            limpiar_consola()
            opc = input("Realizar un nuevo match, S/N: ").upper()

        if opc == "S" and not realizo_matcheo:
            realizo_matcheo = True

"""
opcion: string
"""
def mostrar_menu_principal_estudiante():
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
acceso_valido: Arreglo de 0 a 1 de string
intentos, ind: int
email, password: string
login_valido: bool
"""
def log_in():
    acceso_valido = [""]*2
    intentos = 3

    limpiar_consola()
    print("\n........Ingreso........\n")

    while intentos > 0 and acceso_valido[0] == "":
        email = input("Ingrese su email: ")
        password = getpass("Ingrese su contraseña: ")

        ind = 0
        while ind < 8 and (estudiantes[ind][1] != email or estudiantes[ind][2] != password):
            ind = ind + 1

        login_valido = ind < 8 and estudiantes[ind][10] != ESTADO_ESTUDIANTE[0]

        if login_valido:
            acceso_valido[0] = str(ind + 1)
            acceso_valido[1] = ROLES[0]
        else:
            ind = 0
            while ind < 4 and (moderadores[ind][1] != email or moderadores[ind][2] != password):
                ind = ind + 1

            login_valido = ind < 4

            if login_valido:
                acceso_valido[0] = str(ind + 1)
                acceso_valido[1] = ROLES[1]
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
valores: Arreglo de 0 a 2 de int
cand: Arreglo de 0 a 2 de string
ind: int
"""
def calcular_eleccion_candidatos(valores, cand):
    for ind in range(3):
        valores[ind] = random.randint(0, 100) * int(cand[ind][3])

"""
candidatos: Arreglo de 3x3 de string
est_id, ind: int
nuevo_candidato: bool
"""
def comprobar_nuevo_candidato(candidatos, est_id):
    nuevo_candidato = True

    for ind in range(3):
        if candidatos[ind][0] == est_id:
            nuevo_candidato = False

    return nuevo_candidato

"""
cand: Arreglo de 0 a 2 de string
ind, total: int
"""
def calcular_probabilidad_total_candidatos(cand):
    total = 0

    for ind in range(3):
        total = total + int(cand[ind][2])

    return total

"""
cand: Arreglo de 0 a 2 de string
ind: int
"""
def mostrar_candidatos(cand):
    for ind in range(3):
        print(f"{ind + 1}. {cand[ind][1]}")

    print("\n")

"""
valores: Arreglo de 0 a 2 de int
ind, mayor, pos, valor: int
"""
def buscar_candidato_mayor_valor(valores):
    mayor = -1
    pos = 0

    for ind in range(3):
        valor = valores[ind]

        if valores[ind] > mayor:
            mayor = valor
            pos = ind

    return pos

"""
valores: Arreglo de 0 a 2 de int
cand: Arreglo de 0 a 2 de string
est_id, pos: int
nombre_match: string
"""
def matchear_candidato(valores, cand, est_id):
    pos = buscar_candidato_mayor_valor(valores)

    nombre_match = cand[pos][1]
    me_gusta[est_id - 1][pos] = True

    print("\nTu match es la persona", nombre_match)

"""
person_name: string
probabilidad_match_1, probabilidad_match_2, probabilidad_match_3: int
"""
# TODO
def ruleta(estudiante_id):
    continuar = ""
    cant_estudiantes = contar_estudiantes_activos_no_matcheados(estudiante_id)

    while continuar != "N" and cant_estudiantes < 3:
        limpiar_consola()

        if cant_estudiantes < 3:
            print("No hay suficientes estudiantes activos para esta función.")
        else:
            candidatos = [[""]*3 for n in range(3)]
            cant_candidatos = 0

            # TODO
            # Se reducen los casos pero no tanto se podría mejorar con un while hasta que lo encuentre
            while cant_candidatos < 3:
                est_id = random.randint(0, cant_estudiantes - 1)

                if estudiante_id != est_id:
                    if not comprobar_nuevo_candidato(candidatos[:], est_id):
                        if comprobar_nuevo_candidato(candidatos[:], est_id - 1):
                            est_id = est_id - 1
                        elif comprobar_nuevo_candidato(candidatos[:], est_id + 1):
                            est_id = est_id + 1

                    candidatos[cant_candidatos][0] = est_id
                    candidatos[cant_candidatos][1] = obtener_nombre_estudiante_por_id(est_id)
                    candidatos[cant_candidatos][2] = "0"

                    cant_candidatos = cant_candidatos + 1

            print("........RULETA........")
            print(
                "A continuación, se le pedirá ingresar la probabilidad de matcheo con tres estudiantes."
            )
            print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

            while calcular_probabilidad_total_candidatos(candidatos[:]) != 100:
                mostrar_candidatos(candidatos[:])

                probabilidades_ingresadas = 0

                print("\n")
                while probabilidades_ingresadas < 3:
                    valor = input(f"Ingresar la probabilidad del estudiante {str(probabilidades_ingresadas + 1)}: ")

                    while not valor.isnumeric():
                        valor = input("Por favor ingrese un valor numérico entero: ")

                    candidatos[probabilidades_ingresadas][2] = valor
                    probabilidades_ingresadas = probabilidades_ingresadas + 1

                probabilidad_total = calcular_probabilidad_total_candidatos(candidatos[:])

                if probabilidad_total != 100:
                    limpiar_consola()
                    print(
                        "\n\nLa probabilidad total debe ser igual a 100 y el introducido es",
                        probabilidad_total,
                        ".",
                    )
                    print("Vuelva a introducir los valores.\n\n")

            valores_eleccion_candidatos = [0]*3
            calcular_eleccion_candidatos(valores_eleccion_candidatos, candidatos[:])
            matchear_candidato(valores_eleccion_candidatos[:], candidatos[:], est_id)

        continuar = input("Usar la ruleta nuevamente. S/N ")
        continuar = validar_continuacion(continuar)
        cant_estudiantes = contar_estudiantes_activos_no_matcheados(estudiante_id)

"""
est_id, reporte_id: int
decision, motivo, opc, reportado_id: string
"""
def reportar_candidato(est_id):
    decision = ""

    while decision != "N":
        reportado_id = input("Ingrese el nombre o el id del candidato: ")

        if not reportado_id.isdigit():
            reportado_id = str(obtener_id_estudiante_por_nombre(reportado_id))

        if str(est_id) == reportado_id or not validar_id_estudiante(reportado_id):
            print("El usuario ha reportar no es válido.\n")
        else:
            limpiar_consola()
            opc = input("Seguro que desea continuar con reporte del candidato. S/N ").upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                motivo = input("Motivo:\n\t")

                while motivo == "":
                    print("Debe ingresar el motivo del reporte.")
                    motivo = input("Por favor. Ingrese el motivo:\n\t")

                reporte_ind = contar_reportes()
                reporte_id = reporte_ind + 1

                if reporte_ind == cant_total_reportes:
                    print("\nError al generar el reporte.")
                else:
                    reportes[reporte_ind][0] = str(reporte_id)
                    reportes[reporte_ind][1] = str(est_id)
                    reportes[reporte_ind][2] = reportado_id
                    reportes[reporte_ind][3] = motivo
                    reportes[reporte_ind][4] = ESTADO_REPORTE[0]

                    print("Reporte generado con éxito.")

                input("Presione Enter para continuar... ")
                decision = input("\nGenerar un nuevo reporte. S/N: ").upper()
                decision = validar_continuacion(decision)

    input("abs")

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
            reportar_candidato(estudiante_id)

"""
opc: string
"""
def submenu_matcheos():
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
max_dia_febrero, dia, mes, anio: int
es_valido: bool
"""
def validar_valores_fecha(dia, mes, anio):
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
est_id, ind: int
prop, valor: str
"""
def actualizar_estudiante(est_id, prop, valor):
    ind = 0

    while ind < 7 and prop != PROPS_ESTUDIANTE[ind]:
            ind = ind + 1

    estudiantes[est_id - 1][ind + 3] = valor

"""
est_id: int
eliminado: bool
opc: string
"""
def eliminar_perfil(est_id):
    eliminado = False

    print("\n")
    opc = input("¿Desea eliminar su perfil? (S/N) ").upper()
    opc = validar_continuacion(opc)

    if opc == "S":
        estudiantes[est_id - 1][10] = ESTADO_ESTUDIANTE[0]
        eliminado = True

        print("Perfil borrado con exito.")
        input("Presione Enter para continuar ")

    return eliminado

"""
estudiante_id: int
opc: string
"""
def submenu_gestionar_perfil(estudiante_id):
    opc = ""

    while opc != "c":
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
            editar_datos_estudiante(estudiante_id)
        elif opc == "b":
            eliminado = eliminar_perfil(estudiante_id)

            if eliminado:
                opc = "c"


"""
est_id, ind: int
"""
def mostrar_datos_estudiante(est_id):
    print("Datos de usuario\n")

    for ind in range(3, 10):
        print(PROPS_ESTUDIANTE[ind - 3], ":", estudiantes[est_id - 1][ind])

"""
estudiante_id: int
opc, valor: str   
"""
def editar_datos_estudiante(estudiante_id):
    opc = ""

    while opc != "n":
        limpiar_consola()
        mostrar_datos_estudiante(estudiante_id)

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
        while opc != "a" and opc != "b" and opc != "c" and opc != "d" and opc != "e" and opc != "f" and opc != "n":
            print("No es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        match opc:
            case "a":
                valor = solicitar_fecha_nacimiento()
                actualizar_estudiante(estudiante_id, PROPS_ESTUDIANTE[0], valor)
            case "b":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[2])
                actualizar_estudiante(estudiante_id, PROPS_ESTUDIANTE[2], valor)
            case "c":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[3])
                actualizar_estudiante(estudiante_id, PROPS_ESTUDIANTE[3], valor)
            case "d":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[4])
                actualizar_estudiante(estudiante_id, PROPS_ESTUDIANTE[4], valor)
            case "e":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[5])
                actualizar_estudiante(estudiante_id, PROPS_ESTUDIANTE[5], valor)
            case "f":
                valor = ingresar_propiedad(PROPS_ESTUDIANTE[6])
                actualizar_estudiante(estudiante_id, PROPS_ESTUDIANTE[6], valor)

"""
est_id, ind, likes_dados, likes_recibidos, matches: int
like_dado, like_recibido: bool
porcentaje: float
"""
def reportes_estadisticos_estudiante(est_id):
    likes_dados = 0
    likes_recibidos = 0
    matches = 0

    for ind in range(8):
        like_dado = me_gusta[est_id - 1][ind]
        like_recibido = me_gusta[ind][est_id]

        if est_id - 1 != ind:
            if like_dado and like_recibido:
                matches = matches + 1
            elif like_dado and not like_recibido:
                likes_dados = likes_dados + 1
            elif not like_dado and like_recibido:
                likes_recibidos = likes_recibidos + 1

    porcentaje = 0

    if likes_dados != 0 or likes_recibidos != 0 or matches != 0:
        porcentaje = matches / (likes_recibidos + likes_dados + matches) * 100

    limpiar_consola()
    print(f"Matcheados sobre el % posible: {porcentaje:.2f}%")
    print("Likes dados y no recibidos:", likes_dados)
    print("Likes recibidos y no respondidos:", likes_recibidos)
    input("Presiona Enter para volver al menú... ")

"""
est_id: int
opcion_menu_principal: string
"""
def menu_principal_estudiante(est_id):
    opcion_menu_principal = "1"

    while opcion_menu_principal != "0" and estudiantes[est_id - 1][10] == ESTADO_ESTUDIANTE[1]:
        opcion_menu_principal = mostrar_menu_principal_estudiante()

        match opcion_menu_principal:
            case "1":
                submenu_gestionar_perfil(est_id)

            case "2":
                submenu_gestionar_candidatos(est_id)

            case "3":
                submenu_matcheos()

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

"""
opc: string
"""
def mostrar_menu_principal_moderadores():
    limpiar_consola()

    print("\n........Home........")
    print("1. Gestionar Usuarios")
    print("2. Gestionar Reportes")
    print("3. Reportes Estadísticos")
    print("0. Salir")

    opc = input("\nSeleccione una opción: ")

    while (
        opc != "1"
        and opc != "2"
        and opc != "3"
        and opc != "0"
    ):
        print("\nLa opción introducida no es válida.")
        opc = input("Por favor, introduzca una opción válida: ")

    return opc

"""
decision, estudiante, opc: string
"""
def desactivar_usuario():
    decision = "S"

    while decision == "S":
        limpiar_consola()
        estudiante = input("Ingrese el ID o el nombre del usuario: ")

        if not estudiante.isdigit():
            estudiante = str(obtener_id_estudiante_por_nombre(estudiante))

        if estudiantes[int(estudiante) - 1][10] == ESTADO_ESTUDIANTE[0] or  not validar_id_estudiante(estudiante):
            print("El usuario no existe o ya está desactivado.\n")
        else:
            limpiar_consola()
            opc = input("Seguro que desea continuar con la desactivación del usuario. S/N ").upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                estudiantes[int(estudiante) - 1][10] = ESTADO_ESTUDIANTE[0]

                print("Perfil borrado con exito.")

        input("Presione Enter para continuar ")

        limpiar_consola()
        decision = input("Desactivar otra cuenta. S/N: ").upper()
        decision = validar_continuacion(decision)

"""
opc: string
"""
def submenu_gestionar_usuarios():
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
            desactivar_usuario()

"""
reporte: Arreglo de 0 a 3 de string
nombre_reportante, nombre_reportado: string
"""
def mostrar_reporte(reporte):
    nombre_reportante = obtener_nombre_estudiante_por_id(reporte[1])
    nombre_reportado = obtener_nombre_estudiante_por_id(reporte[2])

    print(f"........Reporte {reporte[0]}........\n")
    print("Reportante:", nombre_reportante)
    print("Reportado:", nombre_reportado)
    print(f"Motivo:\n\t{reporte[3]}\n\n")

"""
reporte: Arreglo de 0 a 3 de string
opc, reportado_id: string
"""
def procesar_reporte(reporte, opc):
    if opc == "1":
        reporte[4] = ESTADO_REPORTE[2]
    elif opc == "2":
        reportado_id = reporte[2]
        reporte[4] = ESTADO_REPORTE[1]
        estudiantes[reportado_id - 1][10] = ESTADO_ESTUDIANTE[0]

"""
reporte: Arreglo de 0 a 3 de string
opc: string
"""
def procesamiento_reporte(reporte):
    print("Procesamiento de reporte\n")
    print("1. Ignorar reporte")
    print("2. Bloquear al reportado")

    opc = input("\n\nSeleccione una opción: ")

    while opc != "1" and opc != "2":
        print("\nNo es una opción válida.")
        opc = input("Ingrese una opción válida: ")

    procesar_reporte(reporte, opc)

"""
reporte: Arreglo de 0 a 3 de string
continuar, estudiantes_activos: bool
cant_reportes_alta, ind: int
estado_reportante, estado_reportado, estado_reporte, opc: string
"""
def ver_reportes():
    continuar = True
    ind = 0
    cant_reportes_alta = contar_reportes()

    while ind < cant_reportes_alta and continuar:
        reporte = reportes[ind]

        estado_reportante = obtener_estado_estudiante_por_id(reporte[1])
        estado_reportado = obtener_estado_estudiante_por_id(reporte[2])
        estado_reporte = reporte[4]

        estudiantes_activos = estado_reportado == ESTADO_ESTUDIANTE[1] and estado_reportante == ESTADO_ESTUDIANTE[1]

        if estudiantes_activos and estado_reporte == ESTADO_REPORTE[0]:
            mostrar_reporte(reporte[:])
            procesamiento_reporte(reporte)

            opc = input("Continuar revisando reportes. (S/N) ").upper()
            opc = validar_continuacion(opc)

            continuar = opc == "S"

        ind = ind + 1

    if ind == cant_reportes_alta:
        print("No quedan más reportes pendientes.")
        input("Presione Enter para continuar... ")

"""
opc: string
"""
def submenu_gestionar_reportes():
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
            ver_reportes()

"""
opc: string
"""
def menu_principal_moderador():
    opc = "1"

    while opc != "0":
        opc = mostrar_menu_principal_moderadores()

        match opc:
            case "1":
                submenu_gestionar_usuarios()

            case "2":
                submenu_gestionar_reportes()

            case "3":
                en_construccion()

            case "0":
                limpiar_consola()
                print("¡Hasta luego!")

"""
usuario_id: int
rol: string
"""
def mostrar_menu_usuario(usuario_id, rol):
    if rol == ROLES[0]:
        menu_principal_estudiante(usuario_id)
    elif rol == ROLES[1]:
        menu_principal_moderador()

"""
usuario: Arreglo de 0 a 1 de string
usuario_id: int
opc, rol: string
"""
def main():
    # cargar_estudiantes(estudiantes)
    # cargar_moderador(moderadores)
    inicializar_estudiantes_mock(estudiantes)
    inicializar_moderadores_mock(moderadores)
    inicializar_reportes_mock()

    opc = ""

    while opc != "0":
        opc = mostrar_menu_principal()

        match opc:
            case "0":
                limpiar_consola()
                print("¡Hasta luego!")
            case "1":
                usuario = log_in() # usuario = [id, rol]
                usuario_id = usuario[0]

                if usuario_id != "":
                    rol = usuario[1]

                    mostrar_menu_usuario(int(usuario_id), rol)
                else:
                    opc = "0"
            case "2":
                registrar()

main()
