class banco:

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

     #ATRIBUTOS
    cajero = ""   
    personal = ""   
    telefonos = ""        
    computadoras = ""      
    sillas = ""      
    ventanas = ""      
    camaras = ""        
    pantallas = ""      
    reloj = ""      
    lamparas = ""
               


coppel = banco()

#METODOS

coppel .activar ()
coppel.reporte ()
coppel.depositar ()
coppel.transacciones ()
coppel.otros ()

#ATRIBUTOS

coppel.cajero  = "4 cajeros para el retiro de dinero"
coppel.personal  = " 18 personal para esesoria de un cliente "
coppel.telefonos  = " 4 para activar tarjetas o desactivar"
coppel.computadoras  = "4 para poder tener un control de los clientes"
coppel.sillas  = "10 para los clientes"
coppel.ventanas  = "10 paredes o ventanas para comunicarse entre clientes"
coppel.camaras  = "10 para una seguridad de los clientes y personal"
coppel.pantallas  = " 4 para revisar el turno del siguiente cliente"
coppel.reloj  = "1 para tener una mejor tiempo por persona"
coppel.lamparas  = "12 parte de alumbrado del banco"

print(coppel.cajero )
print(coppel.personal )
print(coppel.telefonos )
print(coppel.computadoras )
print(coppel.sillas )
print(coppel.ventanas )
print(coppel.camaras )
print(coppel.pantallas )
print(coppel.reloj )
print(coppel.lamparas )
