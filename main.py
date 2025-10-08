import modulo as f

# ----------------- DATOS MOCK -----------------
# books: [[id, nombre, autor, disponible, usuario, fecha de devolucion]]
books = [
    [1, "Cien Años de Soledad", "Gabriel García Márquez", True, None, None],
    [2, "Los Miserables", "Victor Hugo", True, None, None],
    [3, "Rayuela", "Julio Cortazar", False, [1, "Ana", 0, None], "2025-12-05"],
]

# users: [id, nombre, strikes, fecha hasta la cual estara bloqueado]
users = [
    [1, "Ana", 0, None],
    [2, "Carlos", 2, None],
    [3, "Juan", 3, "2025-11-11"]
]

def show_menu():
    print("\n--- Sistema de Gestión de Biblioteca (PySGB) ---")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Listar libros disponibles")
    print("4. Listar libros prestados")
    print("5. Obtener usuarios penalizados")
    print("0. Salir")
    
def main():
    while True:
        show_menu()
        option = input("Seleccione una opción: ")
        
        try:
            if option == "1":
                title = input("Titulo: ")
                author = input("Autor: ")
                result = f.register_book(books, title, author)
                print(f"Se ha registrado el libro '{title}' con el ID {result}")

            elif option == "2":
                name = input("Nombre del usuario: ")
                if any(chr.isdigit() for chr in name):
                    raise ValueError("El nombre no puede contener números.")
                result = f.register_user(users, name)
                print(f"Se ha registrado el usuario '{name}' con el ID {result}")

            elif option == "3":
                available = f.list_books(books)
                if not available:
                    print("No hay libros disponibles.")
                for b in available:
                    print(f"{b[1]} - {b[2]}")

            elif option == "4":
                lent = f.list_books(books, status="prestado")
                if not lent:
                    print("No hay libros prestados.")
                for b in lent:
                    print(f"{b[1]} - Prestado a {b[4][1]}")
            elif option == "5":
                users_list = f.get_users(users)
                if not users_list:
                    print("No hay usuarios penalizados.")
                else:
                    penalizados = list(filter(lambda x: x[2] >= 3 and x[3] is not None, users_list))
                    
                    if not penalizados:
                        print("No hay usuarios penalizados.")
                    else:
                        print("Usuarios penalizados:")
                        for user in penalizados:
                            print(user)


            elif option == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()