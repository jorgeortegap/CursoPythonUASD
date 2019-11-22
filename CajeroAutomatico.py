
Saldo = 100000
while True:
    print()
    print(".:Bienvenido a su cajero automatico:.")
    print()
    print("1. Ingresar dinero en su cuenta de ahorro: ")
    print("2. Retirar dinero de su cuenta de ahorro: ")
    print("3. Consulta de balance")
    print("4. Finalizar")
    print()
    Opcion = int(input("Por favor ingrese una opcion: "))
    print()

    if Opcion == 1:
        Ingreso = float(input("Por favor digite al monto a ingresar: "))
        Saldo += Ingreso
        print()
        print(f"Usted ha ingresado {Ingreso} pesos")
        print(f"Su nuevo balance es: {Saldo}")
    elif Opcion == 2:
        Retiro = float(input("Por favor digite al monto que desea retirar: "))
        if Retiro > Saldo:
            print()
            print(
                f"El monto a retirar de {Retiro}, es mayor que su balance de {Saldo}")
        else:
            Saldo -= Retiro
            print()
            print(f"Usted ha retirado {Retiro} pesos")
            print(f"Su nuevo balance es: {Saldo}")
    elif Opcion == 3:
        print(f"Su balance actual es de: {Saldo}")
    elif Opcion == 4:
        print("Gracias por utilizar nuestros servicios!")
        print()
        break
    else:
        print("Error, por favor elija una opcion del 1 al 4")
        print()
