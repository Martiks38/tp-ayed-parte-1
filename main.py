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
PROP_EDIT_ESTUDIANTES: Arreglo de 0 a 5 de string
PROPS_ADICIONALES_ESTUDIANTES: Arreglo de 0 a 5 de string
ESTADO_ESTUDIANTE: Arreglo de 0 a 1 de string
ESTADO_REPORTE: Arreglo de 0 a 2 de string
SEXO: Arreglo de 0 a 1 de string
ROLES: Arreglo de 0 a 1 de string
"""
NACIMIENTO = "nacimiento"
BIOGRAFIA = "biografia"
HOBBIES = "hobbies"
CIUDAD = "ciudad"
PAIS = "pais"
SEXO = ["F", "M"]
PROP_EDIT_ESTUDIANTES = ["nacimiento", "biografía", "hobbies", "sexo", "ciudad", "pais"]
PROPS_ADICIONALES_ESTUDIANTES = ["nombre", "biografía", "hobbies", "sexo", "ciudad", "pais"]
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
cant, ind: int
"""
def contar_estudiantes_activos():
    cant = 0

    for ind in range(8):
        if estudiantes[ind][7] == ESTADO_ESTUDIANTE[1]:
            cant = cant + 1

    return cant

"""
cant_estudiantes, ind: int
est_id: string
encontrado, valido: bool
"""
def validar_id_estudiante(est_id):
    valido = False
    encontrado = False
    cant_estudiantes = contar_estudiantes_activos()
    ind = 0

    while ind < cant_estudiantes and not encontrado:
        estudiante = estudiantes[ind]

        if estudiante[0] == est_id:
            valido = estudiante[7] == ESTADO_ESTUDIANTE[1]
            encontrado = True

    return valido

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
    print("Se detectó un hueco.\n")
    print(f"Los valores faltantes entre {edad_1} y {edad_2} son:\n")

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
        # Dado que las edades no se repiten la diferencia entre edades es 1
        edad_1 = edades[ind]
        edad_2 = edades[ind + 1]

        if edad_2 - edad_1 != 1:
            cant_huecos = cant_huecos + 1
            mostrar_valores_faltantes(edad_1, edad_2)

    if cant_huecos != 0:
        print(f"Se encontraron {cant_huecos} entre las edades de los 6 estudiantes.")
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

    print("Las edades de los estudiantes obtenidas del reporte son:")
    mostrar_edades(edades)

    ordenar_edades_creciente(edades)
    detectar_huecos_entre_edades(edades[:])

