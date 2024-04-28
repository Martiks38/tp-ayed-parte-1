"""
    Opciones de las secciones del menú principal de estudiantes
"""


def view_student_submenus(menu_option):

    print("\n")
    match menu_option:
        case "1":
            print("a. Editar mis datos personales")
            print("b. Eliminar mi perfil")
            print("c. Volver")

        case "2":
            print("a. Ver candidatos")
            print("b. Reportar un candidato")
            print("c. Volver")

        case "3":
            print("a. Ver matcheos")
            print("b. Eliminar un matcheo")
            print("c. Volver")

    submenu_option = input("\n¿Qué desea hacer? ")

    invalid_submenu_option = (
        submenu_option != "a" and submenu_option != "b" and submenu_option != "c"
    )

    while invalid_submenu_option:
        print("La opción introducida no es válida.")
        submenu_option = input("Por favor, introduzca una opción válida: ")

        invalid_submenu_option = (
            submenu_option != "a" and submenu_option != "b" and submenu_option != "c"
        )

    return submenu_option
