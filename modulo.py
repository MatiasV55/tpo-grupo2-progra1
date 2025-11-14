import os
from datetime import datetime, timedelta
from mi_csv import writer, reader

DIAS_PRESTAMO = 7
BLOQUEO_DIAS = 3
STRIKES_MAXIMOS = 3

BOOKS_FILE = "books.csv"
CLIENTS_FILE = "clients.csv"


def initialize_files():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as f:
            csv_writer = writer(f)
            csv_writer.writerow([
                'id', 'titulo', 'autor', 'genero', 'anio_publicacion',
                'editorial', 'idioma', 'paginas', 'disponible',
                'cliente_prestamo', 'fecha_prestamo', 'fecha_limite'
            ])

    if not os.path.exists(CLIENTS_FILE):
        with open(CLIENTS_FILE, 'w', newline='', encoding='utf-8') as f:
            csv_writer = writer(f)
            csv_writer.writerow([
                'id', 'nombre', 'edad', 'genero', 'ciudad', 'pais',
                'prestamos', 'strikes', 'bloqueado_hasta'
            ])


def read_file(filename, page_size=None, page_number=0):
    rows = []
    if not os.path.exists(filename):
        return rows

    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader, None)

        if page_size is None:
            for row in csvreader:
                rows.append(row)
        else:
            start = page_number * page_size
            for _ in range(start):
                next(csvreader, None)
            for i, row in enumerate(csvreader):
                if i >= page_size:
                    break
                rows.append(row)
    return rows


def get_books():
    return read_file(BOOKS_FILE)


def get_clients():
    return read_file(CLIENTS_FILE)


def register_book(titulo, autor, genero="", anio_publicacion="", editorial="", idioma="", paginas=""):
    books = get_books()
    new_id = max([int(b[0]) for b in books], default=0) + 1
    new_book = [
        new_id, titulo, autor, genero, anio_publicacion,
        editorial, idioma, paginas, 'True', '', '', ''
    ]
    with open(BOOKS_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer(csvfile).writerow(new_book)
    return new_id


def register_client(nombre, edad="", genero="", ciudad="", pais=""):
    clients = get_clients()
    normalized_name = nombre.strip().lower()

    for client in clients:
        if client[1].strip().lower() == normalized_name:
            raise ValueError(f"El cliente con el nombre '{nombre}' ya existe.")

    new_id = max([int(u[0]) for u in clients], default=0) + 1
    new_client = [new_id, nombre.strip(), edad, genero, ciudad, pais, '0', '0', '']

    with open(CLIENTS_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer(csvfile).writerow(new_client)

    return new_id


def save_books(books):
    with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([
            'id', 'titulo', 'autor', 'genero', 'anio_publicacion',
            'editorial', 'idioma', 'paginas', 'disponible',
            'cliente_prestamo', 'fecha_prestamo', 'fecha_limite'
        ])
        csv_writer.writerows(books)


def save_clients(clients):
    with open(CLIENTS_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([
            'id', 'nombre', 'edad', 'genero', 'ciudad', 'pais',
            'prestamos', 'strikes', 'bloqueado_hasta'
        ])
        csv_writer.writerows(clients)


def search_client(nombre):
    clients = get_clients()
    for client in clients:
        if client[1].lower() == nombre.lower():
            return client
    return None


def list_books(status="disponible"):
    books = get_books()
    if status == "disponible":
        return [b for b in books if (b[8] == 'True' or b[8] == '') ]
    elif status == "prestado":
        return [b for b in books if b[8] == 'False']
    return books


def lend_book(book_id, client_name):
    books = get_books()
    clients = get_clients()

    client = next((c for c in clients if c[1].lower() == client_name.lower()), None)
    if not client:
        raise ValueError("Cliente no encontrado.")

    bloqueado_hasta = client[8]
    if bloqueado_hasta:
        bloqueado_dt = datetime.strptime(bloqueado_hasta, "%Y-%m-%d")
        if bloqueado_dt >= datetime.now():
            raise ValueError(f"El cliente está bloqueado hasta {bloqueado_hasta}.")

    book = next((b for b in books if str(b[0]) == str(book_id)), None)
    if not book:
        raise ValueError("No se encontró un libro con ese ID.")
    if book[8] == 'False':
        raise ValueError("El libro ya está prestado.")

    book[8] = 'False'
    book[9] = client_name
    fecha_prestamo = datetime.now()
    fecha_limite = fecha_prestamo + timedelta(days=DIAS_PRESTAMO)
    book[10] = fecha_prestamo.strftime("%Y-%m-%d")
    book[11] = fecha_limite.strftime("%Y-%m-%d")

    client[6] = str(int(client[6]) + 1)

    save_books(books)
    save_clients(clients)
    return True


def return_book(book_id):
    books = get_books()
    clients = get_clients()

    book = next((b for b in books if str(b[0]) == str(book_id)), None)
    if not book:
        raise ValueError("No se encontró un libro con ese ID.")
    if book[8] == 'True':
        raise ValueError("El libro ya está disponible.")

    client_name = book[9]
    fecha_limite = datetime.strptime(book[11], "%Y-%m-%d")
    fecha_actual = datetime.now()

    book[8] = 'True'
    book[9] = ''
    book[10] = ''
    book[11] = ''

    client = next((c for c in clients if c[1].lower() == client_name.lower()), None)
    if client:
        if fecha_actual > fecha_limite:
            strikes = int(client[7]) + 1
            client[7] = str(strikes)
            if strikes >= STRIKES_MAXIMOS:
                client[8] = (fecha_actual + timedelta(days=BLOQUEO_DIAS)).strftime("%Y-%m-%d")
                print(f"Cliente {client[1]} bloqueado hasta {client[8]} por acumulación de strikes.")
            else:
                print(f"Cliente {client[1]} recibió un strike ({strikes}/{STRIKES_MAXIMOS}).")

    save_books(books)
    save_clients(clients)
    return True


def listar_bloqueados():
    clients = get_clients()
    bloqueados = []
    cambios = False
    fecha_actual = datetime.now()

    for c in clients:
        bloqueado_hasta = c[8]
        if bloqueado_hasta:
            fecha_bloqueo = datetime.strptime(bloqueado_hasta, "%Y-%m-%d")
            if fecha_bloqueo >= fecha_actual:
                bloqueados.append({
                    "id": c[0],
                    "nombre": c[1],
                    "strikes": c[7],
                    "bloqueado_hasta": bloqueado_hasta
                })
            else:
                c[8] = ''
                c[7] = '0'
                cambios = True

    if cambios:
        save_clients(clients)

    return bloqueados
