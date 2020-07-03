class Calculadora:
 
    #metodos
    def sumar(self):
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

    
    #Herencia
    
class calculadora_cientifica:

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

objeto_calculadora = Calculadora()
objeto_calculadora.sumar()
objeto_calculadora.restar()
objeto_calculadora.formula()
objeto_calculadora.punto()
objeto_calculadora.signo()
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



objeto_calculadora = calculadora_cientifica()
objeto_calculadora.resultado()
objeto_calculadora.formulas()
print("tapa 1")
print("panel 1")
print("pantalla 1")
print("pila 1")
print("rollo 1")

objeto_calculadora = Calculadora()
objeto_calculadora.color()
objeto_calculadora.tapa()
objeto_calculadora.boton()
objeto_calculadora.pantalla()
objeto_calculadora.panel()