from functools import reduce 
def suma(n1,n2):
  return n1 + n2
    

def resta(n1, n2):
    return n1 - n2

def division(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError
    else :
        return n1 / n2
   
def multiplicar(n1 , n2):
    return n1 * n2
def salirSist():
    print('Fin del programa')
    return False

def parImpar(numeros):
    pares = list(filter(lambda numero : numero %2 == 0,numeros  ))
    impares = list(filter(lambda numero : numero %2 != 0,numeros  ))
    return pares , impares

def acumular(numeros):
    return reduce(lambda acumulado , numero : acumulado + numero , numeros)