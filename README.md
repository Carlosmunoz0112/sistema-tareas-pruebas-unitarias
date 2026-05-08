# Sistema de gestión de tareas en Python

## Descripción del proyecto

Este proyecto corresponde a un sistema básico de gestión de tareas desarrollado en Python.  
El sistema permite realizar operaciones simples como agregar tareas, listar tareas registradas y eliminar tareas existentes.

El objetivo principal del proyecto es aplicar pruebas unitarias para validar el correcto funcionamiento de las funciones principales del sistema.

## Sistema evaluado

Sistema de gestión de tareas en Python.

## Funcionalidades del sistema

El sistema cuenta con tres funcionalidades principales:

- Agregar una tarea.
- Listar las tareas registradas.
- Eliminar una tarea existente.

## Archivos del proyecto

El repositorio contiene los siguientes archivos:

- `tareas.py`: archivo principal donde se encuentra la lógica del sistema.
- `test_tareas.py`: archivo donde se encuentran las pruebas unitarias.
- `README.md`: archivo de documentación del proyecto.

## Código principal

El archivo `tareas.py` contiene las funciones principales del sistema:

- `agregar_tarea(nombre)`: agrega una tarea a la lista.
- `listar_tareas()`: muestra las tareas registradas.
- `eliminar_tarea(nombre)`: elimina una tarea existente de la lista.

## Tipo de prueba aplicada

El tipo de prueba seleccionado fue la prueba unitaria.

Se eligió este tipo de prueba porque permite validar funciones específicas del sistema de manera individual. En este caso, se probaron las funciones encargadas de agregar, listar y eliminar tareas.

## Herramienta utilizada para las pruebas

Para ejecutar las pruebas se utilizó la herramienta `unittest`, incluida por defecto en Python.

## Casos de prueba

Se diseñaron tres casos de prueba:

| Código | Caso de prueba | Función evaluada | Resultado esperado |
|---|---|---|---|
| CP-01 | Agregar tarea | `agregar_tarea()` | El sistema retorna "Tarea agregada" |
| CP-02 | Listar tareas | `listar_tareas()` | La lista contiene la tarea registrada |
| CP-03 | Eliminar tarea | `eliminar_tarea()` | El sistema retorna "Tarea eliminada" |

## Ejecución de las pruebas

Para ejecutar las pruebas unitarias se debe abrir la terminal en la carpeta del proyecto y escribir el siguiente comando:

```bash
py -m unittest -v
```

## Resultado esperado de la ejecución

Al ejecutar las pruebas, el resultado esperado es que las tres pruebas aparezcan aprobadas con estado `ok`.

Ejemplo del resultado esperado:

```text
test_agregar_tarea ... ok
test_eliminar_tarea ... ok
test_listar_tareas ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## Resultado obtenido

Durante la ejecución del proyecto, las tres pruebas unitarias fueron aprobadas correctamente.  
Esto demuestra que las funciones principales del sistema cumplen con los resultados esperados.

## Análisis general

El sistema cumple con las funcionalidades básicas evaluadas. Sin embargo, se identifican algunas oportunidades de mejora:

- Validar que no se agreguen tareas vacías.
- Evitar tareas duplicadas.
- Guardar las tareas en una base de datos o archivo.
- Crear una interfaz gráfica o web.
- Agregar más casos de prueba, incluyendo casos negativos.

## Conclusión

El proyecto permitió aplicar pruebas unitarias a un sistema básico desarrollado en Python.  
A través de la herramienta `unittest`, se comprobó el funcionamiento de las funciones principales del sistema: agregar, listar y eliminar tareas.

Los resultados obtenidos fueron satisfactorios, ya que las tres pruebas fueron aprobadas correctamente. Esto demuestra la importancia de realizar pruebas de software antes de una implementación final.
