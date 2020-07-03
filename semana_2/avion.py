class Avion:

    #METODOS 

    def viajar(self):
        print("Viaja de punto a b")
    
    def seguridad(self):
        print("seguridad dentro del avion")
    
    def transporte(self):
        print("trasporte de personas o cosas")

    def enfrenar(self):
        print("enfrenar al llegar a su punto")
    
    def aterrizar(self):
        print("aterrizar en un aeropuerto")

     #ATRIBUTOS

    alas = "" 
    asientos = ""     
    turbinas = ""       
    ventanillas = ""     
    baños = "" 
    tanque = ""
    llantas = ""  
    caja = ""
    botones = ""  
    spoilers = ""       
 
avion_de_transporte_de_cosas = Avion()

     #MÉTODOS

avion_de_transporte_de_cosas.viajar()
avion_de_transporte_de_cosas.seguridad()
avion_de_transporte_de_cosas.transporte()
avion_de_transporte_de_cosas.enfrenar()
avion_de_transporte_de_cosas.aterrizar()

     #ATRIBUTOS

avion_de_transporte_de_cosas.alas = "cuenta con 2 alas de cada lado"
avion_de_transporte_de_cosas.asiento  = "asientos comodos dependiendo de que tipo de clase se pague"
avion_de_transporte_de_cosas.turbinas  = "turbinas dependindo el pesaje de avion"
avion_de_transporte_de_cosas.ventanillas  = "cada asiento tiene su propia ventanilla "
avion_de_transporte_de_cosas.baños  = "cuenta con 1 o 2 baños el avion"
avion_de_transporte_de_cosas.tanque  = "tanque de combustible y agua para un viaje largo"
avion_de_transporte_de_cosas.llantas  = "cada llanta ayuda para un aterrizajes y evitar daños al avion"
avion_de_transporte_de_cosas.caja  = "apartados para poder tener almacenamiento de cada maleta"
avion_de_transporte_de_cosas.botones  = "para tener ya sea manejo o diferentes usos"
avion_de_transporte_de_cosas.spoilers  = "una mejor aerodinamica del vuelo y avion"


print(avion_de_transporte_de_cosas.alas)
print(avion_de_transporte_de_cosas.asiento )
print(avion_de_transporte_de_cosas.turbinas )
print(avion_de_transporte_de_cosas.ventanillas )
print(avion_de_transporte_de_cosas.baños )
print(avion_de_transporte_de_cosas.tanque )
print(avion_de_transporte_de_cosas.llantas )
print(avion_de_transporte_de_cosas.caja )
print(avion_de_transporte_de_cosas.botones )
print(avion_de_transporte_de_cosas.spoilers )