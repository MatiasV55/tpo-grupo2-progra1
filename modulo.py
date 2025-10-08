def register_book(books, title, author):
    """
    Registra un nuevo libro.

    Args:
        books (list): Lista de libros existentes.
        title (str): Título del libro.
        author (str): Autor del libro.

    Returns:
        int: ID asignado al nuevo libro.
    """
    new_id = max([b[0] for b in books], default=0) + 1
    books.append([new_id, title, author, True, None, None])
    return new_id


def register_user(users, name):
    """
    Registra un nuevo usuario.

    Args:
        users (list): Lista de usuarios existentes.
        name (str): Nombre del usuario.

    Returns:
        int: ID asignado al nuevo usuario.
    """
    new_id = max([u[0] for u in users], default=0) + 1
    users.append([new_id, name, 0, None])
    return new_id

def list_books(books, status="disponible"):
    """
    Lista de libros disponibles o prestados.

    Args:
        books (list): Lista de libros existentes.
        status (str): Estado de los libros a listar ("disponible" o "prestado").

    Returns:
        list: Lista de libros disponibles o prestados.
    """
    if status == "disponible":
        return [b[:5] for b in books if b[3]]
    elif status == "prestado":
        return [b[:5] for b in books if not b[3]]
    else:
        return []
    
def get_users(users):
    """
    Obtiene la lista de usuarios.

    Args:
        users (list): Lista de usuarios existentes.

    Returns:
        list: Lista de usuarios.
    """
    return users