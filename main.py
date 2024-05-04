"""
    Archivo de inicio
"""

import random
import math

from services.log_in import log_in
from views.menus.student_main_menu import view_student_main_menu
from views.menus.student_submenu import view_student_submenus
from views.student.view_students_profile import view_students_profile
from views.student.view_update_student_profile import view_update_student_profile


# Mock de la base de datos de estudiantes
STUDENT_1_EMAIL: str = "estudiante1@ayed.com"
STUDENT_1_PASSWORD: str = "111222"
student_1_birth_day: str = "2001/10/01"
student_1_name: str = "Juan Pérez"
student_1_biography: str = (
    "Juan Pérez es un estudiante de informática apasionado por la programación. Le encanta aprender nuevos lenguajes y tecnologías."
)
student_1_hobbies: str = "Lectura - Senderismo - Juegos de mesa"

STUDENT_2_EMAIL: str = "estudiante2@ayed.com"
STUDENT_2_PASSWORD: str = "333444"
student_2_birth_day: str = "1998/04/11"
student_2_name: str = "María García"
student_2_biography: str = (
    "María García es una estudiante de arte con una pasión por la pintura y el dibujo desde una edad temprana. Actualmente está explorando nuevas formas de expresión artística."
)
student_2_hobbies: str = (
    "Pintura al óleo - Dibujo de retratos - Lectura de novelas históricas"
)


STUDENT_3_EMAIL: str = "estudiante3@ayed.com"
STUDENT_3_PASSWORD: str = "555666"
student_3_birth_day: str = "2000/06/30"
student_3_name: str = "Carlos Martínez"
student_3_biography: str = (
    "Carlos Martínez es un estudiante de medicina enfocado en la investigación de enfermedades infecciosas. Su objetivo es contribuir al desarrollo de tratamientos más efectivos y accesibles."
)
student_3_hobbies: str = "Correr - Tocar la guitarra - Cocinar platos internacionales"


def main():
    me_gusta: str = ""

    # Login
    is_log_in: str | bool = log_in()

    if is_log_in is False:
        return

    main_menu_option: str | None = None
    submenu_opcion: str | None = None

    # Permite al usuario realizar más de una acción
    # en la misma ejecución
    while True:
        while True:
            main_menu_option = view_student_main_menu()

            if main_menu_option == "0" or main_menu_option == "4":
                break

            submenu_opcion = view_student_submenus(main_menu_option)

            if submenu_opcion != "c":
                break

        if main_menu_option == "0":
            break

        if (
            main_menu_option != "1"
            and main_menu_option != "2"
            and main_menu_option != "5"
        ) or submenu_opcion != "a":
            print("\nEn construcción")

        if main_menu_option == "1" and submenu_opcion == "a":
            view_update_student_profile(is_log_in)

        if main_menu_option == "2" and submenu_opcion == "a":
            me_gusta = view_students_profile()

        if main_menu_option == "5":
            match_roulette()


if __name__ == "__main__":
    main()


# Calculadora de valor de
# probability: int
# rand: float
def calculate_person_value(probability):
    rand = random.random()
    return math.floor(rand * probability * 100)


# Ruleta de match de estudiantes
def match_roulette():
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
