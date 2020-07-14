class arreglos:
    def __init__(self):
        pass
    def metodo(self): 
        respuesta = "S"
        while respuesta == "S" or respuesta == "s": 

            centigrados = int(input("INGRESE LA TEMPERATURA EN CENTRIGRADOS:"))
            fahrengeit = 9/5 * centigrados + 32
            print(fahrengeit,"GRADOS FAHRENGEIT")
            fecha = input("¿CUAL ES LA FECHA DEL DIA DE HOY?:")
            print(fecha,"fecha del dia de hoy")

            file = open("temperaturas.txt",'w')
            file.write('centigrados = % str' %centigrados)
            file.write('fahrengeit = % str' %fahrengeit)
            file.write(fecha + 'w')
            file.close()

            print("s significa si y n significa no ")      
            respuesta = input("REQUIERE REALIZAR OTRA MIMSA RESPUESTA?: s/n ")
            if respuesta == "N" or respuesta == "n":              
                break       

objeto = arreglos()      
objeto.metodo() 