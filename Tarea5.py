def list_creator(cantidad):
    n=0
    list = []
    while n<cantidad:
        print("Ingrese un numero entero a la lista: ")
        list.append(int(input()))
        n =n+1
    return list

def even(list_total):
    n=0 
    list_even = []
    while n < len(list_total):
        remainder = list_total[n]%2
        if remainder == 0:
            list_even.append(list_total[n])
        n = n+1
    return list_even

def odd(list_total):
    n=0 
    list_odd = []
    while n < len(list_total):
        remainder = list_total[n]%2
        if remainder != 0:
            list_odd.append(list_total[n])
        n = n+1
    return list_odd

def main():
    print("Ingrese su cantidad de datos: ")
    cantidad = int(input())
    list_total = list_creator(cantidad)
    list_even= even(list_total)
    list_odd = odd(list_total)
    print("Lista original: ")
    print(list_total)
    print("Pares: ")
    print(list_even)
    print("Impares: ")
    print(list_odd)


main()