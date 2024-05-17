print("Introduce un numero entero ")
numero_entero = int(input())
print("Introduce un numero final")
numero_final = int(input())
if numero_entero > 0 and numero_final > 0:
    for i in range(numero_entero, numero_final, 5):
        print(i)
