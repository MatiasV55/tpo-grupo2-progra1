import functions as f

def show_menu():
    print("\n--- Sistema de Gestión de Biblioteca (PySGB) ---")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Listar libros disponibles")
    print("4. Listar libros prestados")
    print("0. Salir")
    
def main():
    while True:
        show_menu()
        option = input("Seleccione una opción: ")
        
        try:
            if option == "1":
                title = input("Titulo: ")
                author = input("Autor: ")
                result = f.register_book(title, author)
                print(f"Se ha registrado el libro '{title}' con el ID {result}")

            elif option == "2":
                name = input("Nombre del usuario: ")
                result = f.register_user(name)
                print(f"Se ha registrado el usuario '{name}' con el ID {result}")

            elif option == "3":
                available = f.list_available_books()
                if not available:
                    print("No hay libros disponibles.")
                for b in available:
                    print(f"ID: {b[0]} | {b[1]} - {b[2]}")

            elif option == "4":
                lent = f.list_lent_books()
                if not lent:
                    print("No hay libros prestados.")
                for b in lent:
                    print(f"ID: {b[0]} | {b[1]} - Prestado a {b[4][1]}")

            elif option == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()