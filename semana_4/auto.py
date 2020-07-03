class transporte_auto:
    #metodos
    def drifting(self):
        print("drifting")
    
    def subir(self):
        print("subir en un estacionamineto")

    def transportar(self):
        print("transporta accsorios")

    def pruebas(self):
        print("pruebas en el motor")

    def viajar(self):
        print("viajas de punto a b")

    #atributos
    def spliter(self):
        print("1")
    def llantas(self):
        print("4")
    def espejos(self):
        print("2")
    def rin(self):
        print("4")
    def escape(self): 
        print("4")
    def puertas(self):
        print("2")
    def cajuela(self):
        print("2")
    def aleron(self):
        print("1")
    def ventanas(self):
        print("2")
    def faros(self):
        print("2")

    #polimorfismo

    def drifting(self):
        print("driftear en un autodromo")

    def subir(self):
        print("sube en un estacionamiento o en la carretera")

    def spliter(self):
        print("tiene un uso ya que se mantiene pegado al piso a velocidades altas")

    def llantas(self):
        print("uso de llantas es primordial ya sea de uso normal o para pista")

    def espejos(self):
        print("se puede eviatr algun golpe o choque")

    def rin(self):
        print("existen diferentes rines ya sea de aluminio o fibra de carbono")

    def escape(self):
        print("un buen sonido proviene de un escape sin valvula")

    #Herncia
class Superdeportivo:
  
   #metodos
    def __init__(self):
        print("constructor superdeportivo")
    
    def encender(self):
        print("enciende con boton")

    def entradas(self):
        print("la aerodinamica para tener mejor flujo de aire")
   

     #atributos
    asientos = "1"
    ventanas = "2"
    motor = "1"
    spliter = "1"
    llantas = "4"
    palanca_de_locidades = "1"
    cajuela = "2"
    faros = "2"
    frenos = "4"
    rines = "4"   
    

objeto_auto = transporte_auto()
objeto_auto.drifting()
objeto_auto.subir()
objeto_auto.transportar()
objeto_auto.pruebas()
objeto_auto.viajar()
print("spliter = 1")
print("llantas = 4")
print("espejos = 2")
print("rin = 4")
print("escape = 4")
print("puertas = 2")
print("cajuela = 2")
print("aleron = 1")
print("ventanas = 2")
print("faros = 2")

objeto_superdeportivo = Superdeportivo()
objeto_superdeportivo.encender()
objeto_superdeportivo.entradas()
print("asientos 1")
print("ventanas 2")
print("motor 2")
print("spliter 1")
print("llantas 4")

objeto_auto = transporte_auto()
objeto_auto.spliter()
objeto_auto.llantas()
objeto_auto.espejos()
objeto_auto.rin()
objeto_auto.escape()