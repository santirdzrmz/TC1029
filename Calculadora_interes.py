print("Ingresa tu nombre: ")
name = str(input())
print("Ingresa tu saldo inicial: ")
saldo = int(input())
print("Ingresa tu deposito de octubre: ")
deposito = int(input())
print("Ingresa tu retiro de octubre: ")
retiro = int(input())
tasa_interes = 0.08
interes_total = 0
count = 1
while count < 13:
    interes_mensual = saldo * tasa_interes / 12
    saldo = saldo + interes_mensual
    interes_total = interes_mensual + interes_total
    if count == 10:
        saldo = deposito + saldo
    elif count == 12:
        saldo = saldo-retiro
    print("El saldo en el mes "+ str(count)+" es: "+ str(round(saldo)))
    count = count +1
print("El saldo al final del año es: "+ str(round(saldo)))
print("El interes ganado al final del año es: "+ str(round(interes_total)))
