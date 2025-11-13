"""
Módulo CSV personalizado implementado con Python nativo.
Reemplaza la funcionalidad básica del módulo csv estándar.
"""


def _escapar_campo(campo):
    """
    Escapa un campo si contiene comas, comillas o saltos de línea.
    
    Args:
        campo: El valor del campo a escapar (se convierte a string)
    
    Returns:
        str: El campo escapado con comillas si es necesario
    """
    campo_str = str(campo)
    
    # Si el campo contiene comas, comillas o saltos de línea, lo envolvemos en comillas
    if ',' in campo_str or '"' in campo_str or '\n' in campo_str:
        # Escapamos las comillas dobles duplicándolas
        campo_str = campo_str.replace('"', '""')
        return f'"{campo_str}"'
    
    return campo_str


def _parsear_campo(campo):
    """
    Parsea un campo del CSV, manejando comillas y escapes.
    
    Args:
        campo: El campo como string (ya sin espacios iniciales/finales)
    
    Returns:
        str: El campo parseado sin comillas de escape
    """
    campo = campo.strip()
    
    # Si está entre comillas
    if campo.startswith('"') and campo.endswith('"'):
        campo = campo[1:-1]  # Quitamos las comillas externas
        campo = campo.replace('""', '"')  # Restauramos comillas escapadas
    
    return campo


def _parsear_linea(linea):
    """
    Parsea una línea de CSV separada por comas.
    
    Args:
        linea: String con una línea completa del CSV
    
    Returns:
        list: Lista de campos parseados
    """
    campos = []
    campo_actual = ""
    dentro_comillas = False
    
    i = 0
    while i < len(linea):
        caracter = linea[i]
        
        if caracter == '"':
            if dentro_comillas and i + 1 < len(linea) and linea[i + 1] == '"':
                # Comilla escapada ""
                campo_actual += '"'
                i += 2
                continue
            else:
                # Inicio o fin de comillas
                dentro_comillas = not dentro_comillas
        elif caracter == ',' and not dentro_comillas:
            # Separador de campo
            campos.append(_parsear_campo(campo_actual))
            campo_actual = ""
        else:
            campo_actual += caracter
        
        i += 1
    
    # Agregar el último campo
    campos.append(_parsear_campo(campo_actual))
    
    return campos


class writer:
    """
    Clase para escribir archivos CSV (similar a csv.writer).
    """
    
    def __init__(self, archivo, delimiter=','):
        """
        Inicializa el writer.
        
        Args:
            archivo: Archivo abierto en modo escritura
            delimiter: Delimitador (por defecto coma)
        """
        self.archivo = archivo
        self.delimiter = delimiter
    
    def writerow(self, fila):
        """
        Escribe una fila en el archivo CSV.
        
        Args:
            fila: Lista o tupla con los valores de la fila
        """
        campos = [_escapar_campo(campo) for campo in fila]
        linea = self.delimiter.join(campos) + '\n'
        self.archivo.write(linea)
    
    def writerows(self, filas):
        """
        Escribe múltiples filas en el archivo CSV.
        
        Args:
            filas: Lista de listas/tuplas, cada una representa una fila
        """
        for fila in filas:
            self.writerow(fila)


class reader:
    """
    Clase para leer archivos CSV (similar a csv.reader).
    """
    
    def __init__(self, archivo, delimiter=','):
        """
        Inicializa el reader.
        
        Args:
            archivo: Archivo abierto en modo lectura
            delimiter: Delimitador (por defecto coma)
        """
        self.archivo = archivo
        self.delimiter = delimiter
    
    def __iter__(self):
        """Hace que el reader sea iterable."""
        return self
    
    def __next__(self):
        """
        Lee la siguiente línea del CSV.
        
        Returns:
            list: Lista de campos parseados
        
        Raises:
            StopIteration: Cuando no hay más líneas
        """
        linea = self.archivo.readline()
        
        if not linea:
            raise StopIteration
        
        # Quitamos el salto de línea final
        linea = linea.rstrip('\n\r')
        
        return _parsear_linea(linea)

