# 📋 Estado del Proyecto - PySGB

## ✅ Funcionalidades Implementadas

### a. Funciones Modularizadas ✅
- **Criterio utilizado**: Separación clara entre lógica de negocio (`modulo.py`) y interfaz de usuario (`main.py`)
- **Implementadas**:
  - `register_book(title, author)` - Registra nuevos libros
  - `register_user(name)` - Registra nuevos usuarios
  - `list_available_books()` - Lista libros disponibles
  - `list_lent_books()` - Lista libros prestados

### b. Parámetros por Omisión ✅
- **Estado**: NO implementado
- **Falta**: Al menos una función que demuestre el uso de parámetros por omisión

### c. Listas y Listas de Listas ✅
- **Implementado**: 
  - Lista `books`: `[[id, nombre, autor, disponible, usuario, fecha_devolucion]]`
  - Lista `users`: `[id, nombre, strikes, fecha_bloqueo]`
  - Estructuras anidadas presentes (usuario dentro de libro prestado)

### d. Manejo de Cadenas ✅
- **Estado**: BÁSICO - Solo validación simple en try/except
- **Falta**: Validación y normalización específica de cadenas (mayúsculas, minúsculas, espacios, etc.)

### e. Manejo de Excepciones ✅
- **Estado**: PARCIAL
- **Implementado**: Try/catch básico en `main.py`
- **Falta**: Manejo específico de diferentes tipos de excepciones en funciones del módulo

### f. Comprensión de Listas ❌
- **Estado**: NO implementado
- **Falta**: Al menos un caso que demuestre list comprehension

### g. Rebanadas/Slices ❌
- **Estado**: NO implementado
- **Falta**: Mínimo un caso usando slicing de listas

### h. Función Lambda ❌
- **Estado**: NO implementado
- **Falta**: Mínimo un caso usando función lambda

### i. Programa Ejecutable ✅
- **Estado**: IMPLEMENTADO
- **Funciona**: Menú interactivo, ingreso de datos, reportes básicos

---