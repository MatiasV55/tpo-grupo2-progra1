import csv

def register_book(title, author, books_file="books.csv"):
    """
    Registra un nuevo libro.

    Args:
        books (list): Lista de libros existentes.
        title (str): Título del libro.
        author (str): Autor del libro.
        books_file (str): Path al archivo para persistencia.

    Returns:
        int: ID asignado al nuevo libro.
    """
    books = get_books()
    new_id = max([int(b[0]) for b in books], default=0) + 1
    new_book = [new_id, title, author, True, '', '']
    with open(books_file, 'a', newline='\n', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new_book)
    csvfile.close()
    return new_id


def register_user(name, users_file="users.csv"):
    """
    Registra un nuevo usuario.

    Args:
        name (str): Nombre del usuario.        
        users_file (str): Ruta al archivo para persistencia.

    Returns:
        int: ID asignado al nuevo usuario.
    """
    users = get_users()
    new_id = max([int(u[0]) for u in users], default=0) + 1
    new_user = [new_id, name, 0, '']
    with open(users_file, 'a', newline='\n', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new_user)
    csvfile.close()
    return new_id
    
def read_file(filename):
    """
    Lee un archivo csv y retorna todas las filas a excepción de los encabezados.

    Args:
        filename (str): Ruta al archivo.

    Returns:
        list: Filas del archivo csv.
    """
    all_rows = []
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            all_rows.append(row)
    csvfile.close()
    return all_rows   
    
def get_books():
    """
    Lee un archivo csv y retorna los libros .

    Returns:
        list: Todos los libros registrados.
    """
    all_books = read_file('books.csv')
    return all_books

def get_users():
    """
    Lee un archivo csv y retorna los usuarios.

    Returns:
        list: Todos los usuarios registrados.
    """
    all_users = read_file('users.csv')
    return all_users

def list_books(status="disponible"):
    """
    Lista de libros disponibles o prestados.

    Args:
        status (str): Estado de los libros a listar ("disponible" o "prestado").

    Returns:
        list: Lista de libros disponibles o prestados.
    """
    books = get_books()
    if status == "disponible":
        return [b for b in books if b[3] == 'True']
    elif status == "prestado":
        return [b for b in books if b[3] == 'False']
    else:
        return []