class banamex:

    #MÉTODOS
    def retiros(self):
        print("Retiro de dinero desde cajeros")
    
    def pagos(self):
        print("pagos de alguno usurio")
    
    def saldo(self):
        print("saber el saldo de tu banco")

    def aplicacion(self):
        print("retirar desde la aplicacion del banco")
    
    def actualizacion(self):
        print("actualizar algun dato")

     #ATRIBUTOS
    teclas = ""
    pantalla = ""
    espejo = ""
    ticket = ""
    salida_efectivo = ""

Cajero_coppel_banamex = banamex()
#metodos
Cajero_coppel_banamex.retiros()
Cajero_coppel_banamex.pagos()
Cajero_coppel_banamex.saldo()
Cajero_coppel_banamex.aplicacion()
Cajero_coppel_banamex.actualizacion()

#atributos

Cajero_coppel_banamex.teclas = "20 botones que muestra el cajero"
Cajero_coppel_banamex.pantalla = "1 pantala que el cajero presenta lo que consultas"
Cajero_coppel_banamex.espejo = "ayuda a evitar que es lo que esta a tu espalda"
Cajero_coppel_banamex.ticket = "ayuda a presentar la catindad de retiro o pago"
Cajero_coppel_banamex.salida_efectivo = "un apartado donde retira el efectivo del cajero"

print(Cajero_coppel_banamex.teclas)
print(Cajero_coppel_banamex.pantalla)
print(Cajero_coppel_banamex.espejo)
print(Cajero_coppel_banamex.ticket)
print(Cajero_coppel_banamex.salida_efectivo)








