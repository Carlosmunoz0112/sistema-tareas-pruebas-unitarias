tareas = []

def agregar_tarea(nombre):
    tareas.append(nombre)
    return "Tarea agregada"

def listar_tareas():
    return tareas

def eliminar_tarea(nombre):
    if nombre in tareas:
        tareas.remove(nombre)
        return "Tarea eliminada"
    return "Tarea no encontrada"