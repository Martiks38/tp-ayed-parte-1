"""
  Vista del menú de actualización del perfil de un estudiante
"""

from constant.student_feature import BIRTH_DAY, BIOGRAPHY, HOBBIES
from controller.student.controller_student import update_student
import db.students
from utils.validate_date import validate_date
from views.student.view_student_profile import view_student_profile


def view_update_student_profile(student_id):

    if student_id == db.students.STUDENT_1_EMAIL:
        view_student_profile(
            db.students.student_1_name,
            db.students.student_1_birth_day,
            db.students.student_1_biography,
            db.students.student_1_hobbies,
        )
    elif student_id == db.students.STUDENT_2_EMAIL:
        view_student_profile(
            db.students.student_2_name,
            db.students.student_2_birth_day,
            db.students.student_2_biography,
            db.students.student_2_hobbies,
        )
    elif student_id == db.students.STUDENT_3_EMAIL:
        view_student_profile(
            db.students.student_3_name,
            db.students.student_3_birth_day,
            db.students.student_3_biography,
            db.students.student_3_hobbies,
        )

    while True:
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
            break

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
