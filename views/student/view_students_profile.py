"""
  Detalla los datos de los estudiantes
"""

import db.students
from .view_student_profile import view_student_profile  # pylint: disable=E0402


def view_students_profile():
    me_gusta: str = ""

    view_student_profile(
        db.students.student_1_name,
        db.students.student_1_birth_day,
        db.students.student_1_biography,
        db.students.student_1_hobbies,
    )
    print("\n")

    view_student_profile(
        db.students.student_2_name,
        db.students.student_2_birth_day,
        db.students.student_2_biography,
        db.students.student_2_hobbies,
    )

    print("\n")

    view_student_profile(
        db.students.student_3_name,
        db.students.student_3_birth_day,
        db.students.student_3_biography,
        db.students.student_3_hobbies,
    )

    print("\n")

    to_match = input(
        "¿Quieres hacer match en algún futuro con algún estudiante? (Y/N) "
    )

    while to_match != "Y" and to_match != "N":
        to_match = input("\nSi desea hacer match con algún estudiante ingrese Y/N ")

    if to_match == "N":
        return me_gusta

    student_name = input("Ingrese el nombre del estudiante: ")
    invalid_name = (
        student_name != db.students.student_1_name
        and student_name != db.students.student_2_name
        and student_name != db.students.student_3_name
    )

    while invalid_name:
        print(f"El nombre {student_name} no existe.")
        student_name = input("Reingrese el nombre del estudiante: ")
        invalid_name = (
            student_name != db.students.student_1_name
            and student_name != db.students.student_2_name
            and student_name != db.students.student_3_name
        )

    return me_gusta
