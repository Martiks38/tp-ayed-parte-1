"""
    Archivo de inicio
"""

# TODO
# Terminar validate_date

import calendar
import math
import msvcrt
import os
import platform
import random
import sys
from datetime import datetime

# Campos de propiedades de estudiante
"""
BIRTH_DAY, BIOGRAPHY, HOBBIES: string
"""
BIRTH_DAY = "birth_day"
BIOGRAPHY = "biography"
HOBBIES = "hobbies"


# Mock de la base de datos de estudiantes
"""
STUDENT_1_EMAIL, STUDENT_1_PASSWORD, student_1_birth_day, student_1_name, student_1_biography, student_1_hobbies: string
"""
STUDENT_1_EMAIL = "estudiante1@ayed.com"
STUDENT_1_PASSWORD = "111222"
student_1_birth_day = "2001/10/01"
student_1_name = "Juan Pérez"
student_1_biography = "Juan Pérez es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías."
student_1_hobbies = "Lectura - Senderismo - Juegos de mesa"

"""
STUDENT_2_EMAIL, STUDENT_2_PASSWORD, student_2_birth_day, student_2_name, student_2_biography, student_2_hobbies: string
"""
STUDENT_2_EMAIL = "estudiante2@ayed.com"
STUDENT_2_PASSWORD = "333444"
student_2_birth_day = "1998/04/11"
student_2_name = "María García"
student_2_biography = "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
student_2_hobbies = (
    "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"
)

"""
STUDENT_3_EMAIL, STUDENT_3_PASSWORD, student_3_birth_day, student_3_name, student_3_biography, student_3_hobbies: string
"""
STUDENT_3_EMAIL = "estudiante3@ayed.com"
STUDENT_3_PASSWORD = "555666"
student_3_birth_day = "2000/06/30"
student_3_name = "Carlos Martínez"
student_3_biography = "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
student_3_hobbies = "Correr - Tocar la guitarra - Cocinar platos internacionales"

"""
command, so: string
"""


def clear_console():
    # Detecta el sistema operativo.
    # No se consideró el uso de implementación en un entorno de Java.
    # Retorna 'Linux', 'Darwin', 'Java', 'Windows'
    so = platform.system()

    if so == "Windows":
        command = "cls"
    else:
        command = "clear"

    os.system(command)


# Permite visualizar * en la terminal de sistema operativo Windows
# Para no instalar librerías se buscó una función que haga lo mismo
"""
char, prompt, user_input: string
"""


