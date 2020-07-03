class auto:
   
    #MÉTODOS
    def correr(self):
        print("correr en una pista,autodromo,trackday o carretera")
    
    def encender(self):
        print("encender el motor para poder tener uso del auto")
    
    def apagar(self):
        print("apagar para eviatr el uso de electricidad o gasolina")

    def rodar(self):
        print("rodar las llantas para evitar alguna ponchadura")
    
    def acelerar (self):
        print("Acelera de punto a,b")
        
    #ATRIBUTOS
    motor = ""
    caja_velocidades = ""
    aceite = ""
    tanque_gasolina = ""
    rin = ""
    llantas = ""
    espejos = ""
    ventanas = ""
    asientos = ""
    slip = ""


bugatti = auto()

#METODOS

bugatti.correr()
bugatti.encender()
bugatti.apagar()
bugatti.rodar()
bugatti.acelerar()


#ATRIBUTOS 

bugatti.motor = "un motor 12 cilindros."
bugatti.caja_velocidades = "cuenta con 8 velocidades 2 clush"
bugatti.aceite  = "especial para su motor"
bugatti.tanque_gasolina  = "12 cilindros v12"
bugatti.rin   = "22 especial para el auto"
bugatti.llantas  = "r8888 michelin"
bugatti.espejos = "2 parte d los costados y 1 de retrovisor"
bugatti.ventanas  = "2 ventanas de puerta electricas"
bugatti.asientos  = "2 con forma de pista para un mejor manejo"
bugatti.slip  = "1 para mejor aerodinamica"

print(bugatti.motor)
print(bugatti.caja_velocidades)
print(bugatti.aceite )
print(bugatti.tanque_gasolina )
print(bugatti.rin )
print(bugatti.llantas )
print(bugatti.espejos )
print(bugatti.ventanas )
print(bugatti.asientos)
print(bugatti.slip )