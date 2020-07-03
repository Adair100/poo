class palindromo: 
    def __init__(self):
        pass
    def palindromo(self): 
        answ = "s" 
        
        while answ == "S" or answ == "s": 
            cad = input("¿Cual es tu cadena?: ")            
            cad = cad.lower() 
            cad= cad.replace(" ","") 
                   
            cad = cad.replace("A", "a") 
            cad = cad.replace("E", "e")
            cad = cad.replace("I", "i")
            cad = cad.replace("O", "o")
            cad = cad.replace("U", "u")
            numerovocales = 0
            for vocales in cad: 
                if vocales in "áéíóúaeiou":
                    numerovocales += 1
            print("Numero de vocales: "+str(numerovocales))
            
            palindromo = "" 
            for i in cad: 
                palindromo = i + palindromo 
            if cad == palindromo: 
                print("tu cadena si es un palindromo")
            
            else: 
                
                print("tu cadena no es un palindromo")
                print("s significa si n significa no") 
            answ = input("Desea anlizar otra cadena? s/n: ")
            if answ == "n" : 
                break 


palindromo = palindromo()

palindromo.palindromo()

