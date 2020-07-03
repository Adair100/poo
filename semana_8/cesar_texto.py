class cesar: 
    def __init__(self):
        pass
    def metodo(self): 
        respuesta = "S"
        while respuesta == "S" or respuesta == "s":          
            texto = input("¿cual es su archivo de texto para cifrar o descifrar?: ")
            n = 3
            accion = input("¿para el texto se cifrara o descifrar?: ") 
            abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
            cif = ''
            texto = texto.upper()
            for s in texto:
                if s in abecedario:                    
                    num = abecedario.find(s) 
                    if accion == 'cifrara' : 
                        num = num + n
                    elif accion == 'descifrar' :
                        num = num - n                  
                    if num >= len(abecedario):
                        num = num - len(abecedario)
                    elif num < 0:
                        num = num + len(abecedario)                 
                    cif = cif + abecedario[num]
                else:                   
                    cif = cif + s
            print(cif)    
            print("s significa si y n significa no ")      
            respuesta = input("Que otro texto desea cifrar o descifrar ? s/n ")
            if respuesta == "N" or respuesta == "n":              
                break 
cesar = cesar()
cesar.metodo()
