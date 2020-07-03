class Classroom:
 
    #MÉTODOS
    def entrega(self):
        print("al entregar una tarea le llega la notificacion al profesor")
    
    def modificar(self):
        print("se puede modificar dentro de la aplicacion algun trabajo o archivo")
    
    def fecha(self):
        print("s tin una fecha limite del mismo paraz evitar algun daño de calificaciones")

    def tareas(self):
        print("se registra la entrega de tareas pedidas")
    
    def capacidad(self):
        print("capacidad de gb ya sea en archivos,videos etc")

#ATRIBUTOS
    apartados = ""
    diseño = ""
    modulos = ""
    profesores = ""
    archivos = ""


Aplicacion_Classroom = Classroom()

#METODOS

Aplicacion_Classroom.entrega()
Aplicacion_Classroom.modificar()
Aplicacion_Classroom.fecha()
Aplicacion_Classroom.tareas()
Aplicacion_Classroom.capacidad()

#ATRIBUTOS

Aplicacion_Classroom.apartados = "difrentes apartados de clases como lo es bade de datos,ingles,etc"
Aplicacion_Classroom.diseño = "classroom cada apartado maneja diferents colores para evitar confundirse"
Aplicacion_Classroom.modulo = "modulo de diferes profesores con diferentes apartados"
Aplicacion_Classroom.profesores = "profesores que manejan su modulo para subir y calificar las taras"
Aplicacion_Classroom.almacenamiento = "google drive de tu propio correo de utec"

print(Aplicacion_Classroom.apartados)
print(Aplicacion_Classroom.diseño)
print(Aplicacion_Classroom.modulo)
print(Aplicacion_Classroom.profesores)
print(Aplicacion_Classroom.almacenamiento)
