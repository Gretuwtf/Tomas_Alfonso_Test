from funciones import suma, resta, division, multiplicar, parImpar, acumular
Menu = """ 
      Menu
  1- suma
  2- resta
  3- multiplicacion
  4- division
  5- pares e impares 
  6- acumulador
"""

print(Menu)
opcion = 0 
while opcion != 7 : 
    opcion = int(input("Selecione Opcion"))
   
    if opcion==1:
        n1 = int(input("Ingrese Numero"))
        n2 = int(input("Ingrese Otro Numero"))
        resultado = suma(n1,n2)
        print(resultado)
    elif opcion==2:
        n1 = int(input("Ingrese Numero"))
        n2 = int(input("Ingrese Otro Numero"))
        resultado = resta(n1,n2)
        print(resultado)
    elif opcion==3:
        n1 = int(input("Ingrese Numero"))
        n2 = int(input("Ingrese Otro Numero"))
        resultado = multiplicar(n1,n2)
        print(resultado)
    elif opcion==4:
        n1 = int(input("Ingrese Numero"))
        n2 = int(input("Ingrese Otro Numero"))
        try : 
            resultado = division (n1,n2)
            print(resultado)
        except ZeroDivisionError : 
            print("no se puede divir por cero")
    elif opcion==5:
        numeros = [1,2,3,4,5,6,7,8,9,10]
        pares , impares = parImpar(numeros)
        print(f"los numeros pares son {pares} ")
        print(f"los numeros impares son {impares} ")
    elif opcion==6:
        numeros = []
        for i in range(6):
            numero = int(input("ingrese un numero : "))
            if numero > 0:
                numeros.append(numero)
            else :
                print("El numero ingresado es menor a 0 vuelva a intentarlo")    
        resultado = acumular(numeros)
        print(resultado)        
    elif opcion ==7:
        print("saliendo del sistema...")      
    else :
        print ("Esa opcion existe")