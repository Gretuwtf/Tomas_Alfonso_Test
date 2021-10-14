from funciones import suma, resta, division, multiplicar, parImpar, acumulador
Menu = """ 
      Menu
  1- suma
  2- resta
  3- Multiplicacion
  4- division
  5- pares e impares 
  6- acumulador
"""

print(Menu)
def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
   
    Opcion = int(input("Selecione Opcion\n"))
    while (Opcion >0 and Opcion <5):
        n1 = int(input("Ingrese Numero"))
        n2 = int(input("Ingrese Otro Numero"))
        if (Opcion==1):
            suma()
        elif(Opcion==2):
            resta()
        elif(Opcion==3):
            division()
        elif(Opcion==4):
            multiplicar()
        elif(Opcion==5):
            parImpar()
        elif(Opcion==6):
            acumulador()    
        else :
            print ("Esa opcion existe")
Calculadora()