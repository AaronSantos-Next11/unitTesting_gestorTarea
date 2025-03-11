#Importamos el modulo para realizar pruebas unitrias
import unittest

#
from gestor_tareas import GestorTareas, Tarea

#Definir la clase de prueba GestorTareas
class TestGestorTareas(unittest.TestCase):
   def setUp(self):

      #Creamos una nueva instancia
      self.gestor = GestorTareas()

      #Agregar 3 tareas de ejemplo con diferentes prioridades
      self.tarea1 = self.gestor.agregar_tarea("Realizar tarea", "Elaborar tarea de Testing", "alta")

      self.tarea2 = self.gestor.agregar_tarea("Estudiar React", "Ver el video de Midudev y otros recursos", "normal")

      self.tarea3 = self.gestor.agregar_tarea("Avanzar proyecto de integradora", "Avanzar el proyecto de desarrollo", "baja")

   def test_agregar_tarea(self):
      # Agregamos una nueva tarea con valores de prueba
      tarea = self.gestor.agregar_tarea("Prueba", "Descripcion de prueba")

      #Verificamos que la tarea se haya añadido a la lista de tareas
      self.assertIn(tarea, self.gestor.tareas)


      #Verificamos que los atributos de la tarea sean los correctos
      self.assertEqual(tarea.titulo, "Prueba")
      self.assertEqual(tarea.descripcion, "Descripcion de prueba")
      self.assertEqual(tarea.prioridad, "normal") # Valor por defecto
      self.assertFalse(tarea.completada) #Por defecto que no está completada

      #Verficamos que el ID sea el siguiente en la secuencia (4)
      self.assertEqual(tarea.id, 4)

   def test_borrar_tarea(self):
      # Verificar borrado exitoso de una tarea existente
      resultado = self.gestor.borrar_tarea(2)
      self.assertEqual(resultado, "La tarea ha sido borrada con éxito")
      # Verificar que la tarea ya no existe en la lista
      for tarea in self.gestor.tareas:
         self.assertNotEqual(tarea.id, 2)
      
      # Verificar comportamiento al intentar borrar una tarea inexistente
      resultado = self.gestor.borrar_tarea(999)
      self.assertEqual(resultado, "No se encontró ninguna tarea con ese ID")

   def test_buscar_tarea_porID(self):
      # Verificar búsqueda de una tarea existente
      resultado = self.gestor.buscar_tarea_porID(1)
      self.assertEqual(resultado, f"Busqueda exitosa. La tarea es : '{self.tarea1.titulo}', con el ID: {self.tarea1.id}")
      
      # Verificar búsqueda de una tarea inexistente
      resultado = self.gestor.buscar_tarea_porID(999)
      self.assertEqual(resultado, "ERROR: No se encontró ninguna tarea con ese ID")
      
   def test_marcar_tarea_completada(self):
      # Verificar marcar como completada una tarea existente
      resultado = self.gestor.marcar_tarea_completada(1)
      self.assertEqual(resultado, f"La tarea con ID 1 ha sido marcada como completada.")
      # Verificar que la tarea está realmente marcada como completada
      for tarea in self.gestor.tareas:
         if tarea.id == 1:
            self.assertTrue(tarea.completada)
      
      # Verificar comportamiento al intentar marcar como completada una tarea inexistente
      resultado = self.gestor.marcar_tarea_completada(999)
      self.assertEqual(resultado, "ERROR: No se encontró ninguna tarea con ese ID")

   def test_listar_tareas(self):
      # Verificar listado de todas las tareas
      resultado = self.gestor.listar_tareas()
      # Verificar que el resultado contiene las tres tareas
      self.assertIn("ID: 1", resultado)
      self.assertIn("ID: 2", resultado)
      self.assertIn("ID: 3", resultado)
      
      # Marcar una tarea como completada
      self.gestor.marcar_tarea_completada(1)
      
      # Verificar listado filtrado por tareas pendientes
      resultado = self.gestor.listar_tareas(TareasPorCompletar=True)
      # Verificar que el resultado contiene solo las tareas pendientes
      self.assertNotIn("ID: 1", resultado)
      self.assertIn("ID: 2", resultado)
      self.assertIn("ID: 3", resultado)

   def test_filtrar_tarea_prioridad(self):
      # Verificar filtrado de tareas por prioridad alta
      resultado = self.gestor.filtrar_tarea_prioridad("alta")
      self.assertIn("ID: 1", resultado)
      self.assertNotIn("ID: 2", resultado)
      self.assertNotIn("ID: 3", resultado)
      
      # Verificar filtrado de tareas por prioridad normal
      resultado = self.gestor.filtrar_tarea_prioridad("normal")
      self.assertNotIn("ID: 1", resultado)
      self.assertIn("ID: 2", resultado)
      self.assertNotIn("ID: 3", resultado)
      
      # Verificar filtrado de tareas por prioridad baja
      resultado = self.gestor.filtrar_tarea_prioridad("baja")
      self.assertNotIn("ID: 1", resultado)
      self.assertNotIn("ID: 2", resultado)
      self.assertIn("ID: 3", resultado)
      
      # Verificar filtrado con prioridad inexistente
      resultado = self.gestor.filtrar_tarea_prioridad("media")
      self.assertEqual(resultado, "ERROR: Prioridad no válida. Use 'baja', 'normal' o 'alta'.")

   def test_validacion_prioridades_invalidas(self):
      # Verificar que se lanza una excepción al usar una prioridad no válida
      with self.assertRaises(ValueError):
         self.gestor.agregar_tarea("Tarea inválida", "Descripción", "urgente")

   def test_comparacion_tareas(self):
      # Crear dos tareas con el mismo ID pero diferentes atributos
      tarea_original = Tarea(100, "Tarea A", "Descripción A", False, "alta")
      tarea_mismoID = Tarea(100, "Tarea B", "Descripción B", True, "baja")
      
      # Verificar que dos tareas con el mismo ID son consideradas iguales
      self.assertEqual(tarea_original, tarea_mismoID)
      
      # Crear una tarea con ID diferente
      tarea_diferenteID = Tarea(101, "Tarea A", "Descripción A", False, "alta")
      
      # Verificar que dos tareas con diferentes ID son consideradas diferentes
      self.assertNotEqual(tarea_original, tarea_diferenteID)
      
      # Verificar que una tarea no es igual a un objeto de otro tipo
      self.assertNotEqual(tarea_original, "Esto no es una tarea")


if __name__ == '__main__':
   unittest.main()