def getpass(prompt="Password: "):
    sys.stdout.write(prompt)
    sys.stdout.flush()

    user_input = ""

    while True:
        char = msvcrt.getch().decode()
        if char in ("\r", "\n"):
            sys.stdout.write("\n")
            sys.stdout.flush()
            break

        if char == "\x03":  # Ctrl-C
            raise KeyboardInterrupt

        if char == "\x08":  # Backspace
            if len(user_input) > 0:
                user_input = user_input[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            user_input += char
            sys.stdout.write("*")
            sys.stdout.flush()

    return user_input


# Verifica que el id y la constraseña del estudiante sean válidos
# Para esta 1° parte del id se tomará el email.
"""
student_id, student_password: string
is_student_1, is_student_2, is_student_3: boolean
"""


def student_authenticator(student_id, student_password):

    is_student_1 = (
        student_id == STUDENT_1_EMAIL and student_password == STUDENT_1_PASSWORD
    )

    is_student_2 = (
        student_id == STUDENT_2_EMAIL and student_password == STUDENT_2_PASSWORD
    )

    is_student_3 = (
        student_id == STUDENT_3_EMAIL and student_password == STUDENT_3_PASSWORD
    )

    return is_student_1 or is_student_2 or is_student_3


# Inicio de sesión de los estudiantes
"""
valid_log_in: boolean
attempst: int
email, password, valid_log_in: string
"""


def log_in():
    attempts = 0
    valid_log_in = ""

    print("\nBienvenido.")

    while attempts < 3 and valid_log_in == "" or attempts >= 3 and valid_log_in != "":
        email = input("Ingresa tu email: ")
        password = getpass("Ingresa tu contraseña: ")

        if student_authenticator(email, password):
            valid_log_in = email
        else:
            attempts += 1
            print("\nLos datos ingresados son incorrectos.\n")

    print("Ha intentado demasiadas veces. Intente más tarde.")

    return valid_log_in


# Vista principal de los estudiantes
"""
option: string
invalid_option: boolean
"""


def view_student_main_menu():
    clear_console()

    print("Home")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta match")
    print("0. Salir")

    option = input("\n¿Qué deseas hacer? ")

    invalid_option = (
        option != "1"
        and option != "2"
        and option != "3"
        and option != "4"
        and option != "5"
        and option != "0"
    )

    while invalid_option:
        print("La opción introducida no es válida.")
        option = input("Por favor, introduzca una opción válida: ")

        invalid_option = (
            option != "1"
            and option != "2"
            and option != "3"
            and option != "4"
            and option != "5"
            and option != "0"
        )

    return option


# Opciones de las secciones del menú principal de estudiantes
"""
menu_option, submenu_option: string
invalid_submenu_option: boolean
"""


def view_student_submenus(menu_option):
    clear_console()

    match menu_option:
        case "1":
            print("a. Editar mis datos personales")
            print("b. Eliminar mi perfil")
            print("c. Volver")

        case "2":
            print("a. Ver candidatos")
            print("b. Reportar un candidato")
            print("c. Volver")

        case "3":
            print("a. Ver matcheos")
            print("b. Eliminar un matcheo")
            print("c. Volver")

    submenu_option = input("\n¿Qué desea hacer? ").lower()

    invalid_submenu_option = (
        submenu_option != "a" and submenu_option != "b" and submenu_option != "c"
    )

    while invalid_submenu_option:
        print("La opción introducida no es válida.")
        submenu_option = input("Por favor, introduzca una opción válida: ")

        invalid_submenu_option = (
            submenu_option != "a" and submenu_option != "b" and submenu_option != "c"
        )

    return submenu_option


# Modificación de los datos del estudiante.
"""
feature, student_id, value: string
"""


def update_student(student_id, feature, value):
    global student_1_birth_day, student_1_biography, student_1_hobbies  # pylint: disable= W0603
    global student_2_birth_day, student_2_biography, student_2_hobbies  # pylint: disable= W0603
    global student_3_birth_day, student_3_biography, student_3_hobbies  # pylint: disable= W0603

    if student_id == STUDENT_1_EMAIL:
        if feature == BIRTH_DAY:
            student_1_birth_day = value
        elif feature == BIOGRAPHY:
            student_1_biography = value
        elif feature == HOBBIES:
            student_1_hobbies = value

    if student_id == STUDENT_2_EMAIL:
        if feature == BIRTH_DAY:
            student_2_birth_day = value
        elif feature == BIOGRAPHY:
            student_2_biography = value
        elif feature == HOBBIES:
            student_2_hobbies = value

    if student_id == STUDENT_3_EMAIL:
        if feature == BIRTH_DAY:
            student_3_birth_day = value
        elif feature == BIOGRAPHY:
            student_3_biography = value
        elif feature == HOBBIES:
            student_3_hobbies = value


# Valida que la fecha esté en formato estándar segun ISO 86011
"""
    date: string
    is_valid_date: boolean
    year, month, day: string | int
"""


def validate_date(date):
    is_valid_date = False
    # TODO cambiar
    year, month, day = date.split("-")

    are_digit = year.isdigit() and month.isdigit() and day.isdigit()

    if are_digit:
        year = int(year)
        month = int(month)
        day = int(day)
        is_valid_date = day <= calendar.monthrange(year, month)[1]

    return is_valid_date


# Vista del menú de actualización del perfil de un estudiante
"""
new_birth_date, option, student_id: string
continue_update, invalid_option: boolean
"""


def view_update_student_profile(student_id):
    continue_update = True

    if student_id == STUDENT_1_EMAIL:
        view_student_profile(
            student_1_name,
            student_1_birth_day,
            student_1_biography,
            student_1_hobbies,
        )
    elif student_id == STUDENT_2_EMAIL:
        view_student_profile(
            student_2_name,
            student_2_birth_day,
            student_2_biography,
            student_2_hobbies,
        )
    elif student_id == STUDENT_3_EMAIL:
        view_student_profile(
            student_3_name,
            student_3_birth_day,
            student_3_biography,
            student_3_hobbies,
        )

    while continue_update:
        print("1. Modificar fecha de nacimiento")
        print("2. Modificar biografía")
        print("3. Modificar hobbies")
        print("0. Salir")

        option = input("¿Qué deseas hacer? ")
        invalid_option = (
            option != "0" and option != "1" and option != "2" and option != "3"
        )

        while invalid_option:
            print("La opción introducida no es válida.")
            option = input("Por favor, introduzca una opción válida: ")

            invalid_option = (
                option != "0" and option != "1" and option != "2" and option != "3"
            )

        if option == "0":
            continue_update = False

        if option == "1":
            new_birth_date = input(
                "Introduce tu fecha de nacimiento con el formato YYYY-MM-DD:\n"
            )

            while not validate_date(new_birth_date):
                print("La fecha introducida no es válida.")
                new_birth_date = input(
                    "Introduce tu fecha de nacimiento con el formato YYYY-MM-DD:\n"
                )

            update_student(student_id, BIRTH_DAY, new_birth_date)

        elif option == "2":
            new_biography = input("Introduce tu biografía:\n")
            update_student(student_id, BIOGRAPHY, new_biography)

        elif option == "3":
            new_hobbies = input("Introduce tus hobbies, separados por espacios:\n")
            update_student(student_id, HOBBIES, new_hobbies)


# Detalla los datos de un estudiante
"""
birth_day, biography, format_birth_day, hobbies, name: string
current_date: datetime
age, day, month, year: int
"""


def view_student_profile(name, birth_day, biography, hobbies):
    current_date = datetime.now()

    year = int(birth_day[:4])
    month = int(birth_day[5:7])
    day = int(birth_day[-2:])
    format_birth_day = f"{day}/{month}/{year}"

    age = (
        current_date.year
        - year
        - (current_date.month < month and current_date.day < day)
    )

    print(f"Nombre: {name}")
    print(f"Fecha de nacimiento: {format_birth_day}")
    print(f"Edad: {age}")
    print(f"Biografía:\n\t{biography}")
    print("Hobbies:")
    print(f"\t{hobbies}")


# Detalla los datos de los estudiantes
"""
me_gusta, student_name, to_match: string
"""


def view_students_profile():
    me_gusta: str = ""

    view_student_profile(
        student_1_name,
        student_1_birth_day,
        student_1_biography,
        student_1_hobbies,
    )
    print("\n")

    view_student_profile(
        student_2_name,
        student_2_birth_day,
        student_2_biography,
        student_2_hobbies,
    )

    print("\n")

    view_student_profile(
        student_3_name,
        student_3_birth_day,
        student_3_biography,
        student_3_hobbies,
    )

    print("\n")

    to_match = input(
        "¿Quieres hacer match en algún futuro con algún estudiante? (S/N) "
    )

    while to_match != "S" and to_match != "N":
        to_match = input("\nSi desea hacer match con algún estudiante ingrese S/N ")

    if to_match == "S":
        student_name = input("Ingrese el nombre del estudiante: ")
        invalid_name = (
            student_name != student_1_name
            and student_name != student_2_name
            and student_name != student_3_name
        )

        while invalid_name:
            print(f"El nombre {student_name} no existe.")
            student_name = input("Reingrese el nombre del estudiante: ")
            invalid_name = (
                student_name != student_1_name
                and student_name != student_2_name
                and student_name != student_3_name
            )

    return me_gusta


# Calculadora de resultado de probabilidad
"""
probability: int
rand: float
"""


def calculate_person_value(probability):
    rand = random.random()
    return math.floor(rand * probability * 100)


# Ruleta de match de estudiantes
"""
person_name: string
person_match_probability_1, person_match_probability_2, person_match_probability_3, total_probability, person_value_1, person_value_2, person_value_3: int
"""


def match_roulette():
    clear_console()
    person_name = ""
    person_match_probability_1 = 0
    person_match_probability_2 = 0
    person_match_probability_3 = 0

    total_probability = (
        person_match_probability_1
        + person_match_probability_2
        + person_match_probability_3
    )

    print(
        "A continuación, se le pedirá ingresar la probabilidad de matcheo con tres persona."
    )
    print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

    while total_probability != 100:
        person_match_probability_1 = int(
            input("Introduzca la afinidad con la persona A: ")
        )

        person_match_probability_2 = int(
            input("Introduzca la afinidad con la persona B: ")
        )
        person_match_probability_3 = int(
            input("Introduzca la afinidad con la persona C: ")
        )

        total_probability = (
            person_match_probability_1
            + person_match_probability_2
            + person_match_probability_3
        )

        if total_probability != 100:
            print(
                f"La probabilidad total debe ser igual a 100 y el introducido es {total_probability}."
            )
            print("Vuelva a introducir los valores.\n")

    person_value_1 = calculate_person_value(person_match_probability_1)
    person_value_2 = calculate_person_value(person_match_probability_2)
    person_value_3 = calculate_person_value(person_match_probability_3)

    # Existe un pequeña probabilidad de que den iguales
    if person_value_2 <= person_value_1 >= person_value_3:
        person_name = "A"
    elif person_value_2 >= person_value_3:
        person_name = "B"
    else:
        person_name = "C"

    print(f"Tu match es la Persona {person_name}")


# Función de inicio de la aplicación
"""
is_log_in, main_menu_option, me_gusta, submenu_opcion: string
must_continue: boolean
"""


def main():
    me_gusta = ""
    must_continue = True

    is_log_in = log_in()

    if is_log_in != "":
        while must_continue:
            main_menu_option = ""
            submenu_opcion = ""

            while (
                main_menu_option != "0"
                and main_menu_option != "4"
                and main_menu_option != "5"
            ) or submenu_opcion == "c":
                submenu_opcion = ""
                main_menu_option = view_student_main_menu()

                # TODO modificar submenu para manejar esta comprobación
                show_submenu = (
                    main_menu_option != "0"
                    and main_menu_option != "4"
                    and main_menu_option != "5"
                )

                if show_submenu:
                    submenu_opcion = view_student_submenus(main_menu_option)

            if (
                (
                    main_menu_option != "0"
                    and main_menu_option != "1"
                    and main_menu_option != "2"
                    and main_menu_option != "5"
                )
                or submenu_opcion != "a"
                and submenu_opcion != ""
            ):
                clear_console()
                print("En construcción.")
                input("Presiona cualquier tecla para continuar...")

            if main_menu_option == "1" and submenu_opcion == "a":
                view_update_student_profile(is_log_in)

            if main_menu_option == "2" and submenu_opcion == "a":
                me_gusta = view_students_profile()

            if main_menu_option == "5":
                match_roulette()

            if main_menu_option == "0":
                must_continue = False


if __name__ == "__main__":
    main()
