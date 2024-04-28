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

    if is_student_1:
        return True

    is_student_2 = (
        student_id == db.students.STUDENT_2_EMAIL
        and student_password == db.students.STUDENT_2_PASSWORD
    )

    if is_student_2:
        return True

    is_student_3 = (
        student_id == db.students.STUDENT_3_EMAIL
        and student_password == db.students.STUDENT_3_PASSWORD
    )

    if is_student_3:
        return True

    return False
