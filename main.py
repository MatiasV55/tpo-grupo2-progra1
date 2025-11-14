from pass_logic import login, log_event, COLORES, limpiar_pantalla
from modulo import (
    register_book, register_client, list_books,
    lend_book, return_book, initialize_files, listar_bloqueados, get_clients
)


PAGE_SIZE = 25


def mostrar_libros(books, titulo, page_size=PAGE_SIZE):
    total = len(books)
    print(COLORES["bright"] + f"\n{titulo} ({total}):" + COLORES["reset"])

    if not books:
        print(COLORES["alerta"] + "No hay libros en esta categoría." + COLORES["reset"])
        return

    pagina = 0
    while True:
        inicio = pagina * page_size
        if inicio >= total:
            print(COLORES["alerta"] + "No hay más libros para mostrar." + COLORES["reset"])
            break

        fin = min(inicio + page_size, total)
        print(
            COLORES["bright"]
            + f"\n{titulo} {inicio + 1}-{fin} de {total}:"
            + COLORES["reset"]
        )

        print(COLORES["bright"] + f"{'ID':<6} | {'Título':<50} | {'Autor':<30} | {'Estado':<15}" + COLORES["reset"])
        print("-" * 110)

        for b in books[inicio:fin]:
            estado = "Disponible" if b[8] == 'True' else "No disponible"
            titulo_libro = b[1] if len(b[1]) <= 50 else b[1][:47] + "..."
            autor_libro = b[2] if len(b[2]) <= 30 else b[2][:27] + "..."
            print(f"{b[0]:<6} | {titulo_libro:<50} | {autor_libro:<30} | {estado:<15}")

        if fin >= total:
            break

        while True:
            continuar = input("\n¿Ver la siguiente página? (s/n): ").strip().lower()
            if continuar in ("s", "n"):
                break
            print(COLORES["alerta"] + "⚠ Opción inválida. Responda 's' o 'n'." + COLORES["reset"])

        if continuar == "n":
            break

        pagina += 1


def mostrar_clientes(clients, titulo, page_size=PAGE_SIZE):
    total = len(clients)
    print(COLORES["bright"] + f"\n{titulo} ({total}):" + COLORES["reset"])

    if not clients:
        print(COLORES["alerta"] + "No hay clientes registrados." + COLORES["reset"])
        return

    pagina = 0
    while True:
        inicio = pagina * page_size
        if inicio >= total:
            print(COLORES["alerta"] + "No hay más clientes para mostrar." + COLORES["reset"])
            break

        fin = min(inicio + page_size, total)
        print(
            COLORES["bright"]
            + f"\n{titulo} {inicio + 1}-{fin} de {total}:"
            + COLORES["reset"]
        )

        print(COLORES["bright"] + f"{'ID':<6} | {'Nombre':<30} | {'Edad':<6} | {'Ciudad':<20} | {'Préstamos':<10} | {'Strikes':<8}" + COLORES["reset"])
        print("-" * 100)

        for c in clients[inicio:fin]:
            nombre_cliente = c[1] if len(c[1]) <= 30 else c[1][:27] + "..."
            edad = c[2] if c[2] else "-"
            ciudad = c[4] if c[4] else "-"
            ciudad = ciudad if len(ciudad) <= 20 else ciudad[:17] + "..."
            prestamos = c[6] if c[6] else "0"
            strikes = c[7] if c[7] else "0"
            print(f"{c[0]:<6} | {nombre_cliente:<30} | {edad:<6} | {ciudad:<20} | {prestamos:<10} | {strikes:<8}")

        if fin >= total:
            break

        while True:
            continuar = input("\n¿Ver la siguiente página? (s/n): ").strip().lower()
            if continuar in ("s", "n"):
                break
            print(COLORES["alerta"] + "⚠ Opción inválida. Responda 's' o 'n'." + COLORES["reset"])

        if continuar == "n":
            break

        pagina += 1


