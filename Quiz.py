def contador(oracion):
    lista = [char for char in oracion]
    n=0
    cuenta=0
    while n < len(lista):
        if lista[n] == ".":
            cuenta = cuenta+1
        n = n+1
    return cuenta

def main():
    oracion = str(input("Otorga un parrafo:"))
    cuenta=str(contador(oracion))
    print("Numero de oraciones terminadas con punto: "+cuenta)

main()

