print("Ingresa un numero entero positivo:")
numero=int(input())
if numero < 0:
    print("Factorial no definido para negativos")
elif numero == 0 or numero ==1:
    print("1")
else:
    total = numero
    for x in range(numero-1, 1, -1):
        total = x*total
    print(str(total))