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

if __name__ == '__main__':
   unittest.main()

