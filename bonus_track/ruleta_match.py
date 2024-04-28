"""
  Ruleta de match de estudiantes
"""

import random
import math


def calculate_person_value(probability):
    rand = random.random()
    return math.floor(rand * probability * 100)


def match_roulette():
    person = ""

    print(
        "A continuación, se le pedirá ingresar la probabilidad de matcheo con tres persona."
    )
    print("Los valores ingresados deben ser enteros y su suma igual a 100.\n")

    while True:
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

        if total_probability == 100:
            break

        print(f"La probabilidad total debe ser igual a 100 y es {total_probability}")
        print("Vuelva a introducir los valores.\n")

    person_value_1 = calculate_person_value(person_match_probability_1)
    person_value_2 = calculate_person_value(person_match_probability_2)
    person_value_3 = calculate_person_value(person_match_probability_3)

    # Existe un pequeña probabilidad de que den iguales
    if person_value_2 <= person_value_1 >= person_value_3:
        person = "A"
    elif person_value_2 >= person_value_3:
        person = "B"
    else:
        person = "C"

    print(f"Tu match es la Persona {person}")
