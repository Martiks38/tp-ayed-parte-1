"""
  Detalla los datos de un estudiante
"""

from datetime import datetime


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
