# TODO: main_user.py Gestion de usuarios, login, el usuario puede solicitar prestamo, cambia pass
# TODO: Busqueda de libro por nombre, logs. 

import modulo as f

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
                result = f.register_book(title, author)
                print(f"Se ha registrado el libro '{title}' con el ID {result}")

            elif option == "2":
                name = input("Nombre del usuario: ")
                if any(char.isdigit() for char in name):
                    raise ValueError("El nombre no puede contener números.")
                result = f.register_user(name)
                print(f"Se ha registrado el usuario '{name}' con el ID {result}")

            elif option == "3":
                available = f.list_books()
                if not available:
                    print("No hay libros disponibles.")
                for book in available:
                    print(f"{book[1]} - {book[2]}")

            elif option == "4":
                lent = f.list_books(status="prestado")
                if not lent:
                    print("No hay libros prestados.")
                for book in lent:
                    print(book)
            elif option == "5":
                users_list = f.get_users()
                if not users_list:
                    print("No hay usuarios penalizados.")
                else:
                    penalizados = list(filter(
                        lambda user: int(user[2]) >= 3 and user[3] is not None,
                        users_list))
                    
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