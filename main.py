"""
    Archivo de inicio
"""

from services.log_in import log_in
from views.menus.student_main_menu import view_student_main_menu
from views.menus.student_submenu import view_student_submenus
from views.student.view_students_profile import view_students_profile
from views.student.view_update_student_profile import view_update_student_profile
import bonus_track.ruleta_match


def main():
    me_gusta: str = ""

    # Login
    is_log_in: str | bool = log_in()

    if is_log_in is False:
        return

    main_menu_option: str | None = None
    submenu_opcion: str | None = None

    # Permite al usuario realizar más de una acción
    # en la misma ejecución
    while True:
        while True:
            main_menu_option = view_student_main_menu()

            if main_menu_option == "0" or main_menu_option == "4":
                break

            submenu_opcion = view_student_submenus(main_menu_option)

            if submenu_opcion != "c":
                break

        if main_menu_option == "0":
            break

        if (
            main_menu_option != "1" and main_menu_option != "2"
        ) or submenu_opcion != "a":
            print("\nEn construcción")

        if main_menu_option == "1" and submenu_opcion == "a":
            view_update_student_profile(is_log_in)

        if main_menu_option == "2" and submenu_opcion == "a":
            me_gusta = view_students_profile()


if __name__ == "__main__":
    main()
    bonus_track.ruleta_match.match_roulette()
