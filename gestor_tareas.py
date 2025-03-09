class Tarea:
   def __init__(self, id, titulo, descripcion ="", 
      completada = False, prioridad="normal"):

      self.id = id
      self.titulo = titulo
      self.descripcion = descripcion
      self.completada = completada

      #Definir la prioridades validas para validación

      prioridades_validas = ["baja", "normal", "alta"]

      #Verificamos que la prioridad proporcionada es valida
      if prioridad not in prioridades_validas:
         raise ValueError(f"Prioridad no valida. Debe ser un de: {prioridades_validas}")

      # Asignamos la prioridad si pasó la validación
      self.prioridad = prioridad

   def __eq__(self, other):
      if not isinstance(other, Tarea):
         return False
      return self.id == other.id


# La clase GestorTareas maneja una colección de objetos Tarea
class GestorTareas:
   def __init__(self):
      #Lista para almacenar mis tareas
      self.tareas = []

      #Contador para asignar IDs unicos a las tareas
      self.contador_id = 0

      # * Metodo añadir tarea
   def agregar_tarea(self, titulo, descripcion="", prioridad="normal"):
      #Incrementamos el contador para obtener un nuevo ID unico
      self.contador_id += 1

      #Creamos la nueva tarea con los parametros proporcionados
      nueva_tarea = Tarea(self.contador_id, titulo, descripcion, False, prioridad)

      #Añadimos la tareaa a nuestra lista
      self.tareas.append(nueva_tarea)

      #Retornamos la tarea creada para que pueda ser utilizada
      return nueva_tarea