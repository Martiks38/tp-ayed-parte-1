"""
  Permite visualizar * en la terminal de sistema operativo Windows
"""

import msvcrt
import sys


# Preguntar a profesor ya que en Windows
# getpass no muestras nada
def getpass(prompt="Password: "):
    sys.stdout.write(prompt)
    sys.stdout.flush()

    user_input = ""

    while True:
        char = msvcrt.getch().decode()
        if char in ("\r", "\n"):
            sys.stdout.write("\n")
            sys.stdout.flush()
            break

        if char == "\x03":  # Ctrl-C
            raise KeyboardInterrupt

        if char == "\x08":  # Backspace
            if len(user_input) > 0:
                user_input = user_input[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            user_input += char
            sys.stdout.write("*")
            sys.stdout.flush()

    return user_input
