import unittest
from tareas import agregar_tarea, listar_tareas, eliminar_tarea

class TestTareas(unittest.TestCase):

    def test_agregar_tarea(self):
        resultado = agregar_tarea("Estudiar")
        self.assertEqual(resultado, "Tarea agregada")

    def test_listar_tareas(self):
        agregar_tarea("Leer")
        lista = listar_tareas()
        self.assertIn("Leer", lista)

    def test_eliminar_tarea(self):
        agregar_tarea("Borrar")
        resultado = eliminar_tarea("Borrar")
        self.assertEqual(resultado, "Tarea eliminada")

if __name__ == "__main__":
    unittest.main()