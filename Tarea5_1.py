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
            print("pos "+str(n)+" ,valor "+str(list_total[n]))
        n = n+1

def main():
    print("Ingrese su cantidad de datos: ")
    cantidad = int(input())
    list_total = list_creator(cantidad)
    even(list_total)


main()