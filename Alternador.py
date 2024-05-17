import random
def alternador(x):
    count = 0
    random_num=random.randint(1,2)
    if random_num == 1:
        binario = True
    else:
        binario = False
    while count <x:
        if binario == True:
            print("#")
            binario = False
        else:
            print("%")
            binario = True
        count = count+1
def main():
    print("Ingresa un número:")
    numero=int(input())
    alternador(numero)
main()
    