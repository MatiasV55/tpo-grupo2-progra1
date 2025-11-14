def escapar_campo(campo):
    campo_str = str(campo)
    if ',' in campo_str or '"' in campo_str or '\n' in campo_str:
        campo_str = campo_str.replace('"', '""')
        return f'"{campo_str}"'
    return campo_str


def parsear_campo(campo):
    campo = campo.strip()
    if campo.startswith('"') and campo.endswith('"'):
        campo = campo[1:-1]
        campo = campo.replace('""', '"')
    return campo


def parsear_linea(linea):
    campos = []
    campo_actual = ""
    dentro_comillas = False
    
    i = 0
    while i < len(linea):
        caracter = linea[i]
        
        if caracter == '"':
            if dentro_comillas and i + 1 < len(linea) and linea[i + 1] == '"':
                campo_actual += '"'
                i += 2
                continue
            else:
                dentro_comillas = not dentro_comillas
        elif caracter == ',' and not dentro_comillas:
            campos.append(parsear_campo(campo_actual))
            campo_actual = ""
        else:
            campo_actual += caracter
        
        i += 1
    
    campos.append(parsear_campo(campo_actual))
    return campos


class writer:
    def __init__(self, archivo, delimiter=','):
        self.archivo = archivo
        self.delimiter = delimiter
    
    def writerow(self, fila):
        campos_escapados = [escapar_campo(campo) for campo in fila]
        linea = self.delimiter.join(campos_escapados) + '\n'
        self.archivo.write(linea)
    
    def writerows(self, filas):
        for fila in filas:
            self.writerow(fila)


class reader:
    def __init__(self, archivo, delimiter=','):
        self.archivo = archivo
        self.delimiter = delimiter
    
    def __iter__(self):
        return self
    
    def __next__(self):
        linea = self.archivo.readline()
        if not linea:
            raise StopIteration
        linea = linea.rstrip('\n\r')
        return parsear_linea(linea)
