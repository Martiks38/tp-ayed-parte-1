"""
  Verifica que el id y la constraseña del estudiante existan en la base de datos.
  Para esta 1° parte del id se tomará el email.
"""

import db.students


def student_authenticator(student_id, student_password):

    is_student_1 = (
        student_id == db.students.STUDENT_1_EMAIL
        and student_password == db.students.STUDENT_1_PASSWORD
    )

    is_student_2 = (
        student_id == db.students.STUDENT_2_EMAIL
        and student_password == db.students.STUDENT_2_PASSWORD
    )

    is_student_3 = (
        student_id == db.students.STUDENT_3_EMAIL
        and student_password == db.students.STUDENT_3_PASSWORD
    )

    return is_student_1 or is_student_2 or is_student_3
