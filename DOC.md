# 📚 Documento de cambios en la última versión — PySGB

---

## Versión 0.3.0 — Sistema de préstamos avanzado, penalizaciones y seguridad

Esta versión introduce un sistema de control de préstamos, devoluciones y penalizaciones automáticas para los usuarios que devuelven los libros fuera de tiempo.  
Además, se integra el nuevo módulo `pass_logic` para el manejo de sesiones y registro de eventos.

---

### a. Nuevas constantes configurables

Se agregan parámetros globales en `modulo.py`:

```python
DIAS_PRESTAMO = 7 # Días estándar de préstamo
STRIKES_MAXIMOS = 3 # Strikes permitidos antes del bloqueo
BLOQUEO_DIAS = 3 # Días de bloqueo tras superar el límite
```

Esto permite ajustar fácilmente la política de préstamos y sanciones.

### b. Nuevos campos en los archivos CSV

books.csv ahora incluye:

id, titulo, autor, disponible, cliente_prestamo, fecha_prestamo, fecha_limite

clients.csv ahora incluye:

id, nombre, prestamos, strikes, bloqueado_hasta

Estos campos permiten rastrear préstamos activos, fechas límite y bloqueos de usuarios.

### c. Validación al registrar clientes

Antes de registrar un nuevo cliente, el sistema valida si ya existe uno con el mismo nombre (ignorando mayúsculas y espacios).
Si existe, lanza una excepción:

```python
raise ValueError(f"El cliente '{name}' ya está registrado.")
```

### d. Sistema de préstamos y devoluciones con penalización

    lend_book() → Presta un libro solo si el usuario no está bloqueado.

    return_book() → Verifica si el libro fue devuelto fuera de plazo:

        Si se pasa la fecha límite, el usuario recibe un strike.

        Al llegar a 3 strikes, el usuario es bloqueado automáticamente durante BLOQUEO_DIAS.

### e. Listado de usuarios bloqueados

Nueva función: listar_bloqueados()

    Muestra todos los usuarios actualmente bloqueados.

    Elimina automáticamente bloqueos expirados (libera usuarios cuando pasa la fecha).

    Guarda los cambios en clients.csv sin intervención manual.

### f. Integración del módulo de seguridad pass_logic

Se incorpora módulo adicional para el manejo de autenticación y registro de eventos del sistema.

Funcionalidades agregadas:

    login() → Controla el acceso de los administradores o bibliotecarios al sistema.

    log_event() → Registra los eventos importantes (préstamos, devoluciones, bloqueos) en un archivo de log.

    COLORES → Define paletas de colores para mejorar la visualización del menú y mensajes en consola.

    limpiar_pantalla() → Permite reiniciar visualmente la consola entre operaciones, manteniendo el entorno ordenado.

Estas integraciones aportan una capa de seguridad, trazabilidad y usabilidad al sistema PySGB.

### g. Resumen de nuevas funciones en la versión 0.3.0

| Función                           | Descripción                                   |
| --------------------------------- | --------------------------------------------- |
| `initialize_files()`              | Crea los CSV con encabezados si no existen.   |
| `register_client()`               | Valida duplicados y registra nuevos usuarios. |
| `lend_book()`                     | Realiza un préstamo y asigna fecha límite.    |
| `return_book()`                   | Marca devolución, aplica strikes y bloqueos.  |
| `listar_bloqueados()`             | Lista y actualiza usuarios bloqueados.        |
| `login()` (pass_logic)            | Controla acceso al sistema.                   |
| `log_event()` (pass_logic)        | Registra eventos importantes en log.          |
| `COLORES` (pass_logic)            | Maneja estilos de color en consola.           |
| `limpiar_pantalla()` (pass_logic) | Limpia la pantalla entre operaciones.         |
