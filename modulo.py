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
]

def register_book(title, author):
    """
    Registra un nuevo libro.

    Args:
        title (str): Título del libro.
        author (str): Autor del libro.

    Returns:
        int: ID asignado al nuevo libro.
    """
    new_id = max([b[0] for b in books], default=0) + 1
    books.append([new_id, title, author, True, None, None])
    return new_id


def register_user(name):
    """
    Registra un nuevo usuario.

    Args:
        name (str): Nombre del usuario.

    Returns:
        int: ID asignado al nuevo usuario.
    """
    new_id = max([u[0] for u in users], default=0) + 1
    users.append([new_id, name, 0, None])
    return new_id

def list_books(status="disponible"):
    """
    Lista de libros disponibles o prestados.

    Returns:
        list: Lista de libros disponibles o prestados.
    """
    if status == "disponible":
        return [b[:5] for b in books if b[3]]
    elif status == "prestado":
        return [b[:5] for b in books if not b[3]]
    else:
        return []