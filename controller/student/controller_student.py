"""
    Alta, baja y modificación de un estudiante.
    Actualmente para la 1° del TP sólo la modificación de un estudiante
"""

from constant.student_feature import BIRTH_DAY, BIOGRAPHY, HOBBIES
import db.students


def update_student(student_id, feature, value):

    if student_id == db.students.STUDENT_1_EMAIL:
        if feature == BIRTH_DAY:
            db.students.student_1_birth_day = value
        elif feature == BIOGRAPHY:
            db.students.student_1_biography = value
        elif feature == HOBBIES:
            db.students.student_1_hobbies = value

    if student_id == db.students.STUDENT_2_EMAIL:
        if feature == BIRTH_DAY:
            db.students.student_2_birth_day = value
        elif feature == BIOGRAPHY:
            db.students.student_2_biography = value
        elif feature == HOBBIES:
            db.students.student_2_hobbies = value

    if student_id == db.students.STUDENT_3_EMAIL:
        if feature == BIRTH_DAY:
            db.students.student_3_birth_day = value
        elif feature == BIOGRAPHY:
            db.students.student_3_biography = value
        elif feature == HOBBIES:
            db.students.student_3_hobbies = value
