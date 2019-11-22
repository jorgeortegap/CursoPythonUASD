# 5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.
# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
# cien.


# -*- coding: utf-8 -*-
import random
usuario = "Admin"
passw = "1234"
saldo = random.randint(0, 1000000)
saldo2 = random.randint(0, 50000)
cont = 0
conectado = bool
while cont < 3:
    us = input("Ingrese usuario: ")
    co = input("Ingrese contrasena: ")
    if us == usuario and passw == co:
        print("Bienvenido al sistema")
        conectado = True
        break
    else:
        cont = cont+1
        print("Usuario y contraseña incorreta")
        conectado = False

while conectado == True:
    print("Que operacion desea utilizar?:")
    print("1.- Giro")
    print("2.- Deposito")
    print("3.- Traspaso")
    print("4.- Consulta Saldo")
    print("0.- Para cerrar")
    choi = int(input("Ingrese opcion:"))
    if choi == 1:
        monto = int(input("Ingrese monto a girar:"))
        saldo = saldo-monto
        print("ha retirado ", monto)
    elif choi == 2:
        monto = int(input("Ingrese monto a Depositar:"))
        saldo = saldo+monto
        print("su nuevo saldo es", saldo)
    elif choi == 3:
        cu2 = input("Ingrese cuenta a depositar")
        monto = int(input("Ingrese monto a Transferir:"))
        saldo = saldo-monto
        saldo2 = saldo2+monto
        print("se han transferido", monto, "pesos a la cuenta", cu2)
        print("el nuevo saldo es:", saldo2)
    elif choi == 4:
        print("Su saldo es:", saldo)
    elif choi == 0:
        break
