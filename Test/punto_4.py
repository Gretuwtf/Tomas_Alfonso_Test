# Mi_lista = [1,4,7,3,21]
# for x in Mi_lista:
#     print(x)


valor = int(input('Introduce un número del 1 al 6: '))
while valor<1 or valor>6:
    print("El numero tiene que ser entre en 1 y el 6.")
    valor = int(input('Introduci un número del 1 al 6: '))
if valor == 1:
    print('Elejiste el numero uno.')
elif valor == 2:
    print('Elejiste el numero dos.')
elif valor == 3:
    print('Elejiste el numero tres.')
elif valor == 4:
    print('Elejiste el numero cuatro.')
elif valor == 5:
    print('Elejiste el numero cinco.')
elif valor == 6:
    print('Elejiste el numero seis.')