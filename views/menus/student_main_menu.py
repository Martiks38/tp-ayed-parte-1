"""
    Home de los estudiantes
"""


def view_student_main_menu():
    print("\n")

    print("Home")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("0. Salir")

    option = input("\n¿Qué deseas hacer? ")

    invalid_option = (
        option != "1"
        and option != "2"
        and option != "3"
        and option != "4"
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
            and option != "0"
        )

    return option
