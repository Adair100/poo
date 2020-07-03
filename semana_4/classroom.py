class Classroom:
 
    #metodos
    def entregar(self):
        print("Sumar una cantidad")
    def restar(self):
        print("Resta una cantidad")
    def formula(self):
        print("ds formula en resolver ")
    def punto(self):
        print("punto para una cifra")
    def signo(self):
        print("de una cifra")

    #atributos
    def color(self): 
        print("1") 
    def tapa(self):
        print("1")
    def boton(self): 
        print("16")
    def pantalla(self):
        print("1")
    def panel(self):
        print("1")
    def botones_formula(self):
        print("10")
    def tamaño(self):
        print("20")
    def pantalla_color(self):
        print("1")
    def resultado(self):
        print("1000000")
    def pilas(self):
        print("1")

    #pilomorfismo

    def sumar(self):
        print("suma cifras que el usario necesita")

    def restar(self):
        print("resta las cifras que el usario necesita")

    def color(self):
        print("color que este en la calculadora por parte de la fabrica")

    def boton(self):
        print("encendido o apagado")

    def pantalla(self): 
        print("pantalla donde da el resultado en cifras")

    def panel(self): 
        print("carga mediate un panel a la luz solar")

    def boton_formula(self):
        print("formula que da al usario")
    
    #Herencia
    
class classroom:

    #Metodos
    def __init__(self):
      print("Constructor calculadora")

    def resultado(self):
      print("da un resultado con formulas")

    def formulas(self):
      print("botones que ayuda en formulas para el usuario")

    #Atributos
    tapa = "1"
    panel = "1"
    pantalla = "1"
    pila = "1"
    rollo = "1"

objeto_Classroom = Classroom()
objeto_Classroom.entregar()
objeto_Classroom.restar()
objeto_Classroom.formula()
objeto_Classroom.punto()
objeto_Classroom.signo()
print("color = 1")
print("tapa = 1")
print("boton = 16")
print("pantalla = 1")
print("panel = 1")
print("botones_formula = 10")
print("tamaño = 20")
print("pantalla_color = 1")
print("resultado = 1000000")
print("pilas = 1")



objeto_classroom = classroom()
objeto_classroom.resultado()
objeto_classroom .formulas()
print("tapa 1")
print("panel 1")
print("pantalla 1")
print("pila 1")
print("rollo 1")

objeto_classroom  = Classroom()
objeto_classroom.color()
objeto_classroom.tapa()
objeto_classroom.boton()
objeto_classroom.pantalla()
objeto_classroom.panel()