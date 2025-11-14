from pass_logic import login, log_event, COLORES, limpiar_pantalla
from modulo import (
    register_book, register_client, list_books,
    lend_book, return_book, initialize_files, listar_bloqueados, get_clients,
    reporte_prestamos_por_genero_pais, conteo_libros_por_autor, promedio_edad_por_ciudad
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


def mostrar_reporte_paginado(datos, titulo, columna1, columna2, page_size=PAGE_SIZE):
    total = len(datos)
    print(COLORES["bright"] + f"\n{titulo} ({total}):" + COLORES["reset"])

    if not datos:
        print(COLORES["alerta"] + "No hay datos para mostrar." + COLORES["reset"])
        return

    pagina = 0
    while True:
        inicio = pagina * page_size
        if inicio >= total:
            print(COLORES["alerta"] + "No hay más datos para mostrar." + COLORES["reset"])
            break

        fin = min(inicio + page_size, total)
        print(
            COLORES["bright"]
            + f"\n{titulo} {inicio + 1}-{fin} de {total}:"
            + COLORES["reset"]
        )

        print(COLORES["bright"] + f"{columna1:<40} | {columna2:<15}" + COLORES["reset"])
        print("-" * 60)

        for item in datos[inicio:fin]:
            clave, valor = item
            clave_display = clave if len(clave) <= 40 else clave[:37] + "..."
            if isinstance(valor, float):
                print(f"{clave_display:<40} | {valor:.2f}")
            else:
                print(f"{clave_display:<40} | {valor:<15}")

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
        print("9. Reportes y estadísticas 📊")
        print("10. Salir 🚪")

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
            print(COLORES["bright"] + "\n════════ REPORTES Y ESTADÍSTICAS ════════" + COLORES["reset"])
            print("1. Reporte matricial: Préstamos por género y país 📊")
            print("2. Conteo de libros por autor 📚")
            print("3. Promedio de edad de usuarios por ciudad 👥")
            print("4. Volver al menú principal ↩️")
            
            sub_opcion = input("Seleccione una opción: ")
            
            if sub_opcion == "1":
                try:
                    matriz, paises, generos = reporte_prestamos_por_genero_pais()
                    
                    if not paises or not generos:
                        print(COLORES["alerta"] + "⚠ No hay datos suficientes para generar el reporte." + COLORES["reset"])
                    else:
                        print(COLORES["bright"] + "\n📊 REPORTE MATRICIAL: Libros por Género y País" + COLORES["reset"])
                        print("=" * 80)
                        
                        ancho_columna = max(15, max(len(p) for p in paises) + 2)
                        ancho_genero = max(15, max(len(g) for g in generos) + 2)
                        
                        header = f"{'País':<{ancho_columna}}"
                        for genero in generos:
                            header += f" | {genero:<{ancho_genero}}"
                        header += " | Total"
                        print(COLORES["bright"] + header + COLORES["reset"])
                        print("-" * len(header))
                        
                        total_general = 0
                        for pais in paises:
                            fila = f"{pais:<{ancho_columna}}"
                            total_fila = 0
                            for genero in generos:
                                cantidad = matriz.get(pais, {}).get(genero, 0)
                                total_fila += cantidad
                                fila += f" | {cantidad:<{ancho_genero}}"
                            fila += f" | {total_fila}"
                            print(fila)
                            total_general += total_fila
                        
                        print("-" * len(header))
                        total_fila = f"{'TOTAL':<{ancho_columna}}"
                        for genero in generos:
                            total_col = sum(matriz.get(p, {}).get(genero, 0) for p in paises)
                            total_fila += f" | {total_col:<{ancho_genero}}"
                        total_fila += f" | {total_general}"
                        print(COLORES["bright"] + total_fila + COLORES["reset"])
                        
                        log_event("reporte_matricial", "INFO", "Reporte matricial generado.", usuario=usuario)
                except Exception as e:
                    print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
                    log_event("reporte_matricial_error", "ERROR", str(e), usuario=usuario)
            
            elif sub_opcion == "2":
                try:
                    conteo = conteo_libros_por_autor()
                    
                    if not conteo:
                        print(COLORES["alerta"] + "⚠ No hay libros registrados." + COLORES["reset"])
                    else:
                        ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
                        mostrar_reporte_paginado(
                            ordenado,
                            "📚 CONTEO DE LIBROS POR AUTOR",
                            "Autor",
                            "Cantidad"
                        )
                        log_event("conteo_autores", "INFO", "Conteo de libros por autor generado.", usuario=usuario)
                except Exception as e:
                    print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
                    log_event("conteo_autores_error", "ERROR", str(e), usuario=usuario)
            
            elif sub_opcion == "3":
                try:
                    promedios = promedio_edad_por_ciudad()
                    
                    if not promedios:
                        print(COLORES["alerta"] + "⚠ No hay datos suficientes para calcular promedios." + COLORES["reset"])
                    else:
                        ordenado = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
                        mostrar_reporte_paginado(
                            ordenado,
                            "👥 PROMEDIO DE EDAD DE USUARIOS POR CIUDAD",
                            "Ciudad",
                            "Promedio Edad"
                        )
                        log_event("promedio_edad_ciudad", "INFO", "Promedio de edad por ciudad generado.", usuario=usuario)
                except Exception as e:
                    print(COLORES["error"] + f"❌ Error: {e}" + COLORES["reset"])
                    log_event("promedio_edad_ciudad_error", "ERROR", str(e), usuario=usuario)
            
            elif sub_opcion == "4":
                continue
            else:
                print(COLORES["alerta"] + "⚠ Opción inválida." + COLORES["reset"])

        elif opcion == "10":
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