def menu_principal(usuario):
    while True:
        print(COLORES["bright"] + "\n════════ MENU PySGB ════════" + COLORES["reset"])
        print("1. Registrar libro 📘")
        print("2. Registrar cliente 👤")
        print("3. Listar libros disponibles 📗")
        print("4. Listar libros prestados 📕")
        print("5. Prestar libro 🔄")
        print("6. Devolver libro ↩️")
        print("7. Listar clientes bloqueados 🚫")
        print("8. Listar clientes 👥")
        print("9. Salir 🚪")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género (opcional): ")
            anio = input("Año de publicación (opcional): ")
            editorial = input("Editorial (opcional): ")
            idioma = input("Idioma (opcional): ")
            paginas = input("Número de páginas (opcional): ")

            try:
                id_libro = register_book(titulo, autor, genero, anio, editorial, idioma, paginas)
                print(COLORES["ok"] + f"✅ Libro registrado con ID {id_libro}" + COLORES["reset"])
                log_event("register_book", "INFO", f"Libro '{titulo}' registrado.", usuario=usuario)
            except Exception as e:
                print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
                log_event("register_book_error", "ERROR", str(e), usuario=usuario)

        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            edad = input("Edad (opcional): ")
            genero = input("Género (opcional): ")
            ciudad = input("Ciudad (opcional): ")
            pais = input("País (opcional): ")

            try:
                id_client = register_client(nombre, edad, genero, ciudad, pais)
                print(COLORES["ok"] + f"✅ Cliente '{nombre}' registrado con ID {id_client}" + COLORES["reset"])
                log_event("register_client", "INFO", f"Cliente '{nombre}' registrado.", usuario=usuario)
            except Exception as e:
                print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
                log_event("register_client_error", "ERROR", str(e), usuario=usuario)

        elif opcion == "3":
            disponibles = list_books("disponible")
            mostrar_libros(disponibles, "📗 Libros Disponibles")
            log_event("list_books", "INFO", "Libros disponibles listados.", usuario=usuario)

        elif opcion == "4":
            prestados = list_books("prestado")
            mostrar_libros(prestados, "📕 Libros Prestados")
            log_event("list_books_borrowed", "INFO", "Libros prestados listados.", usuario=usuario)

        elif opcion == "5":
            try:
                mostrar_libros(list_books("disponible"), "📗 Libros Disponibles")
                book_id = input("\nIngrese el ID del libro a prestar: ").strip()
                if not book_id.isdigit():
                    raise ValueError("El ID del libro debe ser numérico.")
                nombre = input("Ingrese el nombre del cliente: ")
                lend_book(int(book_id), nombre)
                print(COLORES["ok"] + "✅ Libro prestado correctamente." + COLORES["reset"])
                log_event("lend_book", "INFO", f"Libro ID {book_id} prestado a {nombre}.", usuario=usuario)
            except Exception as e:
                print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
                log_event("lend_book_error", "ERROR", str(e), usuario=usuario)

        elif opcion == "6":
            try:
                mostrar_libros(list_books("prestado"), "📕 Libros Prestados")
                book_id = input("\nIngrese el ID del libro a devolver: ").strip()
                if not book_id.isdigit():
                    raise ValueError("El ID del libro debe ser numérico.")
                return_book(int(book_id))
                print(COLORES["ok"] + "✅ Libro devuelto correctamente." + COLORES["reset"])
                log_event("return_book", "INFO", f"Libro ID {book_id} devuelto.", usuario=usuario)
            except Exception as e:
                print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
                log_event("return_book_error", "ERROR", str(e), usuario=usuario)
                
        elif opcion == "7":
            bloqueados = listar_bloqueados()
            if not bloqueados:
                print(COLORES["ok"] + "✅ No hay clientes bloqueados actualmente." + COLORES["reset"])
            else:
                print(COLORES["alerta"] + "\n🚫 Clientes bloqueados:" + COLORES["reset"])
                for c in bloqueados:
                    print(f"ID: {c['id']} | {c['nombre']} | Strikes: {c['strikes']} | Bloqueado hasta: {c['bloqueado_hasta']}")

        elif opcion == "8":
            clientes = get_clients()
            mostrar_clientes(clientes, "👥 Clientes Registrados")
            log_event("list_clients", "INFO", "Clientes listados.", usuario=usuario)

        elif opcion == "9":
            print(COLORES["rosa"] + "👋 Saliendo del sistema. ¡Hasta luego!" + COLORES["reset"])
            log_event("logout", "INFO", "Sesión cerrada.", usuario=usuario)
            break
        else:
            print(COLORES["alerta"] + "⚠ Opción inválida." + COLORES["reset"])


def main():
    initialize_files()
    limpiar_pantalla()
    print(COLORES["bright"] + "📚 Bienvenido a PySGB" + COLORES["reset"])
    print("Sistema de Gestión de Biblioteca con Control de Clientes\n")

    try:
        usuario, _ = login()
        log_event("login_success", "INFO", "Inicio de sesión exitoso.", usuario=usuario)
        menu_principal(usuario)
    except Exception as e:
        print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
        log_event("login_failed", "ERROR", str(e), funcion="main")


if __name__ == "__main__":
    main()
