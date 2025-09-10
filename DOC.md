# 📚 Documento de indicaciones

### a. Funciones en módulos separados ✅
Dividimos el código en dos archivos:
- `modulo.py` - Todas las funciones del sistema
- `main.py` - El menú y la interacción con el usuario

**Funciones que hicimos:**
- Registrar libros nuevos
- Registrar usuarios nuevos  
- Mostrar libros disponibles
- Mostrar libros prestados

### b. Parámetros por omisión ✅
En la función `list_books()` (línea 46 del módulo) usamos un parámetro que tiene un valor por defecto: `status="disponible"`. 
Si no le pasamos nada, busca libros disponibles automáticamente.

### c. Listas y listas de listas ✅
Usamos dos listas principales:
- `books` - Lista de libros (cada libro es otra lista con sus datos)
- `users` - Lista de usuarios (cada usuario también es una lista)

Los libros prestados tienen información del usuario adentro por lo que también respeta el formato de listas de listas.

### d. Manejo de cadenas (validación y normalización) ✅
En el main (líneas 26-27) verificamos que los nombres de usuarios no tengan números usando `isdigit()` y lanzamos una excepción de tipo ValueError

### e. Manejo de excepciones ✅
Todo el programa está envuelto en try/except (líneas 17-67 del main) para que no se rompa si alguien ingresa algo raro.
También tiramos un error específico si el nombre tiene números.

### f. Comprensión de listas ✅
Las usamos en varios lugares para hacer el código más corto:
- Para encontrar el ID más alto y sumarle 1 cuando agregamos libros/usuarios
- Para filtrar libros disponibles o prestados

### g. Rebanadas/slices ✅
En las líneas 54 y 56 del módulo usamos `b[:5]` para tomar solo los primeros 5 datos de cada libro.

### h. Función lambda ✅
En la línea 49 del main usamos una función lambda para filtrar usuarios que tienen 3 o más strikes.
