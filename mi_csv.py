"""
Módulo CSV hecho por nosotros mismos.
Implementación básica para leer y escribir archivos CSV sin usar la librería csv de Python.
"""


def escapar_campo(campo):
    """
    Si un campo tiene comas, comillas o saltos de línea, lo envolvemos en comillas.
    También escapamos las comillas dobles duplicándolas.
    """
    campo_str = str(campo)
    
    # Si tiene caracteres especiales, lo ponemos entre comillas
    if ',' in campo_str or '"' in campo_str or '\n' in campo_str:
        # Duplicamos las comillas para escaparlas
        campo_str = campo_str.replace('"', '""')
        return f'"{campo_str}"'
    
    return campo_str


def parsear_campo(campo):
    """
    Quita las comillas de un campo y restaura las comillas escapadas.
    """
    campo = campo.strip()
    
    # Si está entre comillas, las quitamos
    if campo.startswith('"') and campo.endswith('"'):
        campo = campo[1:-1]  # Quitamos las comillas de los extremos
        campo = campo.replace('""', '"')  # Restauramos comillas escapadas
    
    return campo


def parsear_linea(linea):
    """
    Separa una línea de CSV en campos, manejando comas y comillas correctamente.
    """
    campos = []
    campo_actual = ""
    dentro_comillas = False
    
    i = 0
    while i < len(linea):
        caracter = linea[i]
        
        if caracter == '"':
            # Si encontramos una comilla
            if dentro_comillas and i + 1 < len(linea) and linea[i + 1] == '"':
                # Es una comilla escapada ""
                campo_actual += '"'
                i += 2  # Avanzamos 2 posiciones
                continue
            else:
                # Es el inicio o fin de un campo entre comillas
                dentro_comillas = not dentro_comillas
        elif caracter == ',' and not dentro_comillas:
            # Es un separador de campo (solo si no estamos dentro de comillas)
            campos.append(parsear_campo(campo_actual))
            campo_actual = ""
        else:
            # Es un carácter normal, lo agregamos al campo actual
            campo_actual += caracter
        
        i += 1
    
    # Agregamos el último campo (después de la última coma)
    campos.append(parsear_campo(campo_actual))
    
    return campos


class writer:
    """
    Clase para escribir archivos CSV.
    Similar a csv.writer pero hecho por nosotros.
    """
    
    def __init__(self, archivo, delimiter=','):
        """
        Inicializa el writer con un archivo abierto.
        delimiter es el separador (por defecto coma).
        """
        self.archivo = archivo
        self.delimiter = delimiter
    
    def writerow(self, fila):
        """
        Escribe una fila en el archivo CSV.
        fila es una lista o tupla con los valores.
        """
        # Escapamos cada campo por si tiene comas o comillas
        campos_escapados = [escapar_campo(campo) for campo in fila]
        # Unimos con el delimitador y agregamos salto de línea
        linea = self.delimiter.join(campos_escapados) + '\n'
        self.archivo.write(linea)
    
    def writerows(self, filas):
        """
        Escribe varias filas en el archivo CSV.
        filas es una lista de listas/tuplas.
        """
        for fila in filas:
            self.writerow(fila)


class reader:
    """
    Clase para leer archivos CSV.
    Similar a csv.reader pero hecho por nosotros.
    """
    
    def __init__(self, archivo, delimiter=','):
        """
        Inicializa el reader con un archivo abierto.
        delimiter es el separador (por defecto coma).
        """
        self.archivo = archivo
        self.delimiter = delimiter
    
    def __iter__(self):
        """
        Hace que el reader sea iterable (para usar en for loops).
        """
        return self
    
    def __next__(self):
        """
        Lee la siguiente línea del CSV y la devuelve como lista de campos.
        Si no hay más líneas, lanza StopIteration.
        """
        linea = self.archivo.readline()
        
        # Si no hay más líneas, terminamos
        if not linea:
            raise StopIteration
        
        # Quitamos el salto de línea del final
        linea = linea.rstrip('\n\r')
        
        # Parseamos la línea y devolvemos los campos
        return parsear_linea(linea)
