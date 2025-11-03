import csv
import os
from datetime import datetime, timedelta

DIAS_PRESTAMO = 7
BLOQUEO_DIAS = 3
STRIKES_MAXIMOS = 3

BOOKS_FILE = "books.csv"
CLIENTS_FILE = "clients.csv"


def initialize_files():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'titulo', 'autor', 'disponible', 'cliente_prestamo',
                             'fecha_prestamo', 'fecha_limite'])
    if not os.path.exists(CLIENTS_FILE):
        with open(CLIENTS_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'nombre', 'prestamos', 'strikes', 'bloqueado_hasta'])


def read_file(filename):
    all_rows = []
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        for row in csvreader:
            all_rows.append(row)
    return all_rows


def get_books():
    return read_file(BOOKS_FILE)


def get_clients():
    return read_file(CLIENTS_FILE)


def register_book(title, author):
    books = get_books()
    new_id = max([int(b[0]) for b in books], default=0) + 1
    new_book = [new_id, title, author, 'True', '', '', '']
    with open(BOOKS_FILE, 'a', newline='\n', encoding='utf-8') as csvfile:
        csv.writer(csvfile).writerow(new_book)
    return new_id


def register_client(name):
    clients = get_clients()
    normalized_name = name.strip().lower()

    for client in clients:
        if client[1].strip().lower() == normalized_name:
            raise ValueError(f"El cliente con el nombre '{name}' ya existe.")

    new_id = max([int(u[0]) for u in clients], default=0) + 1
    new_client = [new_id, name.strip(), 0, 0, '']

    with open(CLIENTS_FILE, 'a', newline='\n', encoding='utf-8') as csvfile:
        csv.writer(csvfile).writerow(new_client)

    return new_id



def save_books(books):
    with open(BOOKS_FILE, 'w', newline='\n', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'titulo', 'autor', 'disponible', 'cliente_prestamo',
                         'fecha_prestamo', 'fecha_limite'])
        writer.writerows(books)


def save_clients(clients):
    with open(CLIENTS_FILE, 'w', newline='\n', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'nombre', 'prestamos', 'strikes', 'bloqueado_hasta'])
        writer.writerows(clients)


def search_client(name):
    clients = get_clients()
    for client in clients:
        if client[1].lower() == name.lower():
            return client
    return None


def list_books(status="disponible"):
    books = get_books()
    if status == "disponible":
        return [book for book in books if book[3] == 'True']
    elif status == "prestado":
        return [book for book in books if book[3] == 'False']
    return []


def lend_book(book_id, client_name):
    books = get_books()
    clients = get_clients()

    client = next((c for c in clients if c[1].lower() == client_name.lower()), None)
    if not client:
        raise ValueError("Cliente no encontrado.")

    if client[4]:
        bloqueado_hasta = datetime.strptime(client[4], "%Y-%m-%d")
        if bloqueado_hasta >= datetime.now():
            raise ValueError(f"El cliente está bloqueado hasta {client[4]}.")

    book = next((b for b in books if str(b[0]) == str(book_id)), None)
    if not book:
        raise ValueError("No se encontró un libro con ese ID.")
    if book[3] == 'False':
        raise ValueError("El libro ya está prestado.")

    book[3] = 'False'
    book[4] = client_name
    fecha_prestamo = datetime.now()
    fecha_limite = fecha_prestamo + timedelta(days=DIAS_PRESTAMO)
    book[5] = fecha_prestamo.strftime("%Y-%m-%d")
    book[6] = fecha_limite.strftime("%Y-%m-%d")

    client[2] = str(int(client[2]) + 1)

    save_books(books)
    save_clients(clients)
    return True


def return_book(book_id):
    books = get_books()
    clients = get_clients()

    book = next((b for b in books if str(b[0]) == str(book_id)), None)
    if not book:
        raise ValueError("No se encontró un libro con ese ID.")
    if book[3] == 'True':
        raise ValueError("El libro ya está disponible.")

    client_name = book[4]
    fecha_limite = datetime.strptime(book[6], "%Y-%m-%d")
    fecha_actual = datetime.now()

    book[3] = 'True'
    book[4] = ''
    book[5] = ''
    book[6] = ''

    client = next((c for c in clients if c[1].lower() == client_name.lower()), None)
    if client:
        if fecha_actual > fecha_limite:
            strikes = int(client[3]) + 1
            client[3] = str(strikes)
            if strikes >= STRIKES_MAXIMOS:
                client[4] = (fecha_actual + timedelta(days=BLOQUEO_DIAS)).strftime("%Y-%m-%d")
                print(f"Cliente {client[1]} bloqueado hasta {client[4]} por acumulación de strikes.")
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
        bloqueado_hasta = c[4]
        if bloqueado_hasta:
            fecha_bloqueo = datetime.strptime(bloqueado_hasta, "%Y-%m-%d")
            if fecha_bloqueo >= fecha_actual:
                bloqueados.append({
                    "id": c[0],
                    "nombre": c[1],
                    "strikes": c[3],
                    "bloqueado_hasta": bloqueado_hasta
                })
            else:
                c[4] = ''
                c[3] = '0'
                cambios = True

    if cambios:
        save_clients(clients)

    return bloqueados
