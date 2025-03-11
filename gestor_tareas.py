class Tarea:
   def __init__(self, id, titulo, descripcion ="", completada = False, prioridad="normal"):

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

      #Creamos la nueva tarea con los parametros proporcionados llamando la clase Tarea
      nueva_tarea = Tarea(self.contador_id, titulo, descripcion, False, prioridad)

      #Añadimos la tareaa a nuestra lista
      self.tareas.append(nueva_tarea)

      #Retornamos la tarea creada para que pueda ser utilizada
      return nueva_tarea
   
   # * Metodo borrar tarea
   def borrar_tarea(self, id_tarea):

      # Buscamos la tarea por su ID
      for tarea in self.tareas:

         if tarea.id == id_tarea:

            # Si la encontramos, la eliminamos de la lista
            self.tareas.remove(tarea)
            return "La tarea ha sido borrada con éxito"
      
      # Si no encontramos la tarea con ese ID
      return "No se encontró ninguna tarea con ese ID"
   
   # * Metodo buscar tarea por ID
   def buscar_tarea_porID(self, id_tarea):
      #Recorremos el array que contiene las tareas
      for tarea in self.tareas:

         if tarea.id == id_tarea:

            #Si encontramos la tarea, nos muestra el titulo y su ID
            return f"Busqueda exitosa. La tarea es : '{tarea.titulo}', con el ID: {tarea.id}"
      
      return "ERROR: No se encontró ninguna tarea con ese ID"
      
   # * Metodo marcar tarea completada
   def marcar_tarea_completada(self, id_tarea):
      #Recorremos el array que contiene las tareas
      for tarea in self.tareas:

         if tarea.id == id_tarea:
            # Si encontramos la tarea, la marcamos como completada
            tarea.completada = True
            return f"La tarea con ID {id_tarea} ha sido marcada como completada."
    
      # Si no se encuentra la tarea
      return "ERROR: No se encontró ninguna tarea con ese ID"

   # * Método para listar tareas (todas o solo pendientes)
   def listar_tareas(self, TareasPorCompletar=False):
      if TareasPorCompletar:
         # Filtrar solo tareas pendientes
         tareas_filtradas = [
               f"ID: {tarea.id}, Título: {tarea.titulo}, ¿Completada?: {tarea.completada}"
               for tarea in self.tareas if not tarea.completada
         ]
      else:
         # Listar todas las tareas
         tareas_filtradas = [
               f"ID: {tarea.id}, Título: {tarea.titulo}, ¿Completada?: {tarea.completada}"
               for tarea in self.tareas
         ]
      
      if tareas_filtradas:
         return "\n".join(tareas_filtradas)
      return "No hay tareas registradas." if not TareasPorCompletar else "No hay tareas pendientes."

   # * Metodo para filtrar las tareas por prioridad
   def filtrar_tarea_prioridad(self, prioridad):

      if prioridad not in ["baja", "normal", "alta"]:
          return "ERROR: Prioridad no válida. Use 'baja', 'normal' o 'alta'."
      
      tareas_filtradas = [
         f"ID: {tarea.id}, Título: {tarea.titulo}, ¿Completada?: {tarea.completada}, Prioridad: {tarea.prioridad}"
         for tarea in self.tareas if tarea.prioridad == prioridad
      ]

      if tareas_filtradas:
         return "\n".join(tareas_filtradas)
      
      return f"No hay tareas con prioridad '{prioridad}'."
