class trasporte_avion:
    #Metodos
    def viajar(self):
        print("Viaja de punto a b")
    
    def seguridad(self):
        print("seguridad dentro del avion")
    
    def trasporte(self):
        print("trasporte de personas o cosas")

    def enfrenar(self):
        print("enfrenar al llegar a su punto")
    
    def aterrizar(self):
        print("aterrizar en un aeropuerto")


    #Atributos
    def alas(self):
        print("2")
    def asientos(self):
        print("220")
    def turbinas(self): 
        print("2")
    def ventanillas(self): 
        print("220")
    def baños(self):
        print("2")
    def tanque(self):
        print("2")
    def llantas(self):
        print("16")
    def caja(self):
        print("1")
    def botones(self):
        print("4000")
    def spoilers(self):
        print("1")

    #polimorfismo

    def viajar(self):
      print("viajar desde Ciudad de Mexico a Las vegas")
    
    def seguridad(self):
      print("La seguridad que se debe tener antes de subir un avion")

    def Alas(self):
      print("cada avion cuenta con dos alas para poder tener estabilidad y volar")
    
    def asientos(self):
      print("la cantidad d asientos depende de cada avion modelo")

    def turbinas(self):
      print("Las turbinas necesitan de combustible para poder volar")

    def ventanillas(self):
      print("uso de ventanillas para tener vista o poder grabar un video")

    def baños(self):
      print("uso de baño para el usario y parte del avion")

      #Herencia
class Bicicleta:
      #Metodos
    def __init__(self):
      print("Constructor bicileta")
    
    def frenar(self):
      print("frenar en una bajada")

    def acelerar(self):
      print("acelerar bicicleta") 

      #Atributos
    pedales = "2"
    asientos = "1"
    eje = "2"
    cadena = "1"
    llantas = "2"

objeto_avion = trasporte_avion()
objeto_avion.viajar()
objeto_avion.seguridad()
objeto_avion.trasporte()
objeto_avion.enfrenar()
objeto_avion.aterrizar()
print("alas = 2")
print("asientos = 220")
print("turbinas = 2")
print("ventanillas = 220")
print("baños = 2")
print("tanque = 2")
print("llantas = 16")
print("caja = 1")
print("botones =4000")
print("spoilers = 1")



objeto_bicicleta = Bicicleta()
objeto_bicicleta.frenar()
objeto_bicicleta.acelerar()
print("pedales 2")
print("asientos 1")
print("eje 2")
print("cadena 1")
print("llantas 2")

objeto_avion = trasporte_avion()
objeto_avion.alas()
objeto_avion.asientos()
objeto_avion.turbinas()
objeto_avion.ventanillas()
objeto_avion.baños()