def suma(n1,n2):
       resultado = n1 + n2
       print(resultado)

def resta(n1, n2):
    resultado = n1 - n2
    print(resultado)

def division(n1, n2):
    try:
        resultado = 0/0
    except ZeroDivisionError:
        print("Error! No se puede dividir por cero")
    else:
        resultado = n1 / n2
        print(resultado)

def multiplicacion(n1 , n2):
    resultado = n1 * n2
    print(resultado)
def salirSist():
    print('Fin del programa')
    return False

def parImpar():
    print('Ingrese diez números: ')
    index = 0
    numb = []
    even = []
    odd = []

    while index < 10:
        input()
        numb.append(index)
        index = index + 1
    for index in numb:
        if(index % 2 == 0):
            even.append(index)
        else:
            odd.append(index)
    print("Lista de numeros pares: ", even)
    print("Lista de numeros impares: ", odd)

def acumulator():
    index = 0
    numb = []
    print("Ingrese seis números: ")
    while index < 6:
        var = int(input())
        if(var <= 0):
            print("El numero ingresado es menor a 0 vuelva a intentarlo")
            break
        else:
            numb.append(var)
        index += 1
    print("Numeros ingresados: ", numb)