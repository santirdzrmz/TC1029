def fibonacci(number):
    n1=0
    n2=1
    total=0
    count = 29
    if number == 1:
        list = [0]
    elif number > 1:
        list = [0,1]
        while count<number:
            total = n1+n2
            list.append(total)
            n1=n2
            n2 = total
            count = count+1
    else:
        list = []
    return list

def main():
    boolean = True
    while boolean:
        print("Escribe el numero que quieres dentro de la secuencia de fibonacci: ")
        number = int(input())
        if number >= 0:
            boolean = False
        else:
            print("Escribe un numero valido.")
    list_fibonacci = fibonacci(number)
    print(list_fibonacci)
main()