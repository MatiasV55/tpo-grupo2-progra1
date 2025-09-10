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

Los libros prestados tienen información del usuario adentro, ¡así que son listas dentro de listas!

### d. Manejo de cadenas (validación y normalización) ✅
En el main (líneas 26-27) verificamos que los nombres de usuarios no tengan números usando `isdigit()`.
¡No queremos usuarios que se llamen "Juan123"!

### e. Manejo de excepciones ✅
Todo el programa está envuelto en try/except (líneas 17-67 del main) para que no se rompa si alguien ingresa algo raro.
También tiramos un error específico si el nombre tiene números.

### f. Comprensión de listas ✅
Las usamos en varios lugares para hacer el código más corto:
- Para encontrar el ID más alto cuando agregamos libros/usuarios
- Para filtrar libros disponibles o prestados
- ¡4 ejemplos diferentes en total!

### g. Rebanadas/slices ✅
En las líneas 54 y 56 del módulo usamos `b[:5]` para tomar solo los primeros 5 datos de cada libro.
¡Es como cortar una torta pero con listas!

### h. Función lambda ✅
En la línea 49 del main usamos una función lambda para filtrar usuarios que tienen 3 o más multas.
Es como una función mini que escribimos al vuelo.

### i. Programa ejecutable ✅
¡El programa funciona! Tiene un menú bonito y maneja todo tipo de errores que el usuario pueda meter.

---

## 🎯 Resumen para el profe

| Requisito | ✅ | Dónde está |
|-----------|----|-----------| 
| a. Funciones modularizadas | ✅ | `modulo.py` y `main.py` |
| b. Parámetros por omisión | ✅ | Línea 46 de `modulo.py` |
| c. Listas y listas de listas | ✅ | Variables `books` y `users` |
| d. Manejo de cadenas | ✅ | Líneas 26-27 de `main.py` |
| e. Manejo de excepciones | ✅ | Todo el `main.py` |
| f. Comprensión de listas | ✅ | 4 ejemplos en `modulo.py` |
| g. Rebanadas/slices | ✅ | Líneas 54-56 de `modulo.py` |
| h. Función lambda | ✅ | Línea 49 de `main.py` |
| i. Programa ejecutable | ✅ | ¡Corre sin errores! |


