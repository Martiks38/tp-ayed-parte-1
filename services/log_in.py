"""
  Inicio de sesión de los estudiantes
"""

from controller.student.student_authenticator import student_authenticator
from utils.custom_getpass import getpass


def log_in():
    attempts = 0

    print("\nBienvenido.")

    while attempts < 3:
        email = input("Ingresa tu email: ")
        password = getpass("Ingresa tu contraseña: ")

        if student_authenticator(email, password):
            return email

        attempts += 1
        print("\nLos datos ingresados son incorrectos.\n")

    print("Ha intentado demasiadas veces. Intente más tarde.")

    return False