"""
cant_est, cant_matcheos: int
"""
def matcheos_combinados():
    cant_est = contar_estudiantes_activos()
    cant_matcheos = cant_est*(cant_est - 1)/2

    print(f"La cantidad de matcheos posibles entre {cant_est} estudiantes es: {cant_matcheos}.")

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
"""
def registrar_estudiante(email, password, cant):
    if cant == 8 or not email_existente(email):
        print("Se produjo un error al registrarse.")
        input("Presione Enter para continuar... ")
    else:
        print("Fecha de nacimiento\n")
        fecha = solicitar_fecha_nacimiento()

        estudiantes[cant][0] = cant + 1
        estudiantes[cant][1] = email
        estudiantes[cant][2] = password
        estudiantes[cant][3] = fecha
        estudiantes[cant][7] = ESTADO_ESTUDIANTE[1]

        for ind in range(4, 11):
            if ind != 7:
                estudiantes[cant][ind] = ingresar_propiedad(PROPS_ADICIONALES_ESTUDIANTES[ind - 4])

        print("Registro exitoso!!!")
        input("Presione Enter para continuar...")

"""
email, password: string
cant: int
"""
def registrar_moderador(email, password, cant):
    if cant == "4" or not email_existente(email):
        print("Se produjo un error al registrarse.")
        input("Presione Enter para continuar... ")
    else:
        moderadores[cant][0] = cant + 1
        moderadores[cant][1] = email
        moderadores[cant][2] = password
        print("Registro exitoso!!!")
        input("Presione Enter para continuar...")

"""
bio, email, fecha, password, rol: string
cant: int
"""
def registrar():
    limpiar_consola()

    print("\n........Registro........\n")

    email = ingresar_propiedad("email")
    password = ingresar_contrasenia()
    rol = input("Ingrese el rol estudiante(E) o moderador(M). (E/M): ").upper()

    while rol != "E" and rol != "M":
        print("\nNo es un rol válido.")
        rol = input("ingrese E (Estudiante) o M (Moderador): ")

    limpiar_consola()

    if rol == "E":
        cant = contar_estudiantes()
        registrar_estudiante(email, password, cant)

    elif rol == "M":
        cant = contar_moderadores()
        registrar_moderador(email, password, cant)

    limpiar_consola()

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
    est[0][7] = ESTADO_ESTUDIANTE[1]
    est[0][8] = SEXO[1]
    est[0][9] = "Rosario"
    est[0][10] = "Argentina"

    est[1][0] = "2"
    est[1][1] = "estudiante2@ayed.com"
    est[1][2] = "333444"
    est[1][3] = "1998-04-11"
    est[1][4] = "María García"
    est[1][5] = "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
    est[1][6] = "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"
    est[1][7] = ESTADO_ESTUDIANTE[1]
    est[1][8] = SEXO[0]
    est[1][9] = "Madrid"
    est[1][10] = "España"

    est[2][0] = "3"
    est[2][1] = "estudiante3@ayed.com"
    est[2][2] = "555666"
    est[2][3] = "2005-06-30"
    est[2][4] = "Carlos Martínez"
    est[2][5] = "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
    est[2][6] = "Correr - Tocar la guitarra - Cocinar platos internacionales"
    est[2][7] = ESTADO_ESTUDIANTE[1]
    est[2][8] = SEXO[1]
    est[2][9] = "La Paz"
    est[2][10] = "Bolivia"

    est[3][0] = "4"
    est[3][1] = "estudiante4@ayed.com"
    est[3][2] = "789101"
    est[3][3] = "2001-09-15"
    est[3][4] = "Ana López"
    est[3][5] = "Ana López es una estudiante de ingeniería informática interesada en la inteligencia artificial y la ciberseguridad. Aspira a desarrollar tecnologías innovadoras que mejoren la seguridad digital."
    est[3][6] = "Leer ciencia ficción - Pintar - Practicar yoga"
    est[3][7] = ESTADO_ESTUDIANTE[1]
    est[3][8] = SEXO[0]
    est[3][9] = "Asuncion"
    est[3][10] = "Paraguay"

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
    for ind in range(8):
        if estudiantes[ind] != str(est_id):
            estudiante = estudiantes[ind]

            edad = calcular_edad(estudiante[3])
            formato_espaniol_nacimiento = formatear_fecha_espaniol(estudiante[3])

            print("Nombre:", estudiante[4])
            print("Fecha de nacimiento:", formato_espaniol_nacimiento)
            print("Edad:", edad)
            print("Biografía:\n\t" + estudiante[5])
            print("Hobbies:\n\t", estudiante[6])
            print("\n")

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

    return estudiantes[ind][7]

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
def marcar_match(est_id):
    decision = input("Le gustaría en un futuro hacer matcheo con algún estudiante. (S/N) ")

    while decision != "S" and decision != "N":
        decision = input("Desea hacer matcheo con algún estudiante S o N: ")

    if decision == "S":
        nombre_estudiante = input(
            "Ingrese el nombre del estudiante con el que quiere hacer matcheo: "
        )

        nombre_estudiante = validar_nombre(nombre_estudiante)
        match_id = obtener_id_estudiante_por_nombre(nombre_estudiante)

        me_gusta[est_id - 1][match_id - 1] = True

"""
est_id: int
"""
def vista_perfil_estudiantes(est_id):
    vista_perfil_estudiante(est_id)
    marcar_match(est_id)

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

        login_valido = False

        # TODO
        # Cambiar los for por while
        for ind in range(8):
            login_valido = estudiantes[ind][1] == email and estudiantes[ind][2] == password

            if login_valido:
                acceso_valido[0] = str(ind + 1)
                acceso_valido[1] = ROLES[0]

        if not login_valido:
            for ind in range(4):
                login_valido = moderadores[ind][1] == email and moderadores[ind][2] == password

                if login_valido:
                    acceso_valido[0] = str(ind + 1)
                    acceso_valido[1] = ROLES[1]

            if not login_valido:
                limpiar_consola()
                intentos = intentos - 1
                print("Datos incorrectos. Intentos restantes:", intentos, "\n")

    if intentos == 0:
        print("Ha superado el número máximo de intentos. El programa se cerrará.")

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
    # Hacer esto ciclo mientras el usuario quiera y la cantidad
    #  cant_estudiantes-1 sea mayor que tres pero con cada sigo se le debe restar uno más
    limpiar_consola()

    # TODO
    # Añadir filtro que tampoco ya les haya dado match
    cant_estudiantes = contar_estudiantes_activos()

    if cant_estudiantes - 1 < 4:
        print("No hay suficientes estudiantes activos para esta función.")
    else:
        candidatos = [[""]*3 for n in range(3)]
        cant_candidatos = 0

        # TODO
        # Se reducen los casos pero no tanto se podría mejorar con un while hasta que lo encuentre
        while cant_candidatos < 3:
            est_id = random.randint(1, cant_estudiantes)

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

"""
est_id, reporte_id: int
decision, motivo, opc, reportado_id: string
"""
def reportar_candidato(est_id):
    decision = "S"

    while decision == "S":
        reportado_id = input("Ingrese el nombre o el id del candidato: ")

        if not reportado_id.isdigit():
            reportado_id = str(obtener_id_estudiante_por_nombre(reportado_id))

        if validar_id_estudiante(reportado_id):
            print("El usuario ha reportar no existe.\n")
        else:
            limpiar_consola()
            opc = input("Seguro que desea continuar con reporte del candidato. S/N ").upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                motivo = input("Motivo:\n\t")

                while motivo == "":
                    print("Debe ingresar el motivo del reporte.")
                    motivo = input("Por favor. Ingrese el motivo:\n\t")

                reporte_id = contar_reportes()

                reportes[reporte_id][0] = str(reporte_id + 1)
                reportes[reporte_id][1] = str(est_id)
                reportes[reporte_id][2] = reportado_id
                reportes[reporte_id][3] = motivo
                reportes[reporte_id][4] = ESTADO_REPORTE[0]

                print("Reporte generado con éxito.")
                input("Presione Enter para continuar... ")

                limpiar_consola()
                decision = input("Generar un nuevo reporte. S/N: ").upper()
                decision = validar_continuacion(decision)


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
estudiante: Arreglo de 0 a 7 de string
est_id: int
prop, valor: string
"""
def actualizar_estudiante(est_id, prop, valor):
    estudiante = estudiantes[est_id - 1]

    # TODO
    # hacer que con un mientras búsque el valor de índice de la propiedad para automatizar y no tener q poner los if
    # props[ind] = prop
    if prop == NACIMIENTO:
        estudiante[3] = valor
    elif prop == BIOGRAFIA:
        estudiante[5] = valor
    elif prop == HOBBIES:
        estudiante[6] = valor

