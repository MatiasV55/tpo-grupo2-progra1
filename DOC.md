# 📋 Estado del Proyecto - PySGB

## ✅ Funcionalidades Implementadas

### a. Funciones Modularizadas ✅
- **Criterio utilizado**: Separación clara entre lógica de negocio (`modulo.py`) y interfaz de usuario (`main.py`)
- **Implementadas**:
  - `register_book(title, author)` - Registra nuevos libros
  - `register_user(name)` - Registra nuevos usuarios
  - `list_available_books()` - Lista libros disponibles
  - `list_lent_books()` - Lista libros prestados

### b. Parámetros por Omisión ❌
- **Estado**: NO implementado
- **Falta**: Al menos una función que demuestre el uso de parámetros por omisión

### c. Listas y Listas de Listas ✅
- **Implementado**: 
  - Lista `books`: `[[id, nombre, autor, disponible, usuario, fecha_devolucion]]`
  - Lista `users`: `[id, nombre, strikes, fecha_bloqueo]`
  - Estructuras anidadas presentes (usuario dentro de libro prestado)

### d. Manejo de Cadenas ❌
- **Estado**: BÁSICO - Solo validación simple en try/except
- **Falta**: Validación y normalización específica de cadenas (mayúsculas, minúsculas, espacios, etc.)

### e. Manejo de Excepciones ⚠️
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

## ❌ Funcionalidades Faltantes Críticas

### 🔧 Funciones Pendientes de Implementar:

1. **Préstamo de Libros**
   - Función para prestar libros a usuarios
   - Validación de disponibilidad
   - Asignación de fecha de devolución

2. **Devolución de Libros**
   - Función para procesar devoluciones
   - Cálculo de multas por retraso
   - Sistema de strikes

3. **Validación de Cadenas**
   - Normalización de nombres (capitalización)
   - Validación de títulos y autores
   - Limpieza de espacios extra

4. **Manejo Avanzado de Excepciones**
   - Excepciones personalizadas
   - Validación de IDs
   - Control de datos inválidos

5. **Implementaciones Técnicas Faltantes**:
   - Parámetros por omisión
   - List comprehensions
   - Slicing
   - Funciones lambda

---

## 📊 Resumen de Completitud

| Requisito | Estado | Prioridad |
|-----------|--------|-----------|
| a. Funciones modularizadas | ✅ Completo | - |
| b. Parámetros por omisión | ❌ Falta | Media |
| c. Listas y listas de listas | ✅ Completo | - |
| d. Manejo de cadenas | ❌ Básico | Alta |
| e. Manejo de excepciones | ⚠️ Parcial | Alta |
| f. Comprensión de listas | ❌ Falta | Media |
| g. Rebanadas/slices | ❌ Falta | Media |
| h. Función lambda | ❌ Falta | Media |
| i. Programa ejecutable | ✅ Completo | - |

**Progreso General: 3/9 completo, 1/9 parcial, 5/9 pendiente**