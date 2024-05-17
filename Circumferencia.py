def calculador(a, b, x, y):
    distancia=abs((((b-y)**2+(a-x)**2)**0.5))

    return distancia
def main():
    print("Ingresa un radio:")
    radio =float(input())
    print("Ingresa la coordenada x del centro de la circumferencia:")
    a =float(input())
    print("Ingresa la coordenada y del centro de la circumferencia:")
    b =float(input())
    print("Ingresa la coordenada x de un punto:")
    x =float(input())
    print("Ingresa la coordenada y de un punto:")
    y =float(input())
    distancia = float(calculador(a, b, x, y))
    if (distancia == radio):
        print("Sobre")
    elif(distancia > radio):
        print("Fuera")      
    else:
        print("Dentro")

for x in range(1,4):
    main() 