"""
est_id: int
eliminado: bool
opc: string
"""
def eliminar_perfil(est_id):
    eliminado = False

    opc = input("¿Desea eliminar su perfil? (S/N) ").upper()
    opc = validar_continuacion(opc)

    if opc == "S":
        estudiantes[est_id - 1][7] = ESTADO_ESTUDIANTE[0]
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
TODO
"""
def mostrar_datos_estudiante(estudiante_id):
    print("Datos de usuario\n\n")

    print("Nombre:", estudiantes[estudiante_id - 1][4])
    # print("Sexo:", estudiantes[estudiante_id - 1][8])
    print("Fecha de nacimiento:", estudiantes[estudiante_id - 1][3])
    # print("Ciudad:", estudiantes[estudiante_id - 1][9])
    # print("País:", estudiantes[estudiante_id - 1][10])
    print("Biografía:\n", estudiantes[estudiante_id - 1][5])
    print("Hobbies:\n", estudiantes[estudiante_id - 1][6])


"""
estudiante_id: int
opcion, nacimiento, biografia, hobbies:str   
"""
def editar_datos_estudiante(estudiante_id):
    opc = ""

    while opc != "n":
        limpiar_consola()
        mostrar_datos_estudiante(estudiante_id)

        print("\n\n........Actualizar perfil........\n")
        print("a. Cambiar fecha de nacimiento")
        print("b. Cambiar sexo")
        print("c. Cambiar ciudad")
        print("d. Cambiar país")
        print("b. Editar biografía")
        print("c. Editar hobbies")
        print("n. Finalizar\n")

        opc = input("Seleccione una opción: ")

        while opc != "a" and opc != "b" and opc != "c" and opc != "n":
            print("\nNo es una opción válida.")
            opc = input("Ingrese una opción válida: ")

        if opc == "a":
            nacimiento = solicitar_fecha_nacimiento()
            actualizar_estudiante(estudiante_id, NACIMIENTO, nacimiento)

        elif opc == "b":
            biografia = input("Nueva biografía:\n")
            actualizar_estudiante(estudiante_id, BIOGRAFIA, biografia)

        elif opc == "c":
            hobbies = input("Nuevos Hobbies:\n")
            actualizar_estudiante(estudiante_id, HOBBIES, hobbies)

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

    while opcion_menu_principal != "0" and estudiantes[est_id - 1][7] == ESTADO_ESTUDIANTE[1]:
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
        estudiante = input("Ingrese el ID o el nombre del usuario: ")

        if not estudiante.isdigit():
            estudiante = str(obtener_id_estudiante_por_nombre(estudiante))

        if validar_id_estudiante(estudiante):
            print(f"El usuario de id: {estudiante} no existe.\n")
        else:
            limpiar_consola()
            opc = input("Seguro que desea continuar con la desactivación del usuario. S/N ").upper()
            opc = validar_continuacion(opc)

            if opc == "S":
                estudiantes[estudiante - 1][7] = ESTADO_ESTUDIANTE[0]

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
        estudiantes[reportado_id - 1][7] = ESTADO_ESTUDIANTE[0]

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

    opc = ""

    while opc != "0":
        opc = mostrar_menu_principal()

        match opc:
            case "0":
                limpiar_consola()
                print("¡Hasta luego!")
            case "1":
                usuario = log_in() # usuario = [id, rol]
                usuario_id = int(usuario[0])

                if usuario_id != "":
                    rol = usuario[1]
                    mostrar_menu_usuario(usuario_id, rol)
            case "2":
                registrar()

main()
