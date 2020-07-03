class Cajero:
    
    #metodos
    def retiros(self):
        print("Retiro de dinero desde cajeros ")
    
    def pagos(self):
        print("pagos de alguno usurio")

    def saldo(self):
        print("saber el saldo de tu banco ")
    
    def aplicacion(self):
        print("retirar desde la aplicacion del banco")
    
    def actualizacion(self):
        print("actualizar algun dato ")
    
   
     #atributos
    def tarjeta(self):
       print("1")
    def ticket(self): 
       print("1")
    def pantalla(self): 
        print("1")
    def botones(self): 
        print("20")
    def voz(self): 
        print("1")
    def calcula(self):
       print("1")
    def informacion(self):
       print("1")
    def cantidad(self):
       print("1000000")
    def identificacion(self):
       print("1")
    def verifica(self):
       print("1")
    
    #Polimorfismo
   
    def retiros(self):
       print("se puede retirar dinero desde cualquier banco")

    def pagos(self): 
       print("pagos desde tu tarjeta o aplicacion")

    def tarjeta(self): 
        print("tarjeta uso para pagos o abonos")

    def ticket(self): 
        print("te da el lugar y cantidad de dinero de retiro o pago")

    def pantalla(self): 
        print("ayuda a no perder algun dato")

    def botones(self):
       print("facilota el uso en el cajero")

    def voz(self):
       print("asistente que te permite y te brinda una ayuda")

       #Herencia
class coppel:
       #Metodo
    def __init__(self):
      print("Constructor coppel")

    def asesoria(self):
      print("te puede activar alguna tarjeta mediante el cajero")

    def pago(self):
      print("puedes pagar una compra")

      #Atributos

    cajeros = "1"
    ventanas = "4"
    camaras = "1"
    puerta = "1"
    salida = "1"
    


objeto_cajero = Cajero()
objeto_cajero.retiros()
objeto_cajero.pagos()
objeto_cajero.saldo()
objeto_cajero.aplicacion()
objeto_cajero.actualizacion()
print("tarjeta = 1")
print("ticktet = 1")
print("pantalla = 1")
print("botones = 20")
print("voz = 1")
print("calcula = 1")
print("informacion = 1")
print("cantidad = 1000000")
print("identificacion = 1")
print("verifica = 1")


objeto_cajero = coppel()
objeto_cajero.asesoria()
objeto_cajero.pago()
print("cajeros 1")
print("ventanas 4")
print("camaras 1")
print("puerta 1")
print("salida 1")

objeto_cajero = Cajero()
objeto_cajero.tarjeta()
objeto_cajero.ticket()
objeto_cajero.pantalla()
objeto_cajero.botones()
objeto_cajero.voz()