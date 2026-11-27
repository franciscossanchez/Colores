from colorama import Back, Fore, Style,  init

init(autoreset=True)


def mostrar_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n======== MENÚ BIBLIOTECA ========")
    print(Fore.YELLOW + "1. Mostrar libros")
    print(Fore.GREEN + "2. Agregar libro")
    print(Fore.RED + "3. Eliminar libro")
    print(Fore.MAGENTA + "4. Salir")


def pedir_opcion():
    return input(Fore.BLUE + "Elige una opción: " + Style.RESET_ALL).strip()


def mostrar_libros(biblioteca):
    print(Back.BLUE + Fore.CYAN + "\n===== Libros en la Biblioteca =====")
    if not biblioteca:
        print(Fore.YELLOW + "No hay libros en la biblioteca.")
        return
    for titulo, autor in biblioteca.items():
        print(Fore.GREEN + titulo + Style.RESET_ALL + " : " + Fore.YELLOW + autor)


def agregar_libro(biblioteca):
    titulo = input(Fore.BLUE + "Escribe el título del libro: " + Style.RESET_ALL).strip()
    autor = input(Fore.BLUE + "Escribe el autor del libro: " + Style.RESET_ALL).strip()
    biblioteca[titulo] = autor
    print(Fore.GREEN + "Libro agregadito.")


def eliminar_libro(biblioteca):
    titulo = input(
        Fore.BLUE + "Escribe el título del libro que quieres eliminar: " + Style.RESET_ALL
    ).strip()
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(Fore.GREEN + "Libro eliminadito.")
    else:
        print(Fore.RED + "Ese libro no existe en la biblioteca.")


def despedida():
    print(Fore.MAGENTA + "Saliendo del programa... adiós.")


def opcion_invalida():
    print(Fore.RED + "Opción incorrecta, intenta de nuevo.")


def Biblio():
    biblioteca = {
        "El principito": "Antoine de Saint",
        "Don quijote de la mancha": "Miguel de cervantes",
        "Cien años de soledad": "Gabriel garcia marquez",
    }

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            mostrar_libros(biblioteca)
        elif opcion == "2":
            agregar_libro(biblioteca)
        elif opcion == "3":
            eliminar_libro(biblioteca)
        elif opcion == "4":
            despedida()
            break
        else:
            opcion_invalida()


Biblio()