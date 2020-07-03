class Bancos:
    #metodos
    def activar(self):
        print("activa tu tarjeta nueva")
    
    def reporte(self):
        print("reporte en caso de robo")

    def depositar(self):
        print("deposita a otra cuenta")
    
    def transacciones(self):
        print("dinero de una cuenta a otra")
  
    def otros(self):
        print("se recibe alguna asesorias")

    #atributos
    def cajero(self):  
        print("1")
    def personal(self):
        print("80")
    def telefonos(self): 
        print("4")
    def computadoras(self): 
        print("20")
    def sillas(self): 
        print("20")
    def ventanas(self): 
        print("4")
    def camaras(self): 
        print("4")
    def pantallas(self):
        print("1")
    def reloj(self): 
        print("8")
    def lamparas(self):
        print("8")
    
    
    #polimorfismo
    def activar(self):
      print("se puede activar la nueva tarjeta que da el banco")
    
    def reporte(self):
      print("en caso de robo puede reportar su tarjeta")

    def cajero(self):
      print("retira dinero")
    
    def personal(self):
      print("apoyo a la persona ya sea en su tarjeta o algo mas")

    def telefonos(self):
      print("puedes marcar desde tu casa ")

    def computadoras(self):
      print("poder usar para los requerimientos del usaurio")

    def sillas(self):
      print("espera el turno para atender")
   
    #Herencia

class banamex:
    #Metodos
    def __init__(self):
        print("constructor banco")

    def deposito(self):
        print("Emitir o pagar un sevicio")
    
    def retiro(self):
        print("retiro de efectivo ")
  
    #Atributos
    encargado = "1"
    asistente = "17"
    encargado = "4"
    oficina = "4"
    impresora = "4"

objeto_banco = Bancos()
objeto_banco.activar()
objeto_banco.reporte()
objeto_banco.depositar()
objeto_banco.transacciones()
objeto_banco.otros()
print("cajero = 1")
print("personal = 80")
print("telefonos = 4")
print("computadoras = 20")
print("sillas = 20")
print("ventanas = 4")
print("camaras = 4")
print("pantallas = 1")
print("reloj = 8")
print("lamparas = 8")

objeto_banco = banamex()
objeto_banco.deposito()
objeto_banco.retiro()
print("encargado 1")
print("asistente 17")
print("encargado 4")
print("oficina 4")
print("impresora 4")

objeto_banco = Bancos()
objeto_banco.cajero()
objeto_banco.personal()
objeto_banco.telefonos()
objeto_banco.computadoras()
objeto_banco.sillas()